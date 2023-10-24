import os
import shutil
import typer
import socket
from zeroconf import ServiceInfo, Zeroconf

from src.code_generator import generate_code, generate_port
from src.utils import get_local_ip, send_file

app = typer.Typer(help="Pasta, a peer-to-peer command line file transfer tool.")

@app.command()
def send(file_path: str):
	"""
	Send a file or folder.
	
	Args:
		file_path (str): The path to the file or folder to send.
	"""
	isFolder:bool = False

	# Exit if specified file path does not exist
	if not os.path.exists(file_path):
		typer.echo("The specified path does not exist.")
		raise typer.Exit()
	
	# Zip file if a folder is the input
	if os.path.isdir(file_path):
		shutil.make_archive(file_path, 'zip', file_path)
		file_path += '.zip'
		# We will use this to make sure we unzip only if this is set to true at the receipient end.
		isFolder = True

	code = generate_code()
	port = generate_port(code)

	# Advertise the service over zeroconf
	info = ServiceInfo(
		"_pasta._tcp.local.",
		f"{code}._pasta._tcp.local.",
		addresses=[socket.inet_aton(get_local_ip())],
		port=port,
		properties={'isFolder': 'true' if isFolder else 'false'},
		server=f"{socket.gethostname()}.local.",
    )

	zeroconf = Zeroconf()
	typer.echo(f"Registering service {info.type} with name {info.name}")
	zeroconf.register_service(info)

	typer.echo(f"File prepared for sending. Share this command with the receiver:\n\npasta receive {code}\n")

		# Set up a server socket to listen for a connection
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((get_local_ip(), port))
		s.listen()
		s.settimeout(300)
		typer.echo('Waiting for connection from receiver...')
		try:
			conn, addr = s.accept()
		except socket.timeout:
			typer.echo('No connection received within 5 minutes. Exiting.')
			zeroconf.unregister_service(info)
			return
		with conn:
			typer.echo('Connected by', addr)
			send_file(file_path, s)

	# Unregister the service
	zeroconf.unregister_service(info)

@app.command()
def receive(code: str, output_path: str = typer.Option('.', '--output', '-o', help="The path where the received file will be saved.")):
	"""
	Receive a file or folder.
	
	Args:
		code (str): The unique code to connect to the sender.
		output_path (str, optional): The path where the received file will be saved. Defaults to the current directory.
	"""

	isFolder:bool = False

	# Check if the output path is a valid directory
	if not os.path.isdir(output_path):
		typer.echo(f"Error: The output path {output_path} is not a valid directory.")
		raise typer.Exit(code=1)

if __name__ == "__main__":
	app()

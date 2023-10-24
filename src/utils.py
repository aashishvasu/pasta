import os
import socket

from progress.bar import ChargingBar

def get_local_ip():
	"""
	Get the local IP address of the machine.

	Returns:
		str: The local IP address.
	"""
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't have to be reachable
		s.connect(('10.255.255.255', 1))
		return s.getsockname()[0]
	except Exception:
		return '127.0.0.1'
	finally:
		s.close()

def send_file(file_path: str, conn: socket.socket):

	# Open the file in binary mode
	with open(file_path, 'rb') as f:
		# Get the size of the file
		file_size = os.path.getsize(file_path)

		# Send the size of the file
		conn.sendall(file_size.to_bytes(8, 'big'))

		bar = ChargingBar("sending", max=file_size)

		# Send the file
		while True:
			# Read up to 1024 bytes from the file
			bytes_read = f.read(1024)
			if not bytes_read:
				# File sending is done
				bar.finish()
				break
			conn.sendall(bytes_read)

			# Update the progress bar
			bar.next(len(bytes_read))
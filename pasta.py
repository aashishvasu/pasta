import typer
from typing import List, Optional

import src.receiver as receiver
import src.sender as sender

app = typer.Typer()

def version_callback(value:bool):
	if value:
		import src.consts as consts
		typer.echo(f"Pasta Version: {consts.VERSION}")
		raise typer.Exit()

def update_callback(value:bool):
	if value:
		typer.echo("Checking for updates...")
		raise typer.Exit()

@app.command()
def send(paths:Optional[List[str]], port:int = 9867):
	sender.register_sender_service(paths, port)

@app.command()
def receive(uid: str, port:int = 9867):
	receiver.register_receiver_service(uid, port)

@app.callback()
def common(
	ctx:typer.Context,
	version:bool = typer.Option(None, "--version", callback=version_callback),
	update:bool = typer.Option(None, "--update", callback=update_callback)
):
	pass

if __name__ == "__main__":
	app()
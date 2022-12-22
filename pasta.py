import typer
from typing import List, Optional

import src.receiver as receiver
import src.sender as sender

app = typer.Typer()

@app.command()
def send(paths:Optional[List[str]], port:int = 9867):
	sender.register_sender_service(paths, port)

@app.command()
def receive(uid: str, port:int = 9867):
	receiver.register_receiver_service(uid, port)

if __name__ == "__main__":
	app()
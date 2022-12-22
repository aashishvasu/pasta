import socket
import os

import src.consts as consts
import src.print as printer
def start_handshake_client(host:str, port:int, filename:str, isZipped:bool):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		size = os.path.getsize(filename)
		s.connect((host, port))
		s.sendall(f"{filename}|{size}|{isZipped}".encode('utf-8'))
		data = s.recv(1024)

	return int(data.decode('utf-8'))

def start_transfer_client(host:str, port:int, filename:str, cleanup):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((host, port))

		with open(filename, "rb") as f:
			size = os.path.getsize(filename)
			counter = 0
			while True:
				# read the bytes from the file
				bytes_read = f.read(consts.BUF_SIZE)
				if not bytes_read:
					# file transmitting is done
					break
				# we use sendall to assure transimission in 
				# busy networks
				s.sendall(bytes_read)
				# update the progress bar
				counter += len(bytes_read)
				printer.print_percent_done(counter, size, title="Sending")

	s.close()
	cleanup()
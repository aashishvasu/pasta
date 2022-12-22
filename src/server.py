import socket

import src.consts as consts
import src.print as printer

# Bind a handshake socket
def start_handshake_server(port:int, recv_port:int):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((consts.IP_ADDR, port))
		s.listen()
		conn, addr = s.accept()
		with conn:
			while True:
				data = conn.recv(1024)
				if not data:
					break
				elif data.decode('utf-8') != '':
					conn.sendall(str(recv_port).encode('utf-8'))
					break

	return data.decode('utf-8')

def start_transfer_server(filename:str, size:int, port:int):
	print("Starting transfer")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((consts.IP_ADDR, port))
		s.listen()
		conn, addr = s.accept()
		
		with open (filename, 'wb') as f:
			counter = 0
			while True:
				# Read bytes from socket
				bytes_read = conn.recv(consts.BUF_SIZE)
				if not bytes_read:    
					# nothing is received
					# file transmitting is done
					break
				
				# Write to file
				f.write(bytes_read)

				# update the progress bar
				counter += len(bytes_read)
				printer.print_percent_done(counter, size, title="Receiving")

	# close the client socket
	conn.close()
	# close the server socket
	s.close()


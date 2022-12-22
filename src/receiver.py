import socket
import random
from zeroconf import ServiceInfo, Zeroconf

import src.consts as consts
import src.server as server
import src.filehandler as filehandler

zeroconf = Zeroconf()

recv_port = random.randrange(9868, 15000)
def register_receiver_service(uid:str, port:int, type:str = "handshake"):
	print("Your IP Address is: " + consts.IP_ADDR)

	# Other useful info
	props = {
				"id": uid,
				"type:": type
			}

	# This unique phrase will be used for all further communication
	info = ServiceInfo(
						consts.SERVICE_TYPE,
						f"{uid}.{consts.SERVICE_TYPE}",
						addresses=[socket.inet_aton(consts.IP_ADDR)],
						port=port,
						properties=props
						)

	print(f"Waiting for data at {uid}")
	zeroconf.register_service(info)
	data = server.start_handshake_server(port, recv_port).split('|')
	filename = data[0]
	size = int(data[1])
	isZipped = True if data[2] == "True" else False

	if filename != '':
		server.start_transfer_server(filename, size, recv_port)

	if isZipped:
		filehandler.extract_zip(filename)
		import os
		os.remove(filename)

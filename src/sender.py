from zeroconf import ServiceInfo, ServiceBrowser, ServiceListener, Zeroconf

from time import sleep

import src.phrase as phrase
import src.consts as consts
import src.client as client
import src.filehandler as filehandler

class Listener(ServiceListener):
	filename:str = ''
	isZipped = False
	info:ServiceInfo = None
	canQuit = False

	def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
		print(f"Service {name} updated")

	def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
		print(f"Service {name} removed")

	def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
		self.info = zc.get_service_info(type_, name)
		port = client.start_handshake_client(self.info.parsed_addresses()[0], self.info.port, self.filename, self.isZipped)
		if port != 0:
			client.start_transfer_client(self.info.parsed_addresses()[0], port, self.filename, self.cleanup)

	def cleanup(self):
		if self.isZipped:
			import os
			os.remove(self.filename)
		self.canQuit = True

zeroconf = Zeroconf()


def register_sender_service(filepaths:list, port:int):
	uid = phrase.get_random_phrase()

	# Get a consolidated path
	path, isZipped = filehandler.get_consolidated_path(filepaths, phrase.get_short_phrase(uid))
	
	print (f"Type\n\n    pasta receive {uid} {f'--port {port}' if port != 9867 else ''}\n\non the receiving machine")

	listener = Listener()
	listener.filename = path
	listener.isZipped = isZipped
	browser = ServiceBrowser(zeroconf, consts.SERVICE_TYPE, listener)

	try:
		while listener.canQuit == False:
			sleep(0.1)
	except KeyboardInterrupt:
		pass
	
	zeroconf.close()
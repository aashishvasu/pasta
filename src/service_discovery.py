import threading
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf

from src.utils import get_ip_str

class PastaServiceListener(ServiceListener):

	code:str=''
	service_ip:str=None
	isFolder:bool = False
	filename:str=''
	filesize:int=0
	service_found: threading.Event = None

	def __init__(self):
		self.service_found = threading.Event()

	def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
		print(f"Service {name} removed")
		code=''

	def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
		info = zc.get_service_info(type_, name)
		if(info):
			if(name == f"{self.code}.{type_}"):
				self.service_ip = get_ip_str(info.addresses.pop())
				self.isFolder = info.properties.get(b'isFolder', b'false') == b'true'
				self.filename = info.properties.get(b'filename').decode()
				self.filesize = int.from_bytes(info.properties.get(b'filesize'))
				print(self.isFolder)
				print(self.service_ip)
				print(self.filename)
				print(self.filesize)
				self.service_found.set()


def discover_service(type_, code, timeout=30):
	zeroconf = Zeroconf()
	listener = PastaServiceListener()
	listener.code = code
	browser = ServiceBrowser(zeroconf, type_, listener)

	try:
		found = listener.service_found.wait(timeout)  # Wait until the service is found or the timeout expires
		if not found:
			raise Exception("Service not found within timeout period")  # Wait until the service is found or the timeout expires
	finally:
		zeroconf.close()

	return listener.service_ip, listener.isFolder, listener.filename, listener.filesize
from zeroconf import ServiceInfo, ServiceBrowser, ServiceStateChange, Zeroconf

from time import sleep

import src.phrase as phrase
import src.consts as consts
import src.client as client
from src.job import Job

zeroconf = Zeroconf()
current_job:Job

def cleanup():
	global current_job
	if current_job.isZipped:
		import os
		os.remove(current_job.consolidated_path)
		current_job.done = True

# Define a callback function to be called when a service is added or removed
def on_service_state_change(zeroconf, service_type, name, state_change):
	global current_job
	if state_change == ServiceStateChange.Added:
		info:ServiceInfo = zeroconf.get_service_info(service_type, name)
		current_job.generate_consolidated_file()
		port = client.start_handshake_client(info.parsed_addresses()[0], info.port, current_job.consolidated_path, current_job.isZipped)
		if port != 0:
			client.start_transfer_client(info.parsed_addresses()[0], port, current_job.consolidated_path, cleanup=cleanup)

def register_sender_service(filepaths:list, port:int):
	uid = phrase.get_random_phrase()
	global current_job
	current_job = Job(uid, filepaths)
	
	print (f"Type\n\n    pasta receive {uid} {f'--port {port}' if port != 9867 else ''}\n\non the receiving machine")
	global zeroconf
	browser = ServiceBrowser(zeroconf, consts.SERVICE_TYPE, handlers=[on_service_state_change])
	
	# Wait for services to be added or removed
	try:
		while current_job.done == False:
			sleep(0.1)
	except KeyboardInterrupt:
		pass

	# Close the Zeroconf instance	
	zeroconf.close()
	exit()
from zeroconf import ServiceBrowser, Zeroconf

class ServiceListener:

    def __init__(self, zeroconf, type, name):
        self.zeroconf = zeroconf
        self.type = type
        self.name = name

    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print(f"Service {name} added, service info: {info}")

def discover_service(service_type, timeout=10):
    zeroconf = Zeroconf()
    listener = ServiceListener()
    browser = ServiceBrowser(zeroconf, service_type, listener)
    zeroconf.wait(timeout)
    zeroconf.close()

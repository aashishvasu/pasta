import socket

VERSION = "v0.3"

SERVICE_TYPE = "_pasta._tcp.local."

HNAME = socket.gethostname()
IP_ADDR = socket.gethostbyname(HNAME)
BUF_SIZE = 4096
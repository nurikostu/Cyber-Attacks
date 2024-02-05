import socket

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = "192.168.18.129"

port =81


try:
	s.connect((ip,port))
	print(str(port),"open")
except Exception as e:
	print(str(port),"closed")
finally:
	pass

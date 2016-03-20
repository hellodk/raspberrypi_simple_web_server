import socket
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ainfo = socket.getaddrinfo("192.168.1.107", 1234)
so.connect(ainfo[0][4])
so.sendall(b"Got a request!")
so.close()

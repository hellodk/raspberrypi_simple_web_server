import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket Created"
ainfo = socket.getaddrinfo('0.0.0.0', 12345)
print ainfo
print ainfo[0][4]
so.bind(ainfo[0][4])
so.listen(5)
conn, addr = so.accept()
data = conn.recv(1000)
print data
conn.close()
so.close()
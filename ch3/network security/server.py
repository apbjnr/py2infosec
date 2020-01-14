#!/usr/bin/python
import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# needed to close socket, otherwise socket stays open, and cannot bin to the ip and port again until socket closed.
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))

tcpSocket.listen(2)

# echo server - return any data sent from client back to the client

print "waiting for a client ... "
(client, (ip, sock)) = tcpSocket.accept()

print "received connection from : ", ip

print "starting echo output ...."

data = 'dummy'

# running a loop to keep on receiving data from a client and sending back the data. this will go on until the client or server closed the connection.
while len(data)  :

	data = client.recv(2048)
	print "client sent:  ",data
	client.send(data)


print "closing connection ..."
client.close()

print "shutting down server ..."
tcpSocket.close()

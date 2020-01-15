#!/usr/bin/python

import socket
import sys

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## sys.argv[1] = user input
tcpSocket.connect((sys.argv[1], 8000))

while 1 :
	userInput = raw_input("please enter a string: ")
	tcpSocket.send(userInput)
	print tcpSocket.recv(2048)


tcpSocket.close()

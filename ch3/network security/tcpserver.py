#!/bin/bash

import SocketServer
import socket

class EchoHandler(SocketServer.BaseRequestHandler) :

	def handle(self) :

		print "got connection from : ", self.client_address
		data = 'dummy'

		while len(data) :
			data = self.request.recv(1024)
			self.request.send(data)

		print "client left"


serverAddr = ("0.0.0.0", 9000)

server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever() 

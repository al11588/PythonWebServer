#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = input('Please Enter A Server Port: ')#input server port for user
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
	#Establish the connection

	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
	try:
		message = connectionSocket.recv(1024)#Fill in start #Fill in end
		filename = message.split()[1]
		print message 
		f = open(filename[1:])
		outputdata = f.read() #Fill in start #Fill in end
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send('\nEverything is OK\n')
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()
		print 'File Received'
	except IOError:
		#Send response message for file not found
		#Fill in start
		connectionSocket.send('\n404 File Not Found\n')
		#Fill in end
		#Close client socket
		#Fill in start
connectionSocket.close()
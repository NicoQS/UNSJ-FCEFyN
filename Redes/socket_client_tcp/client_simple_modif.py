""" #Intercambiar datos con el servidor
import socket

HOST = 'localhost'
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	while True:
		data = 'GET / HTTP/1.0\r\n\r\n'
		if  not data:
			break
		client.send(data.encode('utf-8'))
		data = client.recv(BUFSIZ)
		if not data:
			break
		print(data.decode('utf-8'))
	client.close() """

import socket

HOST = 'localhost'
PORT = 12345
BUFSIZ = 256

if __name__ == '__main__':
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = input('Enter the host: ') or HOST
	port = input('Enter the port: ') or PORT

	sock_addr = (host, int(port))
	client_socket.connect(sock_addr)

	payload = 'GET TIME'
	try:
		while True:
			client_socket.send(payload.encode('utf-8'))
			data = client_socket.recv(BUFSIZ)
			print(repr(data))
			more = input('Want to send more data to server[y/n]: ')
			if more.lower() == 'y':
				payload = input('Enter payload: ')
			else:
				break
	except KeyboardInterrupt:
		print('Exited by user')
	client_socket.close()
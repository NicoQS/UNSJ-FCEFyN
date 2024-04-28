import socket 
import sys

if __name__ == '__main__':
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as e:
		print('Failed to create a socket')
		print('Reason: {}'.format(e))
		sys.exit()
	print('Socket created successfully')

	target_host = input('Enter the target host: ')
	target_port = int(input('Enter the target port: '))
	try:
		sock.connect((target_host, target_port))
		print('Socket connected successfully to {} on port {}'.format(target_host, target_port))
		sock.shutdown(2)
	except socket.error as e:
		print('Failed to connect to {} on port {}'.format(target_host, target_port))
		print('Reason: {}'.format(e))
		sys.exit()
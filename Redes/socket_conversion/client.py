import socket

HOST = 'localhost'
PORT = 5000

def query_socket(request):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(request.encode('utf-8'))
		return s.recv(1024).decode('utf-8')

while True:
	valor = float(input('Ingrese el valor a convertir: '))
	moneda1 = input('Ingrese la moneda a convertir (dolar/peso): ')
	moneda2 = input('Ingrese la moneda a la que desea convertir (dolar/peso): ')
	response = query_socket(f'{valor};{moneda1};{moneda2}')
	print('El valor {} de {} a {} es: {}'.format(valor,moneda1, moneda2, response))
	continuar = input('Desea continuar? (s/n): ')
	if continuar == 'n':
		break
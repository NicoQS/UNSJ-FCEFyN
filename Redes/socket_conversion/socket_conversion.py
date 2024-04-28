import socket
import requests

HOST = 'localhost'
PORT = 5000

datosApi = requests.get('https://www.dolarsi.com/api/api.php?type=dolar').json()
valorDolar = float(datosApi[1]['casa']['venta'].replace(',','.')) # Dolar blue venta


def handle_request(conn):
	data = conn.recv(1024).decode('utf-8')
	valor, *tipMoneda = data.split(';')
	if tipMoneda[0] == 'dolar':
		result = round(float(valor) * valorDolar,2)
	elif tipMoneda[0] == 'peso':
		result = round(float(valor) / valorDolar,2)
	else:
		result = 'Invalid service number'
	conn.sendall(str(result).encode('utf-8'))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	while True:
		conn, addr = s.accept()
		with conn:
			try:
				handle_request(conn)
			except Exception as e:
				conn.sendall('Invalid request'.encode('utf-8'))
				conn.close()
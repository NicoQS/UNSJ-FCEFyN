"""
División de polinomios en GF(2) (módulo 2).

Funciones principales:
- parse_poly(str) -> list de coeficientes (0/1), índice = grado
- poly_to_str(coeffs) -> representación legible
- poly_divmod(dividend, divisor, verbose=False) -> (quotient, remainder)

El script incluye una demo con el ejemplo pedido: (x^15 + 1) ÷ g(x).
"""

from typing import List, Tuple


def trim(poly: List[int]) -> List[int]:
	"""Remueve ceros de alto grado (trim leading zeros). poly índice = grado."""
	if not poly:
		return [0]
	i = len(poly) - 1
	while i > 0 and poly[i] == 0:
		i -= 1
	return poly[: i + 1]


def degree(poly: List[int]) -> int:
	p = trim(poly)
	return len(p) - 1


def parse_poly(s: str) -> List[int]:
	"""Parsea cadenas tipo 'x^15 + 1' ó 'x^10 + x^8 + x + 1' a lista de bits (coeficientes).

	Acepta espacios y términos separados por '+'.
	"""
	s = s.replace(' ', '')
	if s == '' or s == '0':
		return [0]
	parts = s.split('+')
	exps = []
	for part in parts:
		if part == '':
			continue
		if part == '1':
			exps.append(0)
		elif part == 'x':
			exps.append(1)
		elif part.startswith('x^'):
			try:
				exps.append(int(part[2:]))
			except ValueError:
				raise ValueError(f'Término no válido: {part}')
		else:
			# intentar parseo de forma 'ax^n' no soportado (coeficiente distinto de 1)
			raise ValueError(f'Término no soportado o inválido: {part}')
	maxexp = max(exps) if exps else 0
	poly = [0] * (maxexp + 1)
	for e in exps:
		poly[e] = (poly[e] + 1) % 2
	return trim(poly)


def poly_to_str(poly: List[int]) -> str:
	p = trim(poly)
	if all(c == 0 for c in p):
		return '0'
	terms = []
	for i in range(len(p) - 1, -1, -1):
		if p[i]:
			if i == 0:
				terms.append('1')
			elif i == 1:
				terms.append('x')
			else:
				terms.append(f'x^{i}')
	return ' + '.join(terms)


def poly_xor_shift(dividend: List[int], divisor: List[int], shift: int) -> None:
	"""XOR (suma en GF(2)) divisor desplazado por 'shift' dentro de dividend in-place."""
	# asegurar longitud suficiente
	needed = shift + len(divisor)
	if len(dividend) < needed:
		dividend.extend([0] * (needed - len(dividend)))
	for i in range(len(divisor)):
		dividend[i + shift] ^= divisor[i]


def poly_mul(a: List[int], b: List[int]) -> List[int]:
	"""Multiplicación de polinomios en GF(2)."""
	if not a or not b:
		return [0]
	res = [0] * (len(a) + len(b) - 1)
	for i, ai in enumerate(a):
		if ai:
			for j, bj in enumerate(b):
				if bj:
					res[i + j] ^= 1
	return trim(res)


def poly_divmod(dividend: List[int], divisor: List[int], verbose: bool = False) -> Tuple[List[int], List[int]]:
	"""Divide dividend ÷ divisor en GF(2). Devuelve (cociente, resto)."""
	dd = trim(dividend[:])
	dv = trim(divisor[:])
	if all(c == 0 for c in dv):
		raise ZeroDivisionError('Divisor nulo')
	
	# Si el grado del dividendo es menor que el del divisor, la división no puede proceder
	if degree(dd) < degree(dv):
		if verbose:
			print(f'El grado del dividendo ({degree(dd)}) es menor que el grado del divisor ({degree(dv)}).')
			print('No se puede realizar la división. El cociente es 0 y el resto es el dividendo original.')
		return [0], dd
	
	q_len = degree(dd) - degree(dv) + 1
	quotient = [0] * q_len
	paso = 1
	
	while degree(dd) >= degree(dv):
		# Verificar que el resto no sea cero
		if all(c == 0 for c in dd):
			break
		
		shift = degree(dd) - degree(dv)
		quotient[shift] = 1
		if verbose:
			print(f'PASO {paso}: Anular x^{degree(dd)}')
			print(f'Resto anterior: {poly_to_str(dd)}')
			mult = ['0'] * shift + dv
			print(f'¿Qué multiplicador necesitamos? Para llegar a x^{degree(dd)} desde x^{degree(dv)} necesitamos: x^{degree(dv)} · x^{shift} = x^{degree(dd)}')
			print(f'El término del cociente es x^{shift}')
			print('Multiplicamos:', poly_to_str(mult))
		poly_xor_shift(dd, dv, shift)
		dd = trim(dd)
		if verbose:
			print('\nRestamos (en módulo 2, restar = sumar):')
			print(poly_to_str(dd))
			if degree(dd) < degree(dv):
				print(f'El grado del resto ({degree(dd)}) es ahora menor que el grado del divisor ({degree(dv)}).')
				print('La división se detiene aquí.')
			print('\n')
		paso += 1
	
	return trim(quotient), trim(dd)


if __name__ == '__main__':
	# Ejemplo pedido
	dividend_str = 'x^8 + x^7 + x^6 + x^5 + x^3 + x^2 + 1'
	divisor_str = 'x^7 + x^6 + x^4 + x^3 + x + 1'

	A = parse_poly(dividend_str)
	G = parse_poly(divisor_str)

	print('DIVISIÓN DE POLINOMIOS EN MÓDULO 2')
	print('Queremos dividir:', dividend_str, '÷ g(x)')
	print('Donde: g(x) =', divisor_str)
	print('\n--- Proceso (verboso) ---\n')
	Q, R = poly_divmod(A, G, verbose=True)

	print('RESULTADO FINAL')
	print('Cociente: h(x) =', poly_to_str(Q))
	print('Resto:', poly_to_str(R))

	# Verificación: g(x) * h(x) == dividend?
	prod = poly_mul(G, Q)
	ok = trim(prod) == trim(A)
	print('\nVerificación: g(x) · h(x) =', poly_to_str(prod), '\n¿Coincide con', poly_to_str(A), '?', '✓' if ok else '✗')
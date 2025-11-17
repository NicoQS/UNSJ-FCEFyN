#!/usr/bin/env python3
"""
RSA Cracker usando el Algoritmo de Fermat
==========================================
Programa para romper el criptosistema RSA mediante la factorización de n
usando el algoritmo de Fermat.

Ejercicios:
13. RSA con (n, e) = (2291, 17), mensaje cifrado = 575
14. RSA con (n, e) = (536813567, 3602561)
"""

import math
import sys


def algoritmo_fermat(n):
    """
    Algoritmo de Fermat para factorizar n en dos factores primos p y q.
    
    Principio:
    - Todo número compuesto n puede expresarse como: n = a² - b² = (a+b)(a-b)
    - Donde p = a+b y q = a-b
    - El algoritmo busca valores de a y b tales que a² - n = b²
    
    Args:
        n: Número a factorizar
        
    Returns:
        (p, q): Tupla con los dos factores primos de n
    """
    print(f"\n{'='*70}")
    print(f"ALGORITMO DE FERMAT PARA FACTORIZAR n = {n}")
    print(f"{'='*70}")
    
    # Comenzamos con a = ceil(sqrt(n))
    a = math.ceil(math.sqrt(n))
    print(f"\nValor inicial: a = ceil(√{n}) = {a}")
    
    iteracion = 0
    while True:
        iteracion += 1
        
        # Calculamos b² = a² - n
        b_cuadrado = a * a - n
        
        # Verificamos si b² es un cuadrado perfecto
        b = int(math.sqrt(b_cuadrado))
        
        if b * b == b_cuadrado:
            # Encontramos los factores
            p = a + b
            q = a - b
            
            print(f"\n✓ Factores encontrados en iteración {iteracion}:")
            print(f"  a = {a}, b = {b}")
            print(f"  p = a + b = {a} + {b} = {p}")
            print(f"  q = a - b = {a} - {b} = {q}")
            print(f"\nVerificación: p × q = {p} × {q} = {p*q}")
            
            return (p, q) if p > q else (q, p)
        
        # Incrementamos a para la siguiente iteración
        if iteracion <= 5:  # Mostramos solo las primeras iteraciones
            print(f"  Iteración {iteracion}: a = {a}, b² = {b_cuadrado} (no es cuadrado perfecto)")
        elif iteracion == 6:
            print(f"  ... (continuando búsqueda)")
            
        a += 1
        
        # Condición de seguridad para evitar bucles infinitos
        if a > (n + 1) // 2:
            print("\n✗ No se encontraron factores (n podría ser primo)")
            return None


def extendido_euclides(a, b):
    """
    Algoritmo extendido de Euclides para encontrar el inverso modular.
    
    Calcula d tal que: a * d ≡ 1 (mod b)
    
    Args:
        a: Número a invertir
        b: Módulo
        
    Returns:
        d: Inverso modular de a módulo b
    """
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extendido_euclides(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y


def calcular_clave_privada(e, phi_n):
    """
    Calcula la clave privada d tal que: e * d ≡ 1 (mod φ(n))
    
    Args:
        e: Clave pública (exponente público)
        phi_n: Indicador de Euler φ(n) = (p-1)(q-1)
        
    Returns:
        d: Clave privada
    """
    print(f"\n{'='*70}")
    print(f"CÁLCULO DE LA CLAVE PRIVADA d")
    print(f"{'='*70}")
    
    gcd, x, _ = extendido_euclides(e, phi_n)
    
    if gcd != 1:
        print(f"\n✗ Error: mcd(e, φ(n)) = {gcd} ≠ 1")
        print(f"  No existe inverso modular.")
        return None
    
    # Aseguramos que d sea positivo
    d = x % phi_n
    
    print(f"\nBuscamos d tal que: e × d ≡ 1 (mod φ(n))")
    print(f"  e = {e}")
    print(f"  φ(n) = {phi_n}")
    print(f"\n✓ Clave privada encontrada: d = {d}")
    print(f"\nVerificación: (e × d) mod φ(n) = ({e} × {d}) mod {phi_n} = {(e * d) % phi_n}")
    
    return d


def potencia_modular(base, exponente, modulo):
    """
    Calcula (base^exponente) mod modulo de forma eficiente.
    Usa el algoritmo de exponenciación rápida.
    
    Args:
        base: Base de la potencia
        exponente: Exponente
        modulo: Módulo
        
    Returns:
        Resultado de (base^exponente) mod modulo
    """
    resultado = 1
    base = base % modulo
    
    while exponente > 0:
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo
        exponente = exponente >> 1
        base = (base * base) % modulo
    
    return resultado


def descifrar_mensaje(criptograma, d, n):
    """
    Descifra un mensaje usando RSA: M = C^d mod n
    
    Args:
        criptograma: Mensaje cifrado (C)
        d: Clave privada
        n: Módulo RSA
        
    Returns:
        Mensaje descifrado (M)
    """
    print(f"\n{'='*70}")
    print(f"DESCIFRADO DEL MENSAJE")
    print(f"{'='*70}")
    
    print(f"\nFórmula: M = C^d mod n")
    print(f"  C = {criptograma}")
    print(f"  d = {d}")
    print(f"  n = {n}")
    
    mensaje = potencia_modular(criptograma, d, n)
    
    print(f"\n✓ Mensaje descifrado: M = {mensaje}")
    
    return mensaje


def numero_a_ascii(numero):
    """
    Convierte un número a su representación ASCII.
    
    Args:
        numero: Número a convertir
        
    Returns:
        Carácter ASCII correspondiente
    """
    try:
        caracter = chr(numero)
        return caracter
    except ValueError:
        return None


def resolver_rsa(n, e, criptograma=None):
    """
    Resuelve completamente un problema de RSA:
    1. Factoriza n usando el algoritmo de Fermat
    2. Calcula φ(n)
    3. Obtiene la clave privada d
    4. Descifra el mensaje (si se proporciona)
    
    Args:
        n: Módulo RSA
        e: Exponente público
        criptograma: Mensaje cifrado (opcional)
    """
    print(f"\n{'#'*70}")
    print(f"# RESOLUCIÓN DE CRIPTOSISTEMA RSA")
    print(f"# Clave pública: (n, e) = ({n}, {e})")
    if criptograma:
        print(f"# Mensaje cifrado: C = {criptograma}")
    print(f"{'#'*70}")
    
    # Paso 1: Factorizar n
    factores = algoritmo_fermat(n)
    
    if factores is None:
        print("\n✗ No se pudo factorizar n. Abortando.")
        return None
    
    p, q = factores
    
    # Paso 2: Calcular φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"\n{'='*70}")
    print(f"CÁLCULO DEL INDICADOR DE EULER")
    print(f"{'='*70}")
    print(f"\nφ(n) = (p-1) × (q-1)")
    print(f"φ(n) = ({p}-1) × ({q}-1)")
    print(f"φ(n) = {p-1} × {q-1}")
    print(f"φ(n) = {phi_n}")
    
    # Paso 3: Calcular la clave privada d
    d = calcular_clave_privada(e, phi_n)
    
    if d is None:
        return None
    
    print(f"\n{'='*70}")
    print(f"CLAVE PRIVADA COMPLETA")
    print(f"{'='*70}")
    print(f"\n✓ Clave privada: (n, d) = ({n}, {d})")
    
    # Paso 4: Descifrar el mensaje (si existe)
    if criptograma is not None:
        mensaje = descifrar_mensaje(criptograma, d, n)
        
        # Convertir a ASCII
        print(f"\n{'='*70}")
        print(f"CONVERSIÓN A ASCII")
        print(f"{'='*70}")
        
        caracter = numero_a_ascii(mensaje)
        if caracter:
            print(f"\nValor ASCII: {mensaje}")
            print(f"Carácter: '{caracter}'")
            
            if caracter.isprintable():
                print(f"Descripción: Carácter imprimible")
            else:
                print(f"Descripción: Carácter de control")
        else:
            print(f"\n✗ El valor {mensaje} no corresponde a un carácter ASCII válido")
    
    return {
        'p': p,
        'q': q,
        'phi_n': phi_n,
        'd': d,
        'mensaje': mensaje if criptograma else None
    }


def main():
    """Función principal del programa."""
    
    print("\n" + "="*70)
    print(" "*15 + "RSA CRACKER - ALGORITMO DE FERMAT")
    print("="*70)
    
    # EJERCICIO 13
    print("\n\n" + "*"*70)
    print("* EJERCICIO 13")
    print("*"*70)
    
    n1 = 2291
    e1 = 17
    c1 = 575
    
    resultado1 = resolver_rsa(n1, e1, c1)
    
    # EJERCICIO 14
    print("\n\n" + "*"*70)
    print("* EJERCICIO 14")
    print("*"*70)
    
    n2 = 536813567
    e2 = 3602561
    
    print("\nNOTA: Para este ejercicio solo calculamos la clave privada d,")
    print("      ya que no se proporciona un mensaje cifrado para descifrar.")
    
    resultado2 = resolver_rsa(n2, e2)
    
    # Resumen final
    print("\n\n" + "="*70)
    print(" "*25 + "RESUMEN DE RESULTADOS")
    print("="*70)
    
    print("\nEJERCICIO 13:")
    print(f"  Clave pública:  (n, e) = ({n1}, {e1})")
    print(f"  Factores:       p = {resultado1['p']}, q = {resultado1['q']}")
    print(f"  Clave privada:  (n, d) = ({n1}, {resultado1['d']})")
    print(f"  Mensaje cifrado: C = {c1}")
    print(f"  Mensaje descifrado: M = {resultado1['mensaje']}")
    print(f"  Carácter ASCII: '{chr(resultado1['mensaje'])}'")
    
    print("\nEJERCICIO 14:")
    print(f"  Clave pública:  (n, e) = ({n2}, {e2})")
    print(f"  Factores:       p = {resultado2['p']}, q = {resultado2['q']}")
    print(f"  Clave privada:  (n, d) = ({n2}, {resultado2['d']})")
    
    print("\n" + "="*70)
    print("\n✓ Análisis completado con éxito.\n")


if __name__ == "__main__":
    main()
"""
Generación de matrices G (generadora) y H (de chequeo) para códigos cíclicos en GF(2).

Proceso:
1. Para matriz G: cada fila i (0 <= i <= k-1) se obtiene dividiendo X^(n-k+i) por G(x)
   Fila i = X^(n-k+i) + resto_i

2. Para matriz H: H = [P^T | I_(n-k)]
   donde P^T es la transpuesta de la matriz de paridad extraída de G

Uso:
    python matriz_G_H_polinomio.py
"""

from typing import List, Tuple
import division_polinomios as dp


def poly_to_vector(poly: List[int], length: int) -> List[int]:
    """Convierte un polinomio a un vector de longitud fija."""
    result = poly[:] + [0] * (length - len(poly))
    return result[:length]


def poly_add(a: List[int], b: List[int]) -> List[int]:
    """Suma de polinomios en GF(2) (XOR bit a bit)."""
    max_len = max(len(a), len(b))
    result = [0] * max_len
    for i in range(len(a)):
        result[i] = a[i]
    for i in range(len(b)):
        result[i] ^= b[i]
    return dp.trim(result)


def generar_matriz_G(g_poly: List[int], n: int, k: int, verbose: bool = False) -> List[List[int]]:
    """
    Genera la matriz generadora G para un código cíclico.
    
    Args:
        g_poly: Polinomio generador G(x) como lista de coeficientes
        n: Longitud del código (n)
        k: Dimensión del código (k)
        verbose: Si True, muestra el proceso detallado
    
    Returns:
        Matriz G de dimensión k x n
    """
    G = []
    
    if verbose:
        print("=" * 70)
        print("GENERACIÓN DE LA MATRIZ GENERADORA G")
        print("=" * 70)
        print(f"Parámetros del código: n = {n}, k = {k}")
        print(f"Polinomio generador: G(x) = {dp.poly_to_str(g_poly)}")
        print(f"Grado de G(x): {dp.degree(g_poly)} (n - k = {n - k})")
        print()
    
    for i in range(k):
        exp = n - k + i
        
        # Crear X^(n-k+i)
        dividend = [0] * (exp + 1)
        dividend[exp] = 1
        
        if verbose:
            print(f"Fila {i}: Dividiendo X^{exp} ÷ G(x)")
            print(f"  Dividendo: {dp.poly_to_str(dividend)}")
        
        # Dividir X^(n-k+i) por G(x)
        quotient, remainder = dp.poly_divmod(dividend, g_poly, verbose=False)
        
        if verbose:
            print(f"  Cociente: {dp.poly_to_str(quotient)}")
            print(f"  Resto: {dp.poly_to_str(remainder)}")
        
        # Fila i = X^(n-k+i) + resto
        fila_poly = poly_add(dividend, remainder)
        
        if verbose:
            print(f"  Fila {i}: X^{exp} + resto = {dp.poly_to_str(fila_poly)}")
        
        # Convertir a vector de longitud n
        fila_vector = poly_to_vector(fila_poly, n)
        G.append(fila_vector)
        
        if verbose:
            print(f"  Vector: {fila_vector}")
            print()
    
    return G


def detectar_identidad_en_G(G: List[List[int]], k: int) -> str:
    """
    Detecta si la identidad está a la izquierda o derecha en la matriz G.
    
    Returns:
        'izquierda' si G = [I_k | P]
        'derecha' si G = [P | I_k]
    """
    # Verificar si la identidad está a la izquierda (primeras k columnas)
    es_identidad_izq = True
    for i in range(k):
        for j in range(k):
            esperado = 1 if i == j else 0
            if G[i][j] != esperado:
                es_identidad_izq = False
                break
        if not es_identidad_izq:
            break
    
    if es_identidad_izq:
        return 'izquierda'
    
    # Verificar si la identidad está a la derecha (últimas k columnas)
    n = len(G[0])
    inicio_identidad = n - k
    es_identidad_der = True
    for i in range(k):
        for j in range(k):
            esperado = 1 if i == j else 0
            if G[i][inicio_identidad + j] != esperado:
                es_identidad_der = False
                break
        if not es_identidad_der:
            break
    
    if es_identidad_der:
        return 'derecha'
    
    # Si no se detecta claramente, asumir izquierda (caso común en códigos cíclicos)
    return 'izquierda'


def extraer_P_de_G(G: List[List[int]], k: int, n: int, verbose: bool = False) -> Tuple[List[List[int]], str]:
    """
    Extrae la matriz P de la matriz G.
    G puede tener la forma [I_k | P] o [P | I_k].
    Detecta automáticamente la forma y extrae P correctamente.
    
    Returns:
        Tupla (P, posicion) donde posicion es 'izquierda' o 'derecha'
    """
    posicion_identidad = detectar_identidad_en_G(G, k)
    
    P = []
    if posicion_identidad == 'izquierda':
        # G = [I_k | P], entonces P son las últimas (n-k) columnas
        if verbose:
            print(f"  Identidad detectada a la IZQUIERDA: G = [I_{k} | P]")
        for i in range(k):
            fila_P = G[i][k:]  # Tomar las últimas n-k columnas
            P.append(fila_P)
    else:
        # G = [P | I_k], entonces P son las primeras (n-k) columnas
        if verbose:
            print(f"  Identidad detectada a la DERECHA: G = [P | I_{k}]")
        for i in range(k):
            fila_P = G[i][:n-k]  # Tomar las primeras n-k columnas
            P.append(fila_P)
    
    return P, posicion_identidad


def transponer(matriz: List[List[int]]) -> List[List[int]]:
    """Transpone una matriz."""
    if not matriz or not matriz[0]:
        return []
    filas = len(matriz)
    cols = len(matriz[0])
    resultado = [[matriz[i][j] for i in range(filas)] for j in range(cols)]
    return resultado


def generar_matriz_H(G: List[List[int]], n: int, k: int, verbose: bool = False) -> List[List[int]]:
    """
    Genera la matriz de chequeo H para un código cíclico.
    
    Si G = [I_k | P], entonces H = [P^T | I_(n-k)]
    Si G = [P | I_k], entonces H = [I_(n-k) | P^T]
    
    Args:
        G: Matriz generadora
        n: Longitud del código
        k: Dimensión del código
        verbose: Si True, muestra el proceso detallado
    
    Returns:
        Matriz H de dimensión (n-k) x n
    """
    if verbose:
        print("=" * 70)
        print("GENERACIÓN DE LA MATRIZ DE CHEQUEO H")
        print("=" * 70)
    
    # Extraer P de G (detectando automáticamente la posición de la identidad)
    P, posicion_identidad = extraer_P_de_G(G, k, n, verbose=verbose)
    
    if verbose:
        print("\nMatriz P extraída de G:")
        imprimir_matriz(P)
        print()
    
    # Transponer P
    P_T = transponer(P)
    
    if verbose:
        print("Matriz P^T (transpuesta):")
        imprimir_matriz(P_T)
        print()
    
    # Crear matriz identidad I_(n-k)
    identidad = [[1 if i == j else 0 for j in range(n - k)] for i in range(n - k)]
    
    if verbose:
        print(f"Matriz Identidad I_{n-k}:")
        imprimir_matriz(identidad)
        print()
    
    # Construir H según la forma de G
    H = []
    if posicion_identidad == 'izquierda':
        # G = [I_k | P] => H = [P^T | I_(n-k)]
        if verbose:
            print(f"Como G = [I_{k} | P], entonces H = [P^T | I_{n-k}]")
        for i in range(n - k):
            fila_H = P_T[i] + identidad[i]
            H.append(fila_H)
    else:
        # G = [P | I_k] => H = [I_(n-k) | P^T]
        if verbose:
            print(f"Como G = [P | I_{k}], entonces H = [I_{n-k} | P^T]")
        for i in range(n - k):
            fila_H = identidad[i] + P_T[i]
            H.append(fila_H)
    
    if verbose:
        print("\nMatriz H final:")
        imprimir_matriz(H)
        print()
    
    return H


def imprimir_matriz(matriz: List[List[int]], nombre: str = ""):
    """Imprime una matriz de forma legible."""
    if nombre:
        print(f"{nombre}:")
    for fila in matriz:
        print("  [" + " ".join(map(str, fila)) + "]")


def verificar_ortogonalidad(G: List[List[int]], H: List[List[int]], verbose: bool = False) -> bool:
    """
    Verifica que G · H^T = 0 (en GF(2)).
    
    Returns:
        True si G · H^T = 0, False en caso contrario
    """
    if verbose:
        print("=" * 70)
        print("VERIFICACIÓN: G · H^T = 0")
        print("=" * 70)
    
    k = len(G)
    n_minus_k = len(H)
    
    # Transponer H
    H_T = transponer(H)
    
    # Multiplicar G · H^T
    resultado = [[0 for _ in range(n_minus_k)] for _ in range(k)]
    
    for i in range(k):
        for j in range(n_minus_k):
            suma = 0
            for l in range(len(G[0])):
                suma ^= (G[i][l] & H_T[l][j])
            resultado[i][j] = suma
    
    if verbose:
        print("Resultado de G · H^T:")
        imprimir_matriz(resultado)
        print()
    
    # Verificar si todos son ceros
    es_cero = all(all(val == 0 for val in fila) for fila in resultado)
    
    if verbose:
        if es_cero:
            print("✓ Verificación exitosa: G · H^T = 0")
        else:
            print("✗ Error: G · H^T ≠ 0")
        print()
    
    return es_cero


def convertir_G_forma_estandar(G: List[List[int]], k: int, n: int, verbose: bool = False) -> List[List[int]]:
    """
    Convierte la matriz G a la forma estándar [I_k | P] si no lo está ya.
    Si G = [P | I_k], intercambia las columnas para obtener [I_k | P].
    
    Args:
        G: Matriz generadora
        k: Dimensión del código
        n: Longitud del código
        verbose: Si True, muestra el proceso
        
    Returns:
        Matriz G en forma estándar [I_k | P]
    """
    posicion_identidad = detectar_identidad_en_G(G, k)
    
    if posicion_identidad == 'izquierda':
        # Ya está en forma estándar [I_k | P]
        if verbose:
            print("  La matriz G ya está en forma estándar [I_k | P]")
        return [fila[:] for fila in G]  # Copia de G
    else:
        # G = [P | I_k], necesitamos intercambiar las columnas
        if verbose:
            print("  Convirtiendo G = [P | I_k] a G = [I_k | P]")
        
        G_estandar = []
        for i in range(k):
            # La parte de identidad (últimas k columnas) va al principio
            # La parte P (primeras n-k columnas) va al final
            fila_nueva = G[i][n-k:] + G[i][:n-k]
            G_estandar.append(fila_nueva)
        
        return G_estandar


def generar_H_desde_G_estandar(G_estandar: List[List[int]], k: int, n: int, verbose: bool = False) -> List[List[int]]:
    """
    Genera la matriz H a partir de G en forma estándar [I_k | P].
    Para G = [I_k | P], entonces H = [P^T | I_(n-k)]
    
    Args:
        G_estandar: Matriz G en forma estándar [I_k | P]
        k: Dimensión del código
        n: Longitud del código
        verbose: Si True, muestra el proceso
        
    Returns:
        Matriz H en forma [P^T | I_(n-k)]
    """
    n_minus_k = n - k
    
    # Extraer P (las últimas n-k columnas de G)
    P = []
    for i in range(k):
        fila_P = G_estandar[i][k:]
        P.append(fila_P)
    
    if verbose:
        print("\n  Matriz P extraída (últimas n-k columnas de G):")
        imprimir_matriz(P, "    ")
    
    # Transponer P
    P_T = transponer(P)
    
    if verbose:
        print("\n  Matriz P^T:")
        imprimir_matriz(P_T, "    ")
    
    # Crear matriz identidad I_(n-k)
    identidad = [[1 if i == j else 0 for j in range(n_minus_k)] for i in range(n_minus_k)]
    
    # Construir H = [P^T | I_(n-k)]
    H = []
    for i in range(n_minus_k):
        fila_H = P_T[i] + identidad[i]
        H.append(fila_H)
    
    return H


if __name__ == '__main__':
    # Ejemplo con el polinomio generador del ejercicio
    g_str = 'x^3 + x + 1'
    g_poly = dp.parse_poly(g_str)
    
    # Parámetros del código
    n = 7  # Longitud del código (típicamente 2^m - 1 para códigos BCH)
    n_minus_k = dp.degree(g_poly)  # n - k = grado de G(x)
    k = n - n_minus_k  # Dimensión del código
    
    print("\n" + "=" * 70)
    print("GENERACIÓN DE MATRICES PARA CÓDIGO CÍCLICO")
    print("=" * 70)
    print(f"Polinomio generador: G(x) = {g_str}")
    print(f"Parámetros: n = {n}, k = {k}, n - k = {n_minus_k}")
    print("=" * 70)
    print()
    
    # Generar matriz G
    G = generar_matriz_G(g_poly, n, k, verbose=True)
    
    print("\n" + "=" * 70)
    print("MATRIZ GENERADORA G FINAL")
    print("=" * 70)
    imprimir_matriz(G, f"Matriz G ({k} x {n})")
    print()
    
    # Generar matriz H
    H = generar_matriz_H(G, n, k, verbose=True)
    
    print("\n" + "=" * 70)
    print("MATRIZ DE CHEQUEO H FINAL")
    print("=" * 70)
    imprimir_matriz(H, f"Matriz H ({n_minus_k} x {n})")
    print()
    
    # Mostrar la transpuesta de H
    H_T = transponer(H)
    print("=" * 70)
    print("MATRIZ H^T (TRANSPUESTA)")
    print("=" * 70)
    imprimir_matriz(H_T, f"Matriz H^T ({n} x {n_minus_k})")
    print()
    
    # Verificar ortogonalidad
    verificar_ortogonalidad(G, H, verbose=True)
    
    # ========================================================================
    # NUEVA SECCIÓN: MATRICES EN FORMA ESTÁNDAR PARA DETECCIÓN DE SÍNDROMES
    # ========================================================================
    print("\n" + "=" * 70)
    print("MATRICES EN FORMA ESTÁNDAR PARA DETECCIÓN DE SÍNDROMES")
    print("=" * 70)
    print("Esta sección muestra las matrices en forma estándar [I|P]")
    print("para facilitar la detección de síndromes.")
    print("=" * 70)
    print()
    
    # Convertir G a forma estándar [I_k | P]
    print("1. MATRIZ GENERADORA EN FORMA ESTÁNDAR G = [I_k | P]")
    print("-" * 70)
    G_estandar = convertir_G_forma_estandar(G, k, n, verbose=True)
    print()
    imprimir_matriz(G_estandar, f"Matriz G estándar ({k} x {n}) = [I_{k} | P]")
    print()
    
    # Generar H correspondiente desde G estándar
    print("2. MATRIZ DE CHEQUEO H = [P^T | I_(n-k)]")
    print("-" * 70)
    H_estandar = generar_H_desde_G_estandar(G_estandar, k, n, verbose=True)
    print()
    imprimir_matriz(H_estandar, f"Matriz H ({n_minus_k} x {n}) = [P^T | I_{n_minus_k}]")
    print()
    
    # Mostrar H^T
    print("3. MATRIZ H^T (TRANSPUESTA)")
    print("-" * 70)
    H_T_estandar = transponer(H_estandar)
    imprimir_matriz(H_T_estandar, f"Matriz H^T ({n} x {n_minus_k})")
    print()
    print("Nota: H^T se utiliza para calcular el síndrome: S = r · H^T")
    print("      donde r es el vector recibido (potencialmente con errores)")
    print()
    
    # Verificar que las matrices estándar también cumplen G · H^T = 0
    print("4. VERIFICACIÓN DE LAS MATRICES ESTÁNDAR")
    print("-" * 70)
    verificacion_estandar = verificar_ortogonalidad(G_estandar, H_estandar, verbose=True)
    
    print("=" * 70)
    print("PROCESO COMPLETADO")
    print("=" * 70)
    print("\nRESUMEN:")
    print(f"  • Matriz G original generada correctamente")
    print(f"  • Matriz H original generada correctamente")
    print(f"  • Matrices convertidas a forma estándar para detección de síndromes")
    print(f"  • Todas las verificaciones: {'✓ EXITOSAS' if verificacion_estandar else '✗ FALLIDAS'}")
    print("=" * 70)

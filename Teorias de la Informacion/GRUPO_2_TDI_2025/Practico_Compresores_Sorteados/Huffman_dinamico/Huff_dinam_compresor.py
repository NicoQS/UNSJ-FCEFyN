"""
Compresor de Huffman Dinámico
==============================
Implementación del algoritmo de compresión de Huffman Adaptativo.
El árbol de Huffman se construye dinámicamente durante la compresión.

Autor: Grupo 2
Fecha: Octubre 2025
"""

import struct
from typing import Dict, Optional, List


class Nodo:
    """
    Representa un nodo en el árbol de Huffman dinámico.
    """
    
    def __init__(self, peso: int = 0, simbolo: Optional[int] = None):
        """
        Inicializa un nodo del árbol.
        
        Args:
            peso: Frecuencia acumulada del nodo
            simbolo: Símbolo ASCII que representa (None para nodos internos)
        """
        self.peso = peso
        self.simbolo = simbolo
        self.padre: Optional[Nodo] = None
        self.izquierda: Optional[Nodo] = None
        self.derecha: Optional[Nodo] = None
        self.orden: int = 0  # Orden de aparición para reordenamiento
    
    def es_hoja(self) -> bool:
        """Verifica si el nodo es una hoja (tiene símbolo)."""
        return self.simbolo is not None


class ArbolHuffmanDinamico:
    """
    Implementa el árbol de Huffman dinámico de forma simplificada y eficiente.
    """
    
    def __init__(self):
        """Inicializa el árbol con un nodo NYT (Not Yet Transmitted)."""
        self.NYT = Nodo(peso=0, simbolo=None)
        self.raiz = self.NYT
        self.nodos: Dict[int, Nodo] = {}  # Mapeo símbolo -> nodo hoja
        self.contador_orden = 0
        self.NYT.orden = self.contador_orden
        self.contador_orden += 1
    
    def obtener_codigo(self, simbolo: int) -> List[int]:
        """
        Obtiene el código binario para un símbolo.
        
        Args:
            simbolo: El símbolo a codificar (valor ASCII)
            
        Returns:
            Lista de bits (0 o 1) que representan el código
        """
        if simbolo in self.nodos:
            # El símbolo ya existe en el árbol
            return self._obtener_camino(self.nodos[simbolo])
        else:
            # Símbolo nuevo: enviar camino a NYT + símbolo en binario
            camino_nyt = self._obtener_camino(self.NYT)
            # Representar el símbolo en 8 bits
            bits_simbolo = [(simbolo >> i) & 1 for i in range(7, -1, -1)]
            return camino_nyt + bits_simbolo
    
    def _obtener_camino(self, nodo: Nodo) -> List[int]:
        """
        Obtiene el camino desde la raíz hasta el nodo.
        
        Args:
            nodo: El nodo destino
            
        Returns:
            Lista de bits (0 para izquierda, 1 para derecha)
        """
        if nodo == self.raiz:
            return []
        
        camino = []
        actual = nodo
        while actual.padre is not None:
            if actual.padre.izquierda == actual:
                camino.append(0)
            else:
                camino.append(1)
            actual = actual.padre
        
        return list(reversed(camino))
    
    def _intercambiar(self, a: Nodo, b: Nodo):
        """
        Intercambia dos nodos en el árbol, asumiendo que b es padre de a.
        
        Args:
            a: Nodo hijo
            b: Nodo padre
        """
        if a.padre != b:
            return  # Solo intercambiar si b es padre de a
        
        # Guardar referencias
        abuelo = b.padre
        es_izquierdo_abuelo = abuelo and abuelo.izquierda == b
        
        # Intercambiar padres
        b.padre = a
        a.padre = abuelo
        
        # Ajustar abuelo
        if abuelo:
            if es_izquierdo_abuelo:
                abuelo.izquierda = a
            else:
                abuelo.derecha = a
        else:
            self.raiz = a
        
        # Intercambiar hijos
        if b.izquierda == a:
            # a era izquierdo de b
            b.izquierda = a.izquierda
            a.izquierda = b
            # a.derecha queda igual
        else:
            # a era derecho de b
            b.derecha = a.derecha
            a.derecha = b
            # a.izquierda queda igual
        
        # Ajustar padres de los hijos movidos
        if b.izquierda:
            b.izquierda.padre = b
        if b.derecha:
            b.derecha.padre = b
        if a.izquierda and a.izquierda != b:
            a.izquierda.padre = a
        if a.derecha and a.derecha != b:
            a.derecha.padre = a
    
    def _reordenar(self, nodo: Nodo):
        """
        Reordena el árbol después de actualizar pesos, intercambiando nodos si es necesario.
        
        Args:
            nodo: Nodo desde donde empezar el reordenamiento
        """
        actual = nodo
        while actual.padre:
            padre = actual.padre
            # Si el peso de actual es mayor que el de padre
            if actual.peso > padre.peso:
                self._intercambiar(actual, padre)
                # Continuar desde el nuevo padre
                actual = padre
            else:
                break
    
    def actualizar(self, simbolo: int):
        """
        Actualiza el árbol después de procesar un símbolo.
        Versión optimizada sin búsquedas exhaustivas.
        
        Args:
            simbolo: El símbolo procesado
        """
        if simbolo in self.nodos:
            # El símbolo ya existe - incrementar pesos en el camino
            nodo = self.nodos[simbolo]
            while nodo is not None:
                nodo.peso += 1
                nodo = nodo.padre
            # self._reordenar(self.nodos[simbolo])
        else:
            # Crear nuevo nodo para el símbolo
            self.contador_orden += 1
            nodo_nuevo = Nodo(peso=1, simbolo=simbolo)
            nodo_nuevo.orden = self.contador_orden
            
            # Crear nuevo nodo interno
            self.contador_orden += 1
            nodo_interno = Nodo(peso=1, simbolo=None)
            nodo_interno.orden = self.contador_orden
            
            # Reorganizar el árbol
            nodo_interno.izquierda = self.NYT
            nodo_interno.derecha = nodo_nuevo
            nodo_interno.padre = self.NYT.padre
            
            if self.NYT.padre:
                if self.NYT.padre.izquierda == self.NYT:
                    self.NYT.padre.izquierda = nodo_interno
                else:
                    self.NYT.padre.derecha = nodo_interno
            else:
                self.raiz = nodo_interno
            
            self.NYT.padre = nodo_interno
            nodo_nuevo.padre = nodo_interno
            
            self.nodos[simbolo] = nodo_nuevo
            
            # Actualizar pesos hacia arriba
            nodo = nodo_interno
            while nodo is not None:
                nodo.peso += 1
                nodo = nodo.padre
            
            # self._reordenar(nodo_interno)


def comprimir_archivo(archivo_entrada: str, archivo_salida: str):
    """
    Comprime un archivo de texto usando Huffman Dinámico.
    
    Args:
        archivo_entrada: Ruta del archivo a comprimir
        archivo_salida: Ruta donde guardar el archivo comprimido
    """
    try:
        # Leer el archivo de entrada en modo binario
        with open(archivo_entrada, 'rb') as f:
            datos = f.read()
        
        if len(datos) == 0:
            print("Advertencia: El archivo está vacío")
            with open(archivo_salida, 'wb') as f:
                f.write(struct.pack('>I', 0))  # Escribir tamaño 0
            return
        
        # Inicializar el árbol de Huffman dinámico
        arbol = ArbolHuffmanDinamico()
        
        # Lista para almacenar todos los bits codificados
        bits_codificados = []
        
        print(f"Comprimiendo {len(datos)} bytes...")
        
        # Procesar cada byte
        for i, byte in enumerate(datos):
            if i % 1000 == 0 and i > 0:
                print(f"  Procesados {i}/{len(datos)} bytes ({i*100//len(datos)}%)...")
            
            # Obtener código para este símbolo
            codigo = arbol.obtener_codigo(byte)
            bits_codificados.extend(codigo)
            
            # Actualizar el árbol
            arbol.actualizar(byte)
        
        # Convertir bits a bytes
        bytes_comprimidos = bits_a_bytes(bits_codificados)
        
        # Escribir archivo comprimido
        with open(archivo_salida, 'wb') as f:
            # Escribir el tamaño original (4 bytes)
            f.write(struct.pack('>I', len(datos)))
            
            # Escribir el número de bits válidos en el último byte (1 byte)
            bits_en_ultimo_byte = len(bits_codificados) % 8
            if bits_en_ultimo_byte == 0:
                bits_en_ultimo_byte = 8
            f.write(struct.pack('B', bits_en_ultimo_byte))
            
            # Escribir los datos comprimidos
            f.write(bytes_comprimidos)
        
        # Estadísticas
        tamaño_original = len(datos)
        tamaño_comprimido = len(bytes_comprimidos) + 5  # +5 por el header
        ratio = (1 - tamaño_comprimido / tamaño_original) * 100 if tamaño_original > 0 else 0
        
        print(f"\n✓ Compresión completada:")
        print(f"  Archivo original: {tamaño_original} bytes")
        print(f"  Archivo comprimido: {tamaño_comprimido} bytes")
        print(f"  Ratio de compresión: {ratio:.2f}%")
        print(f"  Guardado en: {archivo_salida}")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Error durante la compresión: {e}")
        raise


def bits_a_bytes(bits: List[int]) -> bytes:
    """
    Convierte una lista de bits en bytes.
    
    Args:
        bits: Lista de enteros (0 o 1)
        
    Returns:
        bytes: Los bits empaquetados en bytes
    """
    # Rellenar con ceros si es necesario para completar el último byte
    while len(bits) % 8 != 0:
        bits.append(0)
    
    bytes_resultado = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        bytes_resultado.append(byte)
    
    return bytes(bytes_resultado)
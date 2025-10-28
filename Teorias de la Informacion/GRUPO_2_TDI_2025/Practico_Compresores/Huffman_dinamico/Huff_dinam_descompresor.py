"""
Descompresor de Huffman Dinámico
=================================
Implementación del algoritmo de descompresión de Huffman Adaptativo.
El árbol de Huffman se reconstruye dinámicamente durante la descompresión.

Autor: Grupo 2
Fecha: Octubre 2025
"""

import struct
from typing import Optional, List


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
        self.nodos = {}  # Mapeo símbolo -> nodo hoja
        self.contador_orden = 0
        self.NYT.orden = self.contador_orden
        self.contador_orden += 1
    
    def decodificar_simbolo(self, lector_bits) -> Optional[int]:
        """
        Decodifica un símbolo siguiendo el árbol desde la raíz.
        
        Args:
            lector_bits: Objeto LectorBits para leer bits del archivo
            
        Returns:
            El símbolo decodificado o None si se alcanza el final
        """
        nodo_actual = self.raiz
        
        # Navegar por el árbol hasta encontrar una hoja
        while not (nodo_actual.es_hoja() or nodo_actual == self.NYT):
            bit = lector_bits.leer_bit()
            if bit is None:
                return None
            
            if bit == 0:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
        
        # Si llegamos al NYT, leer 8 bits para el nuevo símbolo
        if nodo_actual == self.NYT:
            simbolo = 0
            for _ in range(8):
                bit = lector_bits.leer_bit()
                if bit is None:
                    return None
                simbolo = (simbolo << 1) | bit
            return simbolo
        else:
            return nodo_actual.simbolo
    
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


class LectorBits:
    """
    Lee bits de un flujo de bytes.
    """
    
    def __init__(self, datos: bytes, bits_validos_ultimo_byte: int):
        """
        Inicializa el lector de bits.
        
        Args:
            datos: Los bytes a leer
            bits_validos_ultimo_byte: Número de bits válidos en el último byte
        """
        self.datos = datos
        self.bits_validos_ultimo_byte = bits_validos_ultimo_byte
        self.posicion_byte = 0
        self.posicion_bit = 0
        self.total_bytes = len(datos)
    
    def leer_bit(self) -> Optional[int]:
        """
        Lee un bit del flujo.
        
        Returns:
            0 o 1, o None si se alcanzó el final
        """
        # Verificar si hemos llegado al final
        if self.posicion_byte >= self.total_bytes:
            return None
        
        # Si estamos en el último byte, verificar cuántos bits son válidos
        if self.posicion_byte == self.total_bytes - 1:
            if self.posicion_bit >= self.bits_validos_ultimo_byte:
                return None
        
        # Leer el bit
        byte_actual = self.datos[self.posicion_byte]
        bit = (byte_actual >> (7 - self.posicion_bit)) & 1
        
        # Avanzar a la siguiente posición
        self.posicion_bit += 1
        if self.posicion_bit == 8:
            self.posicion_bit = 0
            self.posicion_byte += 1
        
        return bit


def descomprimir_archivo(archivo_entrada: str, archivo_salida: str):
    """
    Descomprime un archivo creado con el compresor de Huffman Dinámico.
    
    Args:
        archivo_entrada: Ruta del archivo comprimido
        archivo_salida: Ruta donde guardar el archivo descomprimido
    """
    try:
        # Leer el archivo comprimido
        with open(archivo_entrada, 'rb') as f:
            # Leer el header (5 bytes)
            header = f.read(5)
            if len(header) < 5:
                print("Error: Archivo comprimido inválido (header incompleto)")
                return
            
            # Extraer tamaño original (4 bytes)
            tamaño_original = struct.unpack('>I', header[:4])[0]
            
            # Extraer bits válidos en el último byte (1 byte)
            bits_validos_ultimo_byte = struct.unpack('B', header[4:5])[0]
            
            # Leer los datos comprimidos
            datos_comprimidos = f.read()
        
        if tamaño_original == 0:
            # Archivo vacío
            with open(archivo_salida, 'wb') as f:
                pass
            print("✓ Descompresión completada (archivo vacío)")
            return
        
        print(f"Descomprimiendo {len(datos_comprimidos)} bytes...")
        print(f"Tamaño esperado: {tamaño_original} bytes")
        
        # Inicializar el árbol y el lector de bits
        arbol = ArbolHuffmanDinamico()
        lector = LectorBits(datos_comprimidos, bits_validos_ultimo_byte)
        
        # Decodificar los símbolos
        datos_descomprimidos = []
        
        for i in range(tamaño_original):
            if i % 1000 == 0 and i > 0:
                print(f"  Procesados {i}/{tamaño_original} bytes ({i*100//tamaño_original}%)...")
            
            # Decodificar el siguiente símbolo
            simbolo = arbol.decodificar_simbolo(lector)
            
            if simbolo is None:
                print(f"Error: Se alcanzó el final del archivo antes de tiempo (byte {i}/{tamaño_original})")
                break
            
            datos_descomprimidos.append(simbolo)
            
            # Actualizar el árbol
            arbol.actualizar(simbolo)
        
        # Escribir el archivo descomprimido
        with open(archivo_salida, 'wb') as f:
            f.write(bytes(datos_descomprimidos))
        
        print(f"\n✓ Descompresión completada:")
        print(f"  Bytes descomprimidos: {len(datos_descomprimidos)}")
        print(f"  Guardado en: {archivo_salida}")
        
        # Verificar si el tamaño coincide
        if len(datos_descomprimidos) != tamaño_original:
            print(f"  ⚠ Advertencia: El tamaño no coincide (esperado: {tamaño_original}, obtenido: {len(datos_descomprimidos)})")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Error durante la descompresión: {e}")
        raise
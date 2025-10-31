"""
Compresor LZW (Lempel-Ziv-Welch)
=================================
Implementación del algoritmo de compresión LZW.
Construye un diccionario dinámico durante la compresión.

Autor: Grupo 2
Fecha: Octubre 2025
"""

import struct
import os
from typing import Dict, List


class CompresorLZW:
    """
    Implementa el algoritmo de compresión LZW con bits variables (adaptativos).
    Comienza con 9 bits y aumenta dinámicamente según crece el diccionario.
    """
    
    def __init__(self, bits_inicio: int = 9, bits_max: int = 12):
        """
        Inicializa el compresor LZW con bits variables.
        
        Args:
            bits_inicio: Número de bits inicial (por defecto 9 bits = 512 códigos)
            bits_max: Número máximo de bits (por defecto 12 bits = 4096 códigos)
        """
        self.bits_inicio = bits_inicio
        self.bits_max = bits_max
        self.bits_actual = bits_inicio  # Bits actuales (variable)
        self.max_codigo = (1 << bits_max) - 1  # Máximo código posible absoluto
        self.diccionario: Dict[bytes, int] = {}
        self.siguiente_codigo = 0
        self._inicializar_diccionario()
    
    def _inicializar_diccionario(self):
        """
        Inicializa el diccionario con todos los caracteres ASCII (0-255).
        """
        self.diccionario.clear()
        # Inicializar con todos los bytes posibles (0-255)
        for i in range(256):
            self.diccionario[bytes([i])] = i
        self.siguiente_codigo = 256
        self.bits_actual = self.bits_inicio  # Resetear bits a valor inicial
    
    def _obtener_bits_para_codigo(self, codigo: int) -> int:
        """
        Calcula el número de bits necesario para representar un código.
        
        Args:
            codigo: El código a representar
            
        Returns:
            Número de bits necesarios
        """
        if codigo < 512:  # 2^9
            return max(9, self.bits_inicio)
        elif codigo < 1024:  # 2^10
            return max(10, self.bits_inicio)
        elif codigo < 2048:  # 2^11
            return max(11, self.bits_inicio)
        else:  # 2^12 o más
            return self.bits_max
    
    def comprimir(self, datos_entrada: bytes) -> List[tuple]:
        """
        Comprime los datos de entrada usando el algoritmo LZW con bits variables.
        
        Args:
            datos_entrada: Bytes a comprimir
            
        Returns:
            Lista de tuplas (código, bits_usados) para cada código comprimido
        """
        if not datos_entrada:
            return []
        
        # Reiniciar el diccionario
        self._inicializar_diccionario()
        
        codigos_salida = []  # Lista de tuplas (codigo, bits)
        secuencia_actual = bytes([datos_entrada[0]])
        
        for i in range(1, len(datos_entrada)):
            byte_actual = bytes([datos_entrada[i]])
            secuencia_nueva = secuencia_actual + byte_actual
            
            if secuencia_nueva in self.diccionario:
                # La secuencia ya está en el diccionario, continuar
                secuencia_actual = secuencia_nueva
            else:
                # Emitir el código de la secuencia actual con bits variables
                codigo = self.diccionario[secuencia_actual]
                bits_necesarios = self._obtener_bits_para_codigo(codigo)
                codigos_salida.append((codigo, bits_necesarios))
                
                # Agregar la nueva secuencia al diccionario si hay espacio
                if self.siguiente_codigo <= self.max_codigo:
                    self.diccionario[secuencia_nueva] = self.siguiente_codigo
                    self.siguiente_codigo += 1
                    
                    # Actualizar bits_actual si es necesario
                    self.bits_actual = self._obtener_bits_para_codigo(self.siguiente_codigo - 1)
                
                # Comenzar nueva secuencia
                secuencia_actual = byte_actual
        
        # Emitir el código de la última secuencia
        if secuencia_actual:
            codigo = self.diccionario[secuencia_actual]
            bits_necesarios = self._obtener_bits_para_codigo(codigo)
            codigos_salida.append((codigo, bits_necesarios))
        
        return codigos_salida
    
    def _empaquetar_codigos(self, codigos: List[tuple]) -> bytes:
        """
        Empaqueta los códigos en bytes, usando bits variables para cada código.
        
        Args:
            codigos: Lista de tuplas (código, bits_usados) a empaquetar
            
        Returns:
            Bytes empaquetados
        """
        if not codigos:
            return bytes()
        
        # Convertir códigos a una cadena de bits
        bits_totales = []
        for codigo, bits_usados in codigos:
            # Convertir cada código a bits (usando bits_usados bits)
            for i in range(bits_usados - 1, -1, -1):
                bits_totales.append((codigo >> i) & 1)
        
        # Empaquetar bits en bytes
        bytes_resultado = []
        for i in range(0, len(bits_totales), 8):
            byte_actual = 0
            for j in range(8):
                if i + j < len(bits_totales):
                    byte_actual = (byte_actual << 1) | bits_totales[i + j]
                else:
                    byte_actual = byte_actual << 1  # Rellenar con ceros
            bytes_resultado.append(byte_actual)
        
        return bytes(bytes_resultado)


def comprimir_archivo(archivo_entrada: str, archivo_salida: str, bits_inicio: int = 9, bits_max: int = 12):
    """
    Comprime un archivo usando el algoritmo LZW con bits variables.
    
    Args:
        archivo_entrada: Ruta del archivo a comprimir
        archivo_salida: Ruta del archivo comprimido de salida
        bits_inicio: Número de bits inicial (por defecto 9)
        bits_max: Número máximo de bits (por defecto 12)
    """
    print(f"\n{'='*60}")
    print(f"Comprimiendo con LZW (bits variables): {os.path.basename(archivo_entrada)}")
    print(f"{'='*60}")
    
    # Leer el archivo de entrada
    try:
        with open(archivo_entrada, 'rb') as f:
            datos_entrada = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {archivo_entrada}")
    except IOError as e:
        raise IOError(f"Error al leer el archivo: {e}")
    
    tamano_original = len(datos_entrada)
    print(f"Tamaño original: {tamano_original} bytes")
    
    if tamano_original == 0:
        print("⚠ Advertencia: El archivo está vacío")
        # Crear archivo de salida vacío
        with open(archivo_salida, 'wb') as f:
            # Escribir encabezado con tamaño 0
            f.write(struct.pack('>I', 0))  # Tamaño original
            f.write(struct.pack('>H', bits_inicio))  # Bits inicio
            f.write(struct.pack('>H', bits_max))  # Bits máximo
            f.write(struct.pack('>I', 0))  # Número de códigos
        print(f"✓ Archivo comprimido guardado: {archivo_salida}")
        return
    
    # Comprimir
    compresor = CompresorLZW(bits_inicio, bits_max)
    print(f"Configuración: bits inicio={bits_inicio}, bits máx={bits_max}")
    print("Comprimiendo...")
    codigos = compresor.comprimir(datos_entrada)
    
    print(f"Códigos generados: {len(codigos)}")
    print(f"Tamaño del diccionario final: {compresor.siguiente_codigo}")
    
    # Calcular estadísticas de bits usados
    bits_usados = {}
    for _, bits in codigos:
        bits_usados[bits] = bits_usados.get(bits, 0) + 1
    
    print(f"Distribución de bits usados:")
    for bits in sorted(bits_usados.keys()):
        print(f"  {bits} bits: {bits_usados[bits]} códigos")
    
    # Empaquetar códigos en bytes
    datos_comprimidos = compresor._empaquetar_codigos(codigos)
    
    # Escribir archivo de salida con encabezado
    try:
        with open(archivo_salida, 'wb') as f:
            # Encabezado: [tamaño_original (4)] [bits_inicio (2)] [bits_max (2)] [num_codigos (4)]
            f.write(struct.pack('>I', tamano_original))  # Tamaño original (unsigned int)
            f.write(struct.pack('>H', bits_inicio))  # Bits inicio (unsigned short)
            f.write(struct.pack('>H', bits_max))  # Bits máximo (unsigned short)
            f.write(struct.pack('>I', len(codigos)))  # Número de códigos
            f.write(datos_comprimidos)  # Datos comprimidos
    except IOError as e:
        raise IOError(f"Error al escribir el archivo comprimido: {e}")
    
    tamano_comprimido = os.path.getsize(archivo_salida)
    ratio = (1 - tamano_comprimido / tamano_original) * 100 if tamano_original > 0 else 0
    
    print(f"\n{'─'*60}")
    print(f"Tamaño comprimido: {tamano_comprimido} bytes (incluyendo encabezado)")
    print(f"Ratio de compresión: {ratio:.2f}%")
    print(f"✓ Archivo comprimido guardado: {archivo_salida}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Uso: python LZW_compresor.py <archivo_entrada> <archivo_salida> [bits_inicio] [bits_max]")
        print("Ejemplo: python LZW_compresor.py entrada.txt salida.lzw 9 12")
        print("Por defecto: bits_inicio=9, bits_max=12 (bits variables)")
        sys.exit(1)
    
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    bits_inicio = int(sys.argv[3]) if len(sys.argv) > 3 else 9
    bits_max = int(sys.argv[4]) if len(sys.argv) > 4 else 12
    
    try:
        comprimir_archivo(archivo_entrada, archivo_salida, bits_inicio, bits_max)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)

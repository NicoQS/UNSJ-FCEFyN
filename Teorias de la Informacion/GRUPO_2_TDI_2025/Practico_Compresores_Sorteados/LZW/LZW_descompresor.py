"""
Descompresor LZW (Lempel-Ziv-Welch)
====================================
Implementación del algoritmo de descompresión LZW.
Reconstruye el diccionario dinámico durante la descompresión.

Autor: Grupo 2
Fecha: Octubre 2025
"""

import struct
import os
from typing import Dict, List


class DescompresorLZW:
    """
    Implementa el algoritmo de descompresión LZW con bits variables (adaptativos).
    """
    
    def __init__(self, bits_inicio: int = 9, bits_max: int = 12):
        """
        Inicializa el descompresor LZW con bits variables.
        
        Args:
            bits_inicio: Número de bits inicial
            bits_max: Número máximo de bits
        """
        self.bits_inicio = bits_inicio
        self.bits_max = bits_max
        self.bits_actual = bits_inicio
        self.max_codigo = (1 << bits_max) - 1
        self.diccionario: Dict[int, bytes] = {}
        self.siguiente_codigo = 0
        self._inicializar_diccionario()
    
    def _inicializar_diccionario(self):
        """
        Inicializa el diccionario con todos los caracteres ASCII (0-255).
        """
        self.diccionario.clear()
        for i in range(256):
            self.diccionario[i] = bytes([i])
        self.siguiente_codigo = 256
        self.bits_actual = self.bits_inicio
    
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
    
    def descomprimir(self, codigos: List[int]) -> bytes:
        """
        Descomprime una lista de códigos usando el algoritmo LZW con bits variables.
        
        Args:
            codigos: Lista de códigos comprimidos
            
        Returns:
            Bytes descomprimidos
        """
        if not codigos:
            return bytes()
        
        # Reiniciar el diccionario
        self._inicializar_diccionario()
        
        resultado = []
        codigo_anterior = codigos[0]
        
        # Verificar que el primer código sea válido
        if codigo_anterior not in self.diccionario:
            raise ValueError(f"Código inicial inválido: {codigo_anterior}")
        
        secuencia_anterior = self.diccionario[codigo_anterior]
        resultado.append(secuencia_anterior)
        
        for codigo_actual in codigos[1:]:
            if codigo_actual in self.diccionario:
                # El código existe en el diccionario
                secuencia_actual = self.diccionario[codigo_actual]
            elif codigo_actual == self.siguiente_codigo:
                # Caso especial: el código es el siguiente que se va a agregar
                # Esto ocurre cuando la secuencia es de la forma: XYZ...XYZ[X]
                secuencia_actual = secuencia_anterior + bytes([secuencia_anterior[0]])
            else:
                raise ValueError(f"Código inválido durante descompresión: {codigo_actual}")
            
            resultado.append(secuencia_actual)
            
            # Agregar nueva entrada al diccionario
            if self.siguiente_codigo <= self.max_codigo:
                nueva_secuencia = secuencia_anterior + bytes([secuencia_actual[0]])
                self.diccionario[self.siguiente_codigo] = nueva_secuencia
                self.siguiente_codigo += 1
                
                # Actualizar bits_actual
                self.bits_actual = self._obtener_bits_para_codigo(self.siguiente_codigo - 1)
            
            secuencia_anterior = secuencia_actual
        
        return b''.join(resultado)
    
    def _desempaquetar_codigos(self, datos: bytes, num_codigos: int) -> List[int]:
        """
        Desempaqueta bytes en códigos, usando bits variables para cada código.
        
        Args:
            datos: Bytes empaquetados
            num_codigos: Número de códigos a extraer
            
        Returns:
            Lista de códigos desempaquetados
        """
        if not datos or num_codigos == 0:
            return []
        
        # Convertir bytes a cadena de bits
        bits_totales = []
        for byte in datos:
            for i in range(7, -1, -1):
                bits_totales.append((byte >> i) & 1)
        
        # Extraer códigos con bits variables
        codigos = []
        posicion_bit = 0
        codigo_actual_idx = 0  # Para determinar cuántos bits usar
        
        for _ in range(num_codigos):
            # Determinar cuántos bits necesitamos para este código
            # Simulamos el estado del diccionario durante la compresión
            bits_necesarios = self._obtener_bits_para_codigo(codigo_actual_idx)
            
            inicio = posicion_bit
            fin = inicio + bits_necesarios
            
            if fin > len(bits_totales):
                break
            
            # Convertir bits a código
            codigo = 0
            for bit in bits_totales[inicio:fin]:
                codigo = (codigo << 1) | bit
            
            codigos.append(codigo)
            posicion_bit = fin
            
            # Simular el incremento del diccionario
            # (necesitamos saber qué código_actual_idx tendremos para el PRÓXIMO código)
            if codigo_actual_idx >= 256:  # Ya pasamos la inicialización
                codigo_actual_idx += 1
            else:
                # Durante los primeros 256 códigos, pueden ser cualquier byte
                # Después del primer código, empezamos a incrementar
                if len(codigos) > 1:
                    codigo_actual_idx = 256 + len(codigos) - 1
                else:
                    codigo_actual_idx = 256
        
        return codigos


def descomprimir_archivo(archivo_entrada: str, archivo_salida: str):
    """
    Descomprime un archivo comprimido con LZW (bits variables).
    
    Args:
        archivo_entrada: Ruta del archivo comprimido (.lzw)
        archivo_salida: Ruta del archivo descomprimido de salida
    """
    print(f"\n{'='*60}")
    print(f"Descomprimiendo con LZW (bits variables): {os.path.basename(archivo_entrada)}")
    print(f"{'='*60}")
    
    # Leer el archivo comprimido
    try:
        with open(archivo_entrada, 'rb') as f:
            # Leer encabezado
            tamano_original_bytes = f.read(4)
            bits_inicio_bytes = f.read(2)
            bits_max_bytes = f.read(2)
            num_codigos_bytes = f.read(4)
            
            if len(tamano_original_bytes) < 4 or len(bits_inicio_bytes) < 2 or len(bits_max_bytes) < 2 or len(num_codigos_bytes) < 4:
                raise ValueError("Archivo comprimido corrupto o incompleto")
            
            tamano_original = struct.unpack('>I', tamano_original_bytes)[0]
            bits_inicio = struct.unpack('>H', bits_inicio_bytes)[0]
            bits_max = struct.unpack('>H', bits_max_bytes)[0]
            num_codigos = struct.unpack('>I', num_codigos_bytes)[0]
            
            # Leer datos comprimidos
            datos_comprimidos = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {archivo_entrada}")
    except IOError as e:
        raise IOError(f"Error al leer el archivo: {e}")
    
    tamano_comprimido = os.path.getsize(archivo_entrada)
    print(f"Tamaño comprimido: {tamano_comprimido} bytes")
    print(f"Tamaño original esperado: {tamano_original} bytes")
    print(f"Configuración: bits inicio={bits_inicio}, bits máx={bits_max}")
    print(f"Número de códigos: {num_codigos}")
    
    if tamano_original == 0:
        print("⚠ El archivo original estaba vacío")
        # Crear archivo de salida vacío
        with open(archivo_salida, 'wb') as f:
            pass
        print(f"✓ Archivo descomprimido guardado: {archivo_salida}")
        return
    
    # Desempaquetar códigos
    descompresor = DescompresorLZW(bits_inicio, bits_max)
    print("Desempaquetando códigos...")
    codigos = descompresor._desempaquetar_codigos(datos_comprimidos, num_codigos)
    
    print(f"Códigos extraídos: {len(codigos)}")
    
    # Descomprimir
    print("Descomprimiendo...")
    datos_descomprimidos = descompresor.descomprimir(codigos)
    
    print(f"Tamaño del diccionario final: {descompresor.siguiente_codigo}")
    
    # Verificar tamaño
    if len(datos_descomprimidos) != tamano_original:
        print(f"⚠ Advertencia: El tamaño descomprimido ({len(datos_descomprimidos)} bytes) "
              f"no coincide con el esperado ({tamano_original} bytes)")
    
    # Escribir archivo de salida
    try:
        with open(archivo_salida, 'wb') as f:
            f.write(datos_descomprimidos)
    except IOError as e:
        raise IOError(f"Error al escribir el archivo descomprimido: {e}")
    
    print(f"\n{'─'*60}")
    print(f"Tamaño descomprimido: {len(datos_descomprimidos)} bytes")
    print(f"✓ Archivo descomprimido guardado: {archivo_salida}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Uso: python LZW_descompresor.py <archivo_entrada> <archivo_salida>")
        print("Ejemplo: python LZW_descompresor.py salida.lzw descomprimido.txt")
        sys.exit(1)
    
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    
    try:
        descomprimir_archivo(archivo_entrada, archivo_salida)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)

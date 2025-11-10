"""
===============================================================================
COMPRESOR Y DESCOMPRESOR LZW + HUFFMAN ADAPTATIVO
===============================================================================

Este módulo proporciona el menú principal para interactuar con el sistema de
compresión y descompresión de archivos utilizando una combinación de dos
algoritmos:
    1. LZW (Lempel-Ziv-Welch): Compresión basada en diccionarios
    2. Huffman Adaptativo (FGK/NYT): Compresión estadística con árbol dinámico

Autor: Grupo 2 - Teorías de la Información 2025
Fecha: Noviembre 2025
===============================================================================
"""

import os

# Importación de las funciones principales de compresión y descompresión
from compresor import compress
from descompresor import decompress


def verify_files_identical(file1, file2):
    """
    Verifica si dos archivos son idénticos a nivel de bytes.
    
    Esta función lee ambos archivos en modo binario y compara su contenido
    byte por byte para determinar si son exactamente iguales.
    
    Args:
        file1 (str): Ruta al primer archivo
        file2 (str): Ruta al segundo archivo
    
    Returns:
        bool: True si los archivos son idénticos, False en caso contrario
    
    Raises:
        FileNotFoundError: Si alguno de los archivos no existe
        IOError: Si hay problemas al leer los archivos
    """
    try:
        # Leer el contenido completo de ambos archivos en modo binario
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()
        
        # Comparación directa de los contenidos
        return content1 == content2
    except Exception as e:
        print(f"Error al verificar archivos: {e}")
        return False


def compress_decompress_verify(input_file):
    """
    Realiza el ciclo completo de compresión, descompresión y verificación.
    
    Esta función ejecuta todo el proceso:
    1. Comprime el archivo original
    2. Descomprime el archivo comprimido
    3. Verifica que el archivo descomprimido sea idéntico al original
    
    Args:
        input_file (str): Ruta al archivo de entrada a procesar
    
    Returns:
        None
    
    Proceso:
        - Genera archivos temporales con sufijos .comp y _verificacion.txt
        - Calcula y muestra métricas de compresión
        - Realiza verificación byte a byte del resultado
    """
    # Validar que el archivo de entrada existe
    if not os.path.exists(input_file):
        print("Error: El archivo no existe.")
        return
    
    # Generar nombres de archivos para el proceso
    base_name = input_file.rsplit('.', 1)[0]
    compressed_file = base_name + '.comp'
    decompressed_file = base_name + '_verificacion.txt'
    
    try:
        print("\n" + "="*70)
        print("INICIANDO PROCESO DE COMPRESIÓN, DESCOMPRESIÓN Y VERIFICACIÓN")
        print("="*70)
        
        # ============================================================
        # FASE 1: COMPRESIÓN
        # ============================================================
        print("\n--- FASE 1: COMPRESIÓN ---")
        original_size = os.path.getsize(input_file)
        print(f"Archivo original: {input_file}")
        print(f"Tamaño original: {original_size} bytes")
        
        # Llamar a la función de compresión
        final_size = compress(input_file, compressed_file)
        
        # Calcular métricas de compresión
        compression_ratio = (1 - final_size / original_size) * 100 if original_size > 0 else 0.0
        print(f"\n✓ Compresión completada exitosamente")
        print(f"  Archivo comprimido: {compressed_file}")
        print(f"  Tamaño comprimido: {final_size} bytes")
        print(f"  Ratio de compresión: {compression_ratio:.2f}%")
        
        # ============================================================
        # FASE 2: DESCOMPRESIÓN
        # ============================================================
        print("\n--- FASE 2: DESCOMPRESIÓN ---")
        print(f"Descomprimiendo: {compressed_file}")
        
        # Llamar a la función de descompresión
        decompress(compressed_file, decompressed_file)
        
        decompressed_size = os.path.getsize(decompressed_file)
        print(f"\n✓ Descompresión completada exitosamente")
        print(f"  Archivo descomprimido: {decompressed_file}")
        print(f"  Tamaño descomprimido: {decompressed_size} bytes")
        
        # ============================================================
        # FASE 3: VERIFICACIÓN A NIVEL DE BYTES
        # ============================================================
        print("\n--- FASE 3: VERIFICACIÓN ---")
        print("Comparando archivos byte por byte...")
        
        # Verificar si los archivos son idénticos
        if verify_files_identical(input_file, decompressed_file):
            print("\n" + "="*70)
            print("✓✓✓ VERIFICACIÓN EXITOSA ✓✓✓")
            print("="*70)
            print("El archivo descomprimido es IDÉNTICO al archivo original")
            print("La integridad de los datos ha sido preservada al 100%")
            print("="*70)
        else:
            print("\n" + "="*70)
            print("✗✗✗ ERROR EN LA VERIFICACIÓN ✗✗✗")
            print("="*70)
            print("El archivo descomprimido NO coincide con el original")
            print("Puede haber un problema en el algoritmo de compresión/descompresión")
            print("="*70)
        
        # ============================================================
        # RESUMEN FINAL
        # ============================================================
        print("\n--- RESUMEN ---")
        print(f"Tamaño original:      {original_size:>10} bytes")
        print(f"Tamaño comprimido:    {final_size:>10} bytes")
        print(f"Tamaño descomprimido: {decompressed_size:>10} bytes")
        print(f"Reducción lograda:    {compression_ratio:>10.2f}%")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error durante el proceso: {e}")
        import traceback
        traceback.print_exc()


def main_menu():
    """
    Menú principal para compresión y descompresión de archivos.
    
    Proporciona una interfaz de línea de comandos interactiva con las
    siguientes opciones:
        1. Comprimir un archivo de texto
        2. Descomprimir un archivo comprimido
        3. Comprimir, descomprimir y verificar integridad
        4. Salir del programa
    
    El menú se ejecuta en un bucle infinito hasta que el usuario
    selecciona la opción de salir.
    """
    while True:
        # Mostrar el menú principal
        print("\n" + "="*70)
        print("    COMPRESOR LZW + HUFFMAN DINÁMICO NYT")
        print("="*70)
        print("1. Comprimir archivo de texto")
        print("2. Descomprimir archivo")
        print("3. Comprimir, descomprimir y verificar integridad (completo)")
        print("4. Salir")
        print("="*70)
        
        # Solicitar opción al usuario
        choice = input("Seleccione una opción (1-4): ").strip()

        # ============================================================
        # OPCIÓN 1: COMPRIMIR ARCHIVO
        # ============================================================
        if choice == '1':
            print("\n--- COMPRIMIR ARCHIVO ---")
            input_file = input("Ingrese la ruta del archivo a comprimir (.txt): ").strip()
            
            # Validar existencia del archivo
            if not os.path.exists(input_file):
                print("✗ Error: El archivo no existe.")
                continue
            
            # Generar nombre del archivo de salida
            output_file = input_file.rsplit('.', 1)[0] + '.comp'
            
            try:
                # Obtener tamaño original
                original_size = os.path.getsize(input_file)
                
                # Ejecutar compresión
                final_size = compress(input_file, output_file)
                
                # Calcular y mostrar estadísticas
                compression_ratio = (1 - final_size / original_size) * 100 if original_size > 0 else 0.0
                print(f"\n✓ Compresión exitosa")
                print(f"  Archivo original: {input_file}")
                print(f"  Archivo comprimido: {output_file}")
                print(f"  Tamaño original: {original_size} bytes")
                print(f"  Tamaño comprimido: {final_size} bytes")
                print(f"  Reducción: {compression_ratio:.2f}%")
                
            except Exception as e:
                print(f"✗ Error en compresión: {e}")

        # ============================================================
        # OPCIÓN 2: DESCOMPRIMIR ARCHIVO
        # ============================================================
        elif choice == '2':
            print("\n--- DESCOMPRIMIR ARCHIVO ---")
            input_file = input("Ingrese la ruta del archivo comprimido (.comp): ").strip()
            
            # Validar existencia del archivo
            if not os.path.exists(input_file):
                print("✗ Error: El archivo no existe.")
                continue
            
            # Generar nombre del archivo de salida
            output_file = input_file.rsplit('.', 1)[0] + '_descomprimido.txt'
            
            try:
                # Obtener tamaño del archivo comprimido
                compressed_size = os.path.getsize(input_file)
                
                # Ejecutar descompresión
                decompress(input_file, output_file)
                
                # Obtener tamaño del archivo descomprimido
                decompressed_size = os.path.getsize(output_file)
                
                print(f"\n✓ Descompresión exitosa")
                print(f"  Archivo comprimido: {input_file}")
                print(f"  Archivo descomprimido: {output_file}")
                print(f"  Tamaño comprimido: {compressed_size} bytes")
                print(f"  Tamaño descomprimido: {decompressed_size} bytes")
                
            except Exception as e:
                print(f"✗ Error en descompresión: {e}")

        # ============================================================
        # OPCIÓN 3: PROCESO COMPLETO CON VERIFICACIÓN
        # ============================================================
        elif choice == '3':
            print("\n--- PROCESO COMPLETO: COMPRIMIR, DESCOMPRIMIR Y VERIFICAR ---")
            input_file = input("Ingrese la ruta del archivo a procesar (.txt): ").strip()
            
            # Ejecutar el proceso completo
            compress_decompress_verify(input_file)

        # ============================================================
        # OPCIÓN 4: SALIR
        # ============================================================
        elif choice == '4':
            print("\n" + "="*70)
            print("SALIENDO DEL PROGRAMA. FINALIZADO.")
            print("="*70 + "\n")
            break
        
        # ============================================================
        # OPCIÓN INVÁLIDA
        # ============================================================
        else:
            print("\n✗ Opción inválida. Por favor, seleccione una opción del 1 al 4.")


# Punto de entrada del programa
if __name__ == "__main__":
    main_menu()

"""
Programa Principal - Compresor/Descompresor LZW
================================================
Interfaz unificada para comprimir y descomprimir archivos usando
el algoritmo LZW (Lempel-Ziv-Welch).

Autor: Grupo 2
Fecha: Octubre 2025
"""

import os
import sys
from LZW_compresor import comprimir_archivo
from LZW_descompresor import descomprimir_archivo


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("   COMPRESOR/DESCOMPRESOR LZW")
    print("="*60)
    print("\nOpciones:")
    print("  1. Comprimir archivo")
    print("  2. Descomprimir archivo")
    print("  3. Comprimir y descomprimir (prueba completa)")
    print("  4. Salir")
    print("\n" + "="*60)


def obtener_ruta_archivo(mensaje: str, debe_existir: bool = True) -> str:
    """
    Solicita una ruta de archivo al usuario.
    
    Args:
        mensaje: Mensaje a mostrar
        debe_existir: Si True, verifica que el archivo exista
        
    Returns:
        La ruta del archivo o None si se cancela
    """
    while True:
        ruta = input(f"\n{mensaje}: ").strip()
        
        if not ruta:
            print("Error: Debe ingresar una ruta válida")
            continue
        
        if debe_existir and not os.path.exists(ruta):
            print(f"Error: El archivo '{ruta}' no existe")
            continuar = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
            if continuar != 's':
                return None
            continue
        
        return ruta


def obtener_configuracion_bits() -> tuple:
    """
    Solicita la configuración de bits variables al usuario.
    
    Returns:
        Tupla (bits_inicio, bits_max)
    """
    print("\n--- CONFIGURACIÓN DE BITS VARIABLES ---")
    print("Por defecto: inicio=9, máximo=12 (recomendado)")
    usar_default = input("¿Usar configuración por defecto? (s/n): ").strip().lower()
    
    if usar_default == 's':
        return (9, 12)
    
    while True:
        try:
            bits_inicio = int(input("Bits iniciales (9-12, recomendado 9): ").strip() or "9")
            bits_max = int(input("Bits máximos (9-16, recomendado 12): ").strip() or "12")
            
            if 9 <= bits_inicio <= bits_max <= 16:
                return (bits_inicio, bits_max)
            else:
                print("Error: bits_inicio debe ser ≤ bits_max, y ambos entre 9-16")
        except ValueError:
            print("Error: Debe ingresar números válidos")


def opcion_comprimir():
    """Maneja la opción de compresión."""
    print("\n--- COMPRIMIR ARCHIVO ---")
    
    archivo_entrada = obtener_ruta_archivo("Ingrese la ruta del archivo a comprimir", debe_existir=True)
    if not archivo_entrada:
        return
    
    # Sugerir nombre de salida
    nombre_base = os.path.splitext(archivo_entrada)[0]
    archivo_salida_sugerido = nombre_base + ".lzw"
    
    print(f"\nArchivo de salida sugerido: {archivo_salida_sugerido}")
    usar_sugerido = input("¿Usar este nombre? (s/n): ").strip().lower()
    
    if usar_sugerido == 's':
        archivo_salida = archivo_salida_sugerido
    else:
        archivo_salida = obtener_ruta_archivo("Ingrese la ruta del archivo comprimido", debe_existir=False)
        if not archivo_salida:
            return
    
    # Obtener configuración de bits
    bits_inicio, bits_max = obtener_configuracion_bits()
    
    print("\nIniciando compresión...")
    try:
        comprimir_archivo(archivo_entrada, archivo_salida, bits_inicio, bits_max)
    except Exception as e:
        print(f"\n✗ Error durante la compresión: {e}")


def opcion_descomprimir():
    """Maneja la opción de descompresión."""
    print("\n--- DESCOMPRIMIR ARCHIVO ---")
    
    archivo_entrada = obtener_ruta_archivo("Ingrese la ruta del archivo comprimido (.lzw)", debe_existir=True)
    if not archivo_entrada:
        return
    
    # Sugerir nombre de salida
    nombre_base = os.path.splitext(archivo_entrada)[0]
    archivo_salida_sugerido = nombre_base + "_descomprimido.txt"
    
    print(f"\nArchivo de salida sugerido: {archivo_salida_sugerido}")
    usar_sugerido = input("¿Usar este nombre? (s/n): ").strip().lower()
    
    if usar_sugerido == 's':
        archivo_salida = archivo_salida_sugerido
    else:
        archivo_salida = obtener_ruta_archivo("Ingrese la ruta del archivo descomprimido", debe_existir=False)
        if not archivo_salida:
            return
    
    print("\nIniciando descompresión...")
    try:
        descomprimir_archivo(archivo_entrada, archivo_salida)
    except Exception as e:
        print(f"\n✗ Error durante la descompresión: {e}")


def opcion_prueba_completa():
    """Realiza una prueba completa: comprime y luego descomprime."""
    print("\n--- PRUEBA COMPLETA: COMPRIMIR Y DESCOMPRIMIR ---")
    
    archivo_original = obtener_ruta_archivo("Ingrese la ruta del archivo original", debe_existir=True)
    if not archivo_original:
        return
    
    # Generar nombres automáticos
    nombre_base = os.path.splitext(archivo_original)[0]
    archivo_comprimido = nombre_base + "_temp.lzw"
    archivo_descomprimido = nombre_base + "_verificacion.txt"
    
    # Obtener configuración de bits
    bits_inicio, bits_max = obtener_configuracion_bits()
    
    print(f"\nArchivo original: {archivo_original}")
    print(f"Archivo comprimido: {archivo_comprimido}")
    print(f"Archivo descomprimido: {archivo_descomprimido}")
    
    try:
        # Paso 1: Comprimir
        print("\n" + "="*60)
        print("PASO 1: COMPRESIÓN")
        print("="*60)
        comprimir_archivo(archivo_original, archivo_comprimido, bits_inicio, bits_max)
        
        # Paso 2: Descomprimir
        print("\n" + "="*60)
        print("PASO 2: DESCOMPRESIÓN")
        print("="*60)
        descomprimir_archivo(archivo_comprimido, archivo_descomprimido)
        
        # Paso 3: Verificar
        print("\n" + "="*60)
        print("PASO 3: VERIFICACIÓN")
        print("="*60)
        
        with open(archivo_original, 'rb') as f:
            datos_original = f.read()
        
        with open(archivo_descomprimido, 'rb') as f:
            datos_descomprimido = f.read()
        
        if datos_original == datos_descomprimido:
            print("✓ ¡ÉXITO! Los archivos son idénticos byte por byte")
            print(f"  Tamaño: {len(datos_original)} bytes")
        else:
            print("✗ ERROR: Los archivos NO son idénticos")
            print(f"  Tamaño original: {len(datos_original)} bytes")
            print(f"  Tamaño descomprimido: {len(datos_descomprimido)} bytes")
            print(f"  Diferencia: {abs(len(datos_original) - len(datos_descomprimido))} bytes")
        
        print("="*60)
        
        # Preguntar si eliminar archivos temporales
        print("\n¿Desea eliminar los archivos temporales generados?")
        print(f"  - {archivo_comprimido}")
        print(f"  - {archivo_descomprimido}")
        eliminar = input("(s/n): ").strip().lower()
        
        if eliminar == 's':
            try:
                if os.path.exists(archivo_comprimido):
                    os.remove(archivo_comprimido)
                    print(f"✓ Eliminado: {archivo_comprimido}")
                if os.path.exists(archivo_descomprimido):
                    os.remove(archivo_descomprimido)
                    print(f"✓ Eliminado: {archivo_descomprimido}")
            except Exception as e:
                print(f"⚠ Advertencia: No se pudieron eliminar los archivos: {e}")
        
    except Exception as e:
        print(f"\n✗ Error durante la prueba: {e}")


def main():
    """Función principal del programa."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            opcion_comprimir()
        elif opcion == '2':
            opcion_descomprimir()
        elif opcion == '3':
            opcion_prueba_completa()
        elif opcion == '4':
            print("\n¡Hasta luego!")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione 1, 2, 3 o 4.")
        
        # Pausa antes de volver al menú
        if opcion in ['1', '2', '3']:
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}")
        sys.exit(1)

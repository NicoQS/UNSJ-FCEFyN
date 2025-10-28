"""
Programa Principal - Compresor/Descompresor de Huffman Dinámico
================================================================
Interfaz unificada para comprimir y descomprimir archivos usando
el algoritmo de Huffman Adaptativo.

Autor: Grupo 2
Fecha: Octubre 2025
"""

import os
import sys
from Huff_dinam_compresor import comprimir_archivo
from Huff_dinam_descompresor import descomprimir_archivo


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("   COMPRESOR/DESCOMPRESOR DE HUFFMAN DINÁMICO")
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
        La ruta del archivo
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


def opcion_comprimir():
    """Maneja la opción de compresión."""
    print("\n--- COMPRIMIR ARCHIVO ---")
    
    archivo_entrada = obtener_ruta_archivo("Ingrese la ruta del archivo a comprimir", debe_existir=True)
    if not archivo_entrada:
        return
    
    # Sugerir nombre de salida
    nombre_base = os.path.splitext(archivo_entrada)[0]
    archivo_salida_sugerido = nombre_base + ".huff"
    
    print(f"\nArchivo de salida sugerido: {archivo_salida_sugerido}")
    usar_sugerido = input("¿Usar este nombre? (s/n): ").strip().lower()
    
    if usar_sugerido == 's':
        archivo_salida = archivo_salida_sugerido
    else:
        archivo_salida = obtener_ruta_archivo("Ingrese la ruta del archivo comprimido", debe_existir=False)
        if not archivo_salida:
            return
    
    print("\nIniciando compresión...")
    try:
        comprimir_archivo(archivo_entrada, archivo_salida)
    except Exception as e:
        print(f"\n✗ Error durante la compresión: {e}")


def opcion_descomprimir():
    """Maneja la opción de descompresión."""
    print("\n--- DESCOMPRIMIR ARCHIVO ---")
    
    archivo_entrada = obtener_ruta_archivo("Ingrese la ruta del archivo comprimido (.huff)", debe_existir=True)
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
    """Maneja la opción de prueba completa (comprimir y descomprimir)."""
    print("\n--- PRUEBA COMPLETA (COMPRIMIR Y DESCOMPRIMIR) ---")
    
    archivo_original = obtener_ruta_archivo("Ingrese la ruta del archivo original", debe_existir=True)
    if not archivo_original:
        return
    
    # Generar nombres de archivo
    nombre_base = os.path.splitext(archivo_original)[0]
    archivo_comprimido = nombre_base + "_temp.huff"
    archivo_descomprimido = nombre_base + "_recuperado.txt"
    
    print(f"\nArchivo original: {archivo_original}")
    print(f"Archivo comprimido (temporal): {archivo_comprimido}")
    print(f"Archivo descomprimido: {archivo_descomprimido}")
    
    continuar = input("\n¿Continuar con la prueba? (s/n): ").strip().lower()
    if continuar != 's':
        return
    
    try:
        # Paso 1: Comprimir
        print("\n" + "="*60)
        print("PASO 1: COMPRESIÓN")
        print("="*60)
        comprimir_archivo(archivo_original, archivo_comprimido)
        
        # Paso 2: Descomprimir
        print("\n" + "="*60)
        print("PASO 2: DESCOMPRESIÓN")
        print("="*60)
        descomprimir_archivo(archivo_comprimido, archivo_descomprimido)
        
        # Paso 3: Verificar
        print("\n" + "="*60)
        print("PASO 3: VERIFICACIÓN")
        print("="*60)
        
        with open(archivo_original, 'rb') as f1:
            datos_originales = f1.read()
        
        with open(archivo_descomprimido, 'rb') as f2:
            datos_descomprimidos = f2.read()
        
        if datos_originales == datos_descomprimidos:
            print("✓ ¡ÉXITO! Los archivos son idénticos byte a byte")
            print(f"  Tamaño: {len(datos_originales)} bytes")
        else:
            print("✗ ERROR: Los archivos NO son idénticos")
            print(f"  Tamaño original: {len(datos_originales)} bytes")
            print(f"  Tamaño descomprimido: {len(datos_descomprimidos)} bytes")
            print(f"  Diferencia: {abs(len(datos_originales) - len(datos_descomprimidos))} bytes")
        
        # Preguntar si desea eliminar el archivo comprimido temporal
        print("\n" + "="*60)
        eliminar = input("\n¿Desea eliminar el archivo comprimido temporal? (s/n): ").strip().lower()
        if eliminar == 's':
            os.remove(archivo_comprimido)
            print(f"✓ Archivo '{archivo_comprimido}' eliminado")
        
    except Exception as e:
        print(f"\n✗ Error durante la prueba: {e}")
        # Limpiar archivos temporales en caso de error
        if os.path.exists(archivo_comprimido):
            os.remove(archivo_comprimido)


def main():
    """Función principal del programa."""
    print("Bienvenido al Compresor/Descompresor de Huffman Dinámico")
    
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
            print("\n✗ Opción inválida. Por favor, seleccione una opción del 1 al 4.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta luego!")
        sys.exit(0)

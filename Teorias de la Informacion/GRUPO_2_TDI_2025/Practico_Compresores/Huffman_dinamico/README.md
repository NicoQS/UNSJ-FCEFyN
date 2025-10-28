# Compresor/Descompresor de Huffman Dinámico

Implementación del algoritmo de compresión y descompresión de **Huffman Adaptativo** en Python.

## Descripción

Este proyecto implementa el algoritmo de Huffman Dinámico, que construye el árbol de codificación de forma adaptativa durante la compresión y descompresión. A diferencia del Huffman estático, no requiere dos pasadas sobre los datos ni almacenar la tabla de frecuencias.

### Características

- ✅ Compresión y descompresión de archivos de texto
- ✅ Reconstrucción idéntica del archivo original (verificación byte a byte)
- ✅ Algoritmo completo con actualización dinámica del árbol
- ✅ Interfaz de línea de comandos amigable
- ✅ Código bien estructurado, comentado y documentado
- ✅ Sin dependencias externas (solo biblioteca estándar de Python)

## Estructura del Proyecto

```
Huffman_dinamico/
├── Huff_dinam_compresor.py    # Módulo de compresión
├── Huff_dinam_descompresor.py # Módulo de descompresión
├── main.py                     # Interfaz principal
├── README.md                   # Este archivo
└── archivos_ej/                # Archivos de ejemplo para pruebas
    ├── prueba.txt
    ├── prueba_2.txt
    └── prueba_3.txt
```

## Requisitos

- **Python 3.7 o superior**
- No se requieren librerías externas

## Instalación

1. Clone o descargue este repositorio
2. Asegúrese de tener Python 3.7+ instalado:
   ```bash
   python --version
   ```

## Uso

### Opción 1: Interfaz Interactiva

Ejecute el programa principal para acceder al menú interactivo:

```bash
python main.py
```

El menú ofrece las siguientes opciones:
1. **Comprimir archivo**: Comprime un archivo de texto
2. **Descomprimir archivo**: Descomprime un archivo .huff
3. **Comprimir y descomprimir (prueba completa)**: Realiza ambas operaciones y verifica la integridad
4. **Salir**

## Formato del Archivo Comprimido

El archivo comprimido (.huff) tiene la siguiente estructura:

```
[Header: 5 bytes]
  - Bytes 0-3: Tamaño del archivo original (entero de 32 bits, big-endian)
  - Byte 4: Número de bits válidos en el último byte (1-8)
[Datos comprimidos]
  - Secuencia de bits codificados según el árbol de Huffman
```

## Algoritmo

### Compresión

1. Inicializar el árbol con un nodo NYT (Not Yet Transmitted)
2. Para cada símbolo en el archivo:
   - Si el símbolo ya existe en el árbol:
     * Obtener su código binario
     * Emitir el código
   - Si es un símbolo nuevo:
     * Emitir el camino al nodo NYT
     * Emitir el símbolo en 8 bits
   - Actualizar el árbol (incrementar pesos y rebalancear)

### Descompresión

1. Inicializar el árbol con un nodo NYT
2. Para cada símbolo a decodificar:
   - Navegar por el árbol siguiendo los bits
   - Si se llega al NYT:
     * Leer los siguientes 8 bits como símbolo nuevo
   - Si se llega a una hoja:
     * Emitir el símbolo de esa hoja
   - Actualizar el árbol de la misma forma que en la compresión

### Actualización del Árbol (Algoritmo)

Después de procesar cada símbolo:
1. Si es un símbolo nuevo, crear nodos hoja e interno
2. Encontrar el nodo con mayor número en el mismo bloque de peso
3. Intercambiar nodos si es necesario (manteniendo la propiedad sibling)
4. Incrementar el peso del nodo
5. Repetir desde el paso 2 para el nodo padre hasta llegar a la raíz

## Ejemplo de Uso Completo

1. Crear un archivo de prueba (por ejemplo, usando uno de los archivos incluidos en `archivos_ej/` o creando uno nuevo).

2. Ejecutar el programa principal:
   ```bash
   python main.py
   ```

3. Seleccionar la opción 1 para comprimir un archivo (ingresar el nombre del archivo de entrada y salida).

4. Seleccionar la opción 2 para descomprimir el archivo comprimido (ingresar el nombre del archivo comprimido y salida).

5. Para verificar la integridad, usar la opción 3: "Comprimir y descomprimir (prueba completa)", que realiza todo el proceso automáticamente y verifica que el archivo recuperado sea idéntico al original.

En PowerShell, para verificar manualmente que dos archivos sean idénticos:
```powershell
Compare-Object (Get-Content archivo1.txt -Raw -Encoding Byte) (Get-Content archivo2.txt -Raw -Encoding Byte)
```
Si no hay salida, los archivos son idénticos.

## Pruebas

El programa incluye una opción de prueba completa que:
1. Comprime el archivo original
2. Descomprime el archivo comprimido
3. Verifica byte a byte que el archivo recuperado sea idéntico al original
4. Muestra estadísticas de compresión

Para ejecutar la prueba:
```bash
python main.py
# Seleccionar opción 3: "Comprimir y descomprimir (prueba completa)"
```

**Archivos de ejemplo incluidos:**
- `archivos_ej/prueba.txt`
- `archivos_ej/prueba_2.txt`
- `archivos_ej/prueba_3.txt`

Puedes usar estos archivos para probar el compresor y descompresor.

## Limitaciones

- El algoritmo funciona mejor con archivos que tienen patrones repetitivos
- Para archivos muy pequeños o muy aleatorios, el tamaño comprimido puede ser mayor que el original
- El archivo comprimido incluye un overhead de 5 bytes (header)

## Notas Técnicas

- **Codificación**: Los símbolos se representan en 8 bits (bytes)
- **Árbol inicial**: Comienza con un solo nodo NYT
- **Números de nodo**: Se asignan de forma decreciente (512, 511, 510, ...)
- **Orden de bits**: Big-endian para enteros, MSB primero para bits individuales

## Autores

- Grupo 2
- Teorías de la Información - 2025

## Licencia

Este proyecto es de uso académico para la materia Teorías de la Información.

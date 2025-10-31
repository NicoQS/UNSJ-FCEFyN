# Compresor/Descompresor LZW

Implementación del algoritmo de compresión **LZW (Lempel-Ziv-Welch)** en Python con **bits variables adaptativos**.

## Descripción

LZW es un algoritmo de compresión sin pérdida que construye un diccionario dinámico durante el proceso de compresión. Es especialmente efectivo para archivos con patrones repetitivos.

### Características

 **Bits variables adaptativos** (9→10→11→12 bits) para mayor tasa de compresión
 Compresión y descompresión completas
 Archivos descomprimidos idénticos al original (verificación byte por byte)
 Optimización automática según tamaño del diccionario
 Manejo de archivos de cualquier tamaño
 Interfaz interactiva amigable
 Código bien documentado y estructurado

### Mejora: Bits Variables

Esta implementación usa **bits variables** en lugar de bits fijos, lo que significa:

- **Inicio**: 9 bits (suficiente para 512 códigos)
- **Crecimiento automático**: Se expande a 10, 11, 12 bits según crece el diccionario
- **Ventaja**: Mejor compresión en archivos pequeños (ahorra ~25% en bits vs. usar 12 bits fijos)
- **Compatibilidad**: El descompresor detecta automáticamente la configuración usada

## Requisitos

- **Python 3.6 o superior**
- Sin dependencias externas (utiliza solo librerías estándar)

## Estructura del Proyecto

```
LZW/
├── LZW_compresor.py       # Módulo de compresión
├── LZW_descompresor.py    # Módulo de descompresión
├── main.py                # Programa principal (interfaz)
├── README.md              # Este archivo
└── archivos_ej/           # Directorio para archivos de prueba
```

## Instalación

No se requiere instalación de paquetes adicionales. Simplemente asegúrate de tener Python 3.6+ instalado.

Para verificar tu versión de Python:

```bash
python --version
```

## Uso

### Modo Interactivo (Recomendado)

Ejecuta el programa principal para acceder al menú interactivo:

```bash
python main.py
```

El menú ofrece las siguientes opciones:

1. **Comprimir archivo**: Comprime un archivo de texto
2. **Descomprimir archivo**: Descomprime un archivo .lzw
3. **Comprimir y descomprimir**: Prueba completa con verificación
4. **Salir**: Cierra el programa

### Modo Línea de Comandos

#### Comprimir

```bash
python LZW_compresor.py <archivo_entrada> <archivo_salida> [bits_inicio] [bits_max]
```

Ejemplo:
```bash
# Usar valores por defecto (9 bits inicio, 12 bits máximo)
python LZW_compresor.py archivo.txt archivo.lzw

# Configuración personalizada
python LZW_compresor.py archivo.txt archivo.lzw 9 12
```

#### Descomprimir

```bash
python LZW_descompresor.py <archivo_comprimido> <archivo_salida>
```

Ejemplo:
```bash
python LZW_descompresor.py archivo.lzw archivo_descomprimido.txt
```

**Nota**: El descompresor lee automáticamente la configuración de bits del encabezado del archivo.

## Algoritmo LZW

### Funcionamiento

1. **Inicialización**: El diccionario comienza con todos los caracteres ASCII (0-255)

2. **Compresión**:
   - Lee el archivo byte por byte
   - Busca la secuencia más larga que existe en el diccionario
   - Emite el código de esa secuencia
   - Agrega la secuencia + próximo byte al diccionario
   - Continúa hasta procesar todo el archivo

3. **Descompresión**:
   - Reconstruye el diccionario dinámicamente
   - Lee código por código
   - Emite la secuencia correspondiente
   - Agrega nuevas entradas al diccionario siguiendo la misma lógica

### Parámetros

- **bits_codigo**: Número de bits para representar cada código (9-16)
  - 9 bits = 512 códigos máximos
  - 12 bits = 4096 códigos máximos (por defecto, buen balance)
  - 16 bits = 65536 códigos máximos (mayor diccionario, mejor para archivos grandes)

### Formato del Archivo Comprimido

El archivo .lzw tiene la siguiente estructura:

```
[Encabezado]
- 4 bytes: Tamaño original (unsigned int, big-endian)
- 2 bytes: Bits por código (unsigned short, big-endian)
- 4 bytes: Número de códigos (unsigned int, big-endian)

[Datos Comprimidos]
- Códigos empaquetados según el número de bits especificado
```

## Ejemplos de Uso

### Ejemplo 1: Comprimir un archivo de texto

```python
# Usando el módulo directamente
from LZW_compresor import comprimir_archivo

comprimir_archivo('entrada.txt', 'salida.lzw', bits_codigo=12)
```

### Ejemplo 2: Descomprimir

```python
from LZW_descompresor import descomprimir_archivo

descomprimir_archivo('salida.lzw', 'recuperado.txt')
```

### Ejemplo 3: Prueba completa

```bash
# 1. Comprimir
python LZW_compresor.py prueba.txt prueba.lzw

# 2. Descomprimir
python LZW_descompresor.py prueba.lzw prueba_recuperado.txt

# 3. Verificar (en PowerShell o CMD)
fc /b prueba.txt prueba_recuperado.txt
```

## Rendimiento

El algoritmo LZW funciona mejor con:

-  Archivos con patrones repetitivos
-  Texto estructurado (código, XML, JSON)
-  Archivos de tamaño mediano a grande

Puede no comprimir bien (o incluso aumentar el tamaño) en:

- ❌ Archivos muy pequeños (overhead del encabezado)
- ❌ Datos aleatorios o ya comprimidos
- ❌ Imágenes o archivos binarios complejos

## Verificación de Integridad

El programa incluye verificación automática en el modo de prueba completa:

1. Comprime el archivo original
2. Descomprime el archivo comprimido
3. Compara byte por byte ambos archivos
4. Reporta si son idénticos

## Estructura del Código

### LZW_compresor.py

- **Clase `CompresorLZW`**: Implementa la lógica de compresión
  - `_inicializar_diccionario()`: Crea el diccionario base
  - `comprimir()`: Algoritmo principal de compresión
  - `_empaquetar_codigos()`: Convierte códigos a bytes

- **Función `comprimir_archivo()`**: Función principal que maneja archivos

### LZW_descompresor.py

- **Clase `DescompresorLZW`**: Implementa la lógica de descompresión
  - `_inicializar_diccionario()`: Crea el diccionario base
  - `descomprimir()`: Algoritmo principal de descompresión
  - `_desempaquetar_codigos()`: Convierte bytes a códigos

- **Función `descomprimir_archivo()`**: Función principal que maneja archivos

### main.py

- Interfaz de usuario interactiva
- Manejo de errores robusto
- Opciones de menú intuitivas

## Manejo de Errores

El programa maneja correctamente:

-  Archivos inexistentes
-  Archivos vacíos
-  Permisos de lectura/escritura
-  Archivos corruptos
-  Códigos inválidos durante descompresión
-  Interrupciones del usuario (Ctrl+C)

## Limitaciones

- El tamaño máximo del diccionario está determinado por `bits_codigo`
- Cuando el diccionario se llena, no se agregan más entradas
- Para archivos muy grandes, considerar usar 14-16 bits

## Autor

**Grupo 2**  
Teorías de la Información  
Octubre 2025
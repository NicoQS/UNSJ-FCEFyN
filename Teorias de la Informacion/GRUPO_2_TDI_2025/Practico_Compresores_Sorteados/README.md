#  Compresor LZW + Huffman Dinámico NYT

##  Descripción General

Este proyecto implementa un **sistema  de compresión y descompresión de archivos de texto** utilizando una combinación de dos potentes algoritmos de compresión que trabajan en secuencia para lograr una reducción óptima del tamaño de los archivos.

###  Arquitectura del Sistema

El sistema utiliza un **pipeline de compresión en dos etapas**:

```
COMPRESIÓN:
┌─────────────┐     ┌─────────────────┐     ┌──────────────────┐     ┌──────────────┐
│  Archivo    │ --> │  Compresión     │ --> │   Compresión     │ --> │  Archivo     │
│  Original   │     │  LZW            │     │   Huffman NYT    │     │  .comp       │
│  (.txt)     │     │  (Diccionario)  │     │   (Adaptativo)   │     │  (Comprimido)│
└─────────────┘     └─────────────────┘     └──────────────────┘     └──────────────┘

DESCOMPRESIÓN:
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐     ┌─────────────┐
│  Archivo     │ --> │  Descompresión   │ --> │  Descompresión  │ --> │  Archivo    │
│  .comp       │     │  Huffman NYT     │     │  LZW            │     │  Original   │
│  (Comprimido)│     │  (Adaptativo)    │     │  (Diccionario)  │     │  (.txt)     │
└──────────────┘     └──────────────────┘     └─────────────────┘     └─────────────┘
```

---

##  Algoritmos Implementados

### 1️ Compresión LZW (Lempel-Ziv-Welch)

**LZW** es un algoritmo de compresión sin pérdida basado en diccionarios que funciona identificando y codificando secuencias repetidas de datos.

####  Funcionamiento:

1. **Inicialización**: El diccionario comienza con 256 entradas (todos los bytes posibles: 0-255)

2. **Procesamiento**: 
   - Lee secuencias de bytes progresivamente más largas
   - Cuando encuentra una secuencia no vista, emite el código de la secuencia anterior
   - Agrega la nueva secuencia al diccionario

3. **Limitación**: El diccionario está limitado a **1024 entradas** (códigos de 12 bits)
   - Esto previene que el diccionario crezca indefinidamente
   - Deja redundancia para que la segunda etapa (Huffman) pueda comprimir más

####  Output de LZW:

El algoritmo LZW genera dos componentes:

- **Diccionario**: Lista de tuplas `(parent_idx, new_byte)` que permite reconstruir el diccionario
- **Códigos**: Secuencia de códigos de 12 bits que representan las secuencias en el diccionario

**Formato de serialización**:
```
┌─────────────────────────────────────────────────┐
│ Tamaño del diccionario (2 bytes)                │
├─────────────────────────────────────────────────┤
│ Entradas del diccionario (3 bytes c/u)          │
│   - parent_idx (2 bytes)                        │
│   - new_byte (1 byte)                           │
├─────────────────────────────────────────────────┤
│ Número de códigos (4 bytes)                     │
├─────────────────────────────────────────────────┤
│ Códigos empaquetados (12 bits c/u)              │
└─────────────────────────────────────────────────┘
```

####  Ventajas:
-  Excelente para textos con patrones repetitivos
-  Compresión rápida y eficiente
-  Genera diccionarios compactos

---

### 2️ Compresión Huffman Adaptativa (FGK/NYT)

**Huffman Adaptativo** es un algoritmo de compresión estadística que construye un árbol de codificación dinámico sin necesidad de conocer las frecuencias de antemano.

####  Funcionamiento:

1. **Inicialización**: El árbol comienza con un solo nodo especial llamado **NYT** (Not Yet Transmitted)

2. **Procesamiento**:
   - Para cada símbolo:
     - Si ya fue visto: emite el camino a su nodo en el árbol
     - Si es nuevo: emite el camino al nodo NYT + el símbolo completo (8 bits)
     - Actualiza el árbol incrementando pesos y reorganizando nodos

3. **Algoritmo FGK** (Faller-Gallager-Knuth):
   - Mantiene la **propiedad sibling**: nodos con pesos similares se agrupan
   - Realiza **swapping** de nodos para mantener el árbol balanceado
   - Garantiza sincronización perfecta entre compresor y descompresor

####  Estructura del Árbol:

```
         [Raíz]
         /    \
     [10]      [5]
     /  \      /  \
   'A'  'B'  NYT  'C'
```

- Los números representan **pesos** (frecuencias acumuladas)
- Las letras representan **símbolos** (bytes)
- **NYT** marca la posición para nuevos símbolos

####  Output de Huffman:

**Formato de compresión**:
```
┌──────────────────────────────────────────┐
│ Tamaño original (4 bytes)                │
├──────────────────────────────────────────┤
│ Bitstream comprimido:                    │
│   Para cada símbolo:                     │
│   - Camino en árbol (bits variables)    │
│   - Si NYT: símbolo completo (8 bits)   │
└──────────────────────────────────────────┘
```

####  Ventajas:
-  Solo requiere **una pasada** sobre los datos (no necesita análisis previo)
-  Se adapta dinámicamente a las estadísticas de los datos
-  Sincronización perfecta entre compresor y descompresor
-  Muy efectivo para comprimir el output de LZW

---

##  Estructura del Proyecto

```
Practico_Compresores_Sorteados/
│
├── main.py                 #  Menú principal e interfaz de usuario
├── compresor.py            #  Implementación de compresión (LZW + Huffman)
├── descompresor.py         #  Implementación de descompresión
├── README.md               #  Este archivo (documentación completa)
│
└── ejemplos/               # Carpeta con archivos de prueba
    ├── prueba.txt          # Archivo de texto de ejemplo
    └── prueba.comp         # Archivo comprimido de ejemplo
```

###  Descripción de Archivos

#### `main.py`
- **Propósito**: Interfaz de usuario con menú interactivo
- **Funcionalidades**:
  - Opción 1: Comprimir archivos
  - Opción 2: Descomprimir archivos
  - Opción 3: Comprimir, descomprimir y verificar integridad
  - Opción 4: Salir

#### `compresor.py`
- **Propósito**: Implementación completa del pipeline de compresión
- **Componentes principales**:
  - `lzw_compress()`: Algoritmo LZW
  - `serialize_lzw_output()`: Serialización del output LZW
  - `AdaptiveHuffman`: Clase del árbol Huffman adaptativo
  - `BitWriter`: Utilidad para escribir datos a nivel de bits
  - `compress()`: Función principal que coordina todo el proceso

#### `descompresor.py`
- **Propósito**: Implementación completa del pipeline de descompresión
- **Componentes principales**:
  - `lzw_decompress()`: Algoritmo LZW inverso
  - `deserialize_lzw_output()`: Deserialización del output LZW
  - `AdaptiveHuffman`: Árbol Huffman adaptativo (sincronizado con compresor)
  - `BitReader`: Utilidad para leer datos a nivel de bits
  - `decompress()`: Función principal que coordina todo el proceso

---

##  Instalación y Requisitos

###  Requisitos del Sistema

- **Python 3.6 o superior**
- **Sistema Operativo**: Windows, Linux, o macOS
- **Librerías**: Solo librerías estándar de Python (no se requieren instalaciones adicionales)

###  Instalación

1. **Clonar o descargar el repositorio**:
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd Practico_Compresores_Sorteados
   ```

2. **Verificar versión de Python**:
   ```bash
   python --version
   ```
   o en algunos sistemas:
   ```bash
   python3 --version
   ```

3. **¡Listo para usar!** No se requiere instalación de dependencias adicionales.

---

##  Uso del Programa

###  Ejecutar el Programa

```bash
python main.py
```

###  Menú Principal

Al ejecutar el programa, verás el siguiente menú:

```
======================================================================
    COMPRESOR LZW + HUFFMAN DINÁMICO NYT
======================================================================
1. Comprimir archivo de texto
2. Descomprimir archivo
3. Comprimir, descomprimir y verificar integridad (completo)
4. Salir
======================================================================
Seleccione una opción (1-4):
```

---

### 1️ Opción 1: Comprimir Archivo

**Pasos**:
1. Seleccionar opción `1`
2. Ingresar la ruta del archivo a comprimir (por ejemplo: `ejemplos/prueba.txt`)
3. El programa genera automáticamente un archivo `.comp` con el mismo nombre

**Ejemplo**:
```
Seleccione una opción (1-4): 1

--- COMPRIMIR ARCHIVO ---
Ingrese la ruta del archivo a comprimir (.txt): ejemplos/prueba.txt

Etapa 1: Leyendo el archivo de entrada...
Tamaño original: 1024 bytes

Etapa 2: Aplicando compresión LZW...
Tamaño después de LZW: 512 bytes
Porcentaje de reducción en LZW: 50.00%

Etapa 3: Aplicando compresión Huffman...
Tamaño final después de Huffman: 384 bytes
Porcentaje de reducción total: 62.50%

✓ Compresión exitosa
  Archivo comprimido: ejemplos/prueba.comp
```

---

### 2️ Opción 2: Descomprimir Archivo

**Pasos**:
1. Seleccionar opción `2`
2. Ingresar la ruta del archivo comprimido (`.comp`)
3. El programa genera un archivo `_descomprimido.txt`

**Ejemplo**:
```
Seleccione una opción (1-4): 2

--- DESCOMPRIMIR ARCHIVO ---
Ingrese la ruta del archivo comprimido (.comp): ejemplos/prueba.comp

✓ Descompresión exitosa
  Archivo descomprimido: ejemplos/prueba_descomprimido.txt
  Tamaño descomprimido: 1024 bytes
```

---

### 3️ Opción 3: Proceso Completo con Verificación 

Esta es la opción **más completa** y **recomendada** para validar el funcionamiento del sistema.

**Pasos**:
1. Seleccionar opción `3`
2. Ingresar la ruta del archivo original
3. El programa ejecuta:
   -  Compresión completa
   -  Descompresión completa
   -  Verificación byte por byte

**Ejemplo**:
```
Seleccione una opción (1-4): 3

--- PROCESO COMPLETO: COMPRIMIR, DESCOMPRIMIR Y VERIFICAR ---
Ingrese la ruta del archivo a procesar (.txt): ejemplos/prueba.txt

======================================================================
INICIANDO PROCESO DE COMPRESIÓN, DESCOMPRESIÓN Y VERIFICACIÓN
======================================================================

--- FASE 1: COMPRESIÓN ---
Archivo original: ejemplos/prueba.txt
Tamaño original: 1024 bytes

Etapa 1: Leyendo el archivo de entrada...
Etapa 2: Aplicando compresión LZW...
Etapa 3: Aplicando compresión Huffman adaptativa...
Etapa 4: Escribiendo el archivo comprimido...

✓ Compresión completada exitosamente
  Archivo comprimido: ejemplos/prueba.comp
  Tamaño comprimido: 384 bytes
  Ratio de compresión: 62.50%

--- FASE 2: DESCOMPRESIÓN ---
Descomprimiendo: ejemplos/prueba.comp

✓ Descompresión completada exitosamente
  Archivo descomprimido: ejemplos/prueba_verificacion.txt
  Tamaño descomprimido: 1024 bytes

--- FASE 3: VERIFICACIÓN ---
Comparando archivos byte por byte...

======================================================================
✓✓✓ VERIFICACIÓN EXITOSA ✓✓✓
======================================================================
El archivo descomprimido es IDÉNTICO al archivo original
La integridad de los datos ha sido preservada al 100%
======================================================================

--- RESUMEN ---
Tamaño original:           1024 bytes
Tamaño comprimido:          384 bytes
Tamaño descomprimido:      1024 bytes
Reducción lograda:         62.50%
======================================================================
```

---

## 🔬 Detalles Técnicos

### 📏 Formato del Archivo Comprimido (.comp)

El archivo `.comp` tiene la siguiente estructura:

```
┌─────────────────────────────────────────────────────────┐
│ ARCHIVO .COMP (COMPRIMIDO)                              │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────┐             │
│  │  HEADER HUFFMAN (4 bytes)              │             │
│  │  - Tamaño del output LZW serializado   │             │
│  └────────────────────────────────────────┘             │
│                                                          │
│  ┌────────────────────────────────────────┐             │
│  │  BITSTREAM HUFFMAN                     │             │
│  │  (tamaño variable, comprimido)         │             │
│  │                                        │             │
│  │  Contiene internamente:                │             │
│  │  ┌──────────────────────────────────┐  │             │
│  │  │ Header diccionario LZW (2 bytes) │  │             │
│  │  ├──────────────────────────────────┤  │             │
│  │  │ Entradas del diccionario         │  │             │
│  │  ├──────────────────────────────────┤  │             │
│  │  │ Número de códigos (4 bytes)      │  │             │
│  │  ├──────────────────────────────────┤  │             │
│  │  │ Códigos LZW (12 bits c/u)        │  │             │
│  │  └──────────────────────────────────┘  │             │
│  └────────────────────────────────────────┘             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

###  Garantía de Integridad

El sistema **garantiza integridad total** de los datos:

 **Compresión sin pérdida**: No se pierde ni se modifica información  
 **Verificación byte por byte**: El archivo descomprimido es idéntico al original  
 **Sincronización perfecta**: Los árboles Huffman del compresor y descompresor se mantienen sincronizados

###  Complejidad Computacional

- **Compresión LZW**: O(n) donde n es el tamaño del archivo
- **Compresión Huffman**: O(n) con overhead de actualización del árbol
- **Memoria**: O(k) donde k es el tamaño del diccionario (limitado a 1024)

---

##  Ejemplos y Casos de Uso

###  Tipos de Archivos Recomendados

El compresor funciona mejor con:

-  **Archivos de texto plano** (.txt)
-  **Documentos con patrones repetitivos**

---

##  Limitaciones y Consideraciones

###  Limitaciones

- El compresor está optimizado para **archivos de texto**
- El diccionario LZW está limitado a **1024 entradas**
- Archivos muy pequeños (< 1KB) pueden no comprimirse significativamente

###  Recomendaciones

1. **Archivos grandes**: El compresor es más efectivo con archivos > 5KB
2. **Textos repetitivos**: Mayor compresión en archivos con patrones repetidos
3. **Backup del original**: Siempre conservar el archivo original antes de comprimir

---

## 👥 Información del Proyecto

**Curso**: Teorías de la Información 2025  
**Grupo**: Grupo 2  
**Institución**: UNSJ - FCEFyN  
**Fecha**: Noviembre 2025

---

## 📜 Licencia

Este proyecto es parte de un trabajo práctico académico para la materia Teorías de la Información.
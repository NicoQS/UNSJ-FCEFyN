# Compilador de Autómatas Finitos Deterministas (AFD) con Coco/R

Este es un compilador completo que permite definir Autómatas Finitos Deterministas usando un lenguaje de alto nivel fácil de usar, y genera una visualización gráfica interactiva en HTML.

## 📋 Requisitos Previos

- **Coco/R para C#**: Descarga de [http://www.ssw.uni-linz.ac.at/Coco/](http://www.ssw.uni-linz.ac.at/Coco/)
- **.NET Framework 4.5+** o **.NET Core 3.1+**
- Compilador de C# (csc.exe o dotnet)

## 📁 Estructura del Proyecto

```
/AutomataCompiler/
│
├── Automata.atg              (Gramática del lenguaje)
├── Parser.frame              (Frame del parser - NO MODIFICAR)
├── Scanner.frame             (Frame del scanner - NO MODIFICAR)
├── AutomataBuilder.cs        (Constructor del autómata)
├── AutomataVisualizador.cs   (Generador de visualización HTML)
├── Program.cs                (Programa principal)
├── build.bat                 (Script de compilación)
│
├── /ejemplos/
│   ├── ejemplo1.aut          (Cadenas con dos ceros consecutivos)
│   ├── ejemplo2.aut          (Números divisibles por 3)
│   └── ejemplo3.aut          (Puerta automática)
│
├── /out/                     (Ejecutable compilado)
│   └── AutomataCompiler.exe
│
├── /htmls_generados/         (Archivos HTML de salida)
│
└── README.md                 (Este archivo)
```

## 🚀 Pasos para Compilar y Ejecutar

### Paso 1: Generar el Scanner y Parser con Coco/R

```bash
# En el directorio del proyecto, ejecuta:
Coco.exe Automata.atg

# Esto generará automáticamente:
# - Scanner.cs
# - Parser.cs
```

**Nota**: El script `build.bat` eliminará automáticamente los archivos `Scanner.cs` y `Parser.cs` antiguos antes de generar nuevos para evitar conflictos.
# - Scanner.cs
# - Parser.cs
```

### Paso 2: Compilar el proyecto completo

#### Opción A: Usando .NET Framework (csc.exe)

```bash
csc /out:out\AutomataCompiler.exe Program.cs Scanner.cs Parser.cs AutomataBuilder.cs AutomataVisualizador.cs
```

#### Opción B: Usando .NET Core/5+

```bash
# Crear archivo de proyecto (si no existe)
dotnet new console -n AutomataCompiler

# Copiar todos los archivos .cs al proyecto

# Compilar
dotnet build

# Ejecutar
dotnet run -- ejemplo1.aut
```

### Paso 3: Ejecutar el compilador

```bash
# Forma 1: Especificando el archivo como argumento
out\AutomataCompiler.exe ejemplo1.aut

# Forma 2: Sin argumentos (el programa pedirá la ruta)
out\AutomataCompiler.exe
```

### Paso 4: Ver el resultado

Después de una compilación exitosa, se generará un archivo HTML en la carpeta `htmls_generados/` con el formato `NombreAutomata_YYYYMMDD_HHMMSS.html`. Ábrelo en cualquier navegador web para ver la visualización interactiva del autómata.

Los archivos HTML se almacenan con timestamp para mantener un historial de las compilaciones y evitar sobrescribir versiones anteriores.

## 📖 Sintaxis del Lenguaje

### Estructura básica

```
AUTOMATA NombreDelAutomata

[ALFABETO: símbolo1, símbolo2, ...]

ESTADOS: estado1, estado2, estado3, ...

INICIAL: estadoInicial

[FINALES: estadoFinal1, estadoFinal2, ...]

TRANSICIONES:
    origen -> destino con 'símbolo'
    origen -> destino con 'a', 'b', 'c'
    ...

FIN
```

### Reglas del Lenguaje

1. **Palabras clave** (case-sensitive):
   - `AUTOMATA` - Declara el inicio del autómata
   - `ALFABETO` - Define explícitamente el alfabeto
   - `ESTADOS` - Lista todos los estados
   - `INICIAL` - Define el estado inicial
   - `FINALES` - (Opcional) Lista los estados de aceptación
   - `TRANSICIONES` - Define las transiciones del autómata
   - `FIN` - Marca el final de la definición

2. **Símbolos**:
   - Entre comillas simples: `'a'`, `'0'`, `'1'`
   - Entre comillas dobles: `"start"`, `"sensor"`
   - Pueden ser letras, números o palabras

3. **Transiciones**:
   - Formato: `origen -> destino con símbolo`
   - Alternativas: `→` en lugar de `->`
   - Alternativas: `mediante` o `usando` en lugar de `con`
   - Múltiples símbolos: `q0 -> q1 con 'a', 'b', 'c'`

4. **Comentarios**:
   - Línea simple: `// comentario`
   - Múltiples líneas: `/* comentario */`

## 💡 Ejemplos de Uso

### Ejemplo 1: Reconocedor de cadenas con dos ceros consecutivos

```
AUTOMATA DoscerosConsecutivos

ESTADOS: q0, q1, q2

INICIAL: q0

FINALES: q2

TRANSICIONES:
    q0 -> q1 con '0'
    q0 -> q0 con '1'
    q1 -> q2 con '0'
    q1 -> q0 con '1'
    q2 -> q2 con '0', '1'

FIN
```

**Acepta**: "00", "100", "0011", "10010"  
**Rechaza**: "0", "1", "01", "101"

### Ejemplo 2: Números binarios divisibles por 3

```
AUTOMATA DivisiblesPor3

ALFABETO: '0', '1'

ESTADOS: S0, S1, S2

INICIAL: S0

FINALES: S0

TRANSICIONES:
    S0 -> S0 con '0'
    S0 -> S1 con '1'
    S1 -> S2 con '0'
    S1 -> S0 con '1'
    S2 -> S1 con '0'
    S2 -> S2 con '1'

FIN
```

### Ejemplo 3: Puerta automática (símbolos tipo cadena)

```
AUTOMATA PuertaAutomatica

ESTADOS: cerrada, abriendo, abierta, cerrando

INICIAL: cerrada

FINALES: cerrada

TRANSICIONES:
    cerrada  → abriendo con "sensor"
    abriendo → abierta  mediante "timeout"
    abierta  → cerrando usando "timeout"
    abierta  → abierta  con "sensor"
    cerrando → abriendo con "sensor"
    cerrando → cerrada  con "timeout"

FIN
```

## 🎨 Visualización Gráfica

El compilador genera un archivo HTML interactivo con:

- **Dibujo del autómata**: Estados y transiciones visualizados gráficamente
- **Código de colores**:
  - 🟢 Verde: Estado inicial
  - 🔴 Rojo (doble círculo): Estados finales
  - ⚫ Negro: Estados normales
- **Tabla de transiciones**: Representación tabular completa
- **Controles interactivos**:
  - Zoom in/out con botones o scroll del mouse
  - Arrastrar para mover el autómata
  - Restablecer vista

## 🛠️ Solución de Problemas

### Error: "Cannot open file..."
- Verifica que el archivo .aut existe
- Verifica la ruta del archivo

### Error en la compilación de Coco/R
- Asegúrate de tener los archivos .frame correctos
- Verifica que Automata.atg no tiene errores de sintaxis

### Error al compilar el código C#
- Verifica que todos los archivos .cs están presentes
- Asegúrate de tener el .NET Framework/Core instalado

## 📝 Notas Adicionales

- Los archivos .frame **NO deben modificarse** ya que son necesarios para que Coco.exe genere correctamente el compilador base
- El lenguaje es case-sensitive para las palabras clave
- Los nombres de estados e identificadores pueden usar letras, números y guiones bajos
- El alfabeto puede ser inferido automáticamente de las transiciones

## 🤝 Contribuciones

Este compilador fue diseñado para ser educativo y fácil de usar. Siéntete libre de extenderlo con nuevas características como:
- Validación de completitud del autómata
- Minimización de autómatas
- Conversión de AFND a AFD
- Simulación interactiva con cadenas de entrada

## 📄 Licencia

Este proyecto utiliza Coco/R que está bajo licencia GPL. El código generado puede usarse libremente según los términos de la excepción de plugin de Coco/R.
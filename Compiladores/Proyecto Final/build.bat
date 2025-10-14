@echo off
echo ========================================
echo   Compilador de Automatas - Build
echo ========================================
echo.

REM Crear carpeta para archivos HTML generados
if not exist htmls_generados (
    mkdir htmls_generados
    echo Carpeta htmls_generados creada
) else (
    echo Carpeta htmls_generados ya existe
)

REM Crear carpeta para el ejecutable de salida
if not exist out (
    mkdir out
    echo Carpeta out creada
) else (
    echo Carpeta out ya existe
)
echo.

REM Limpiar archivos generados anteriormente
echo Eliminando archivos generados anteriormente...
if exist Scanner.cs (
    del Scanner.cs
    echo    Scanner.cs eliminado
)
if exist Parser.cs (
    del Parser.cs
    echo    Parser.cs eliminado
)
echo.

REM Verificar si existe Coco.exe
if not exist Coco.exe (
    echo ERROR: Coco.exe no encontrado en el directorio actual
    echo Por favor, descarga Coco/R desde http://www.ssw.uni-linz.ac.at/Coco/
    pause
    exit /b 1
)

REM Paso 1: Generar Scanner y Parser
echo [1/2] Generando Scanner.cs y Parser.cs con Coco/R...
Coco.exe Automata.atg

if errorlevel 1 (
    echo ERROR: Fallo al generar el scanner y parser
    pause
    exit /b 1
)

if not exist Scanner.cs (
    echo ERROR: Scanner.cs no fue generado
    pause
    exit /b 1
)

if not exist Parser.cs (
    echo ERROR: Parser.cs no fue generado
    pause
    exit /b 1
)

echo    OK - Scanner.cs y Parser.cs generados exitosamente
echo.

REM Paso 2: Compilar con csc.exe
echo [2/2] Compilando AutomataCompiler.exe...
csc /out:out\AutomataCompiler.exe Program.cs Scanner.cs Parser.cs AutomataBuilder.cs AutomataVisualizador.cs SymTab.cs

if errorlevel 1 (
    echo ERROR: Fallo la compilacion
    pause
    exit /b 1
)

goto :success

:success
echo.
echo ========================================
echo   COMPILACION EXITOSA DEL GAF!
echo ========================================
echo.
echo Presiona cualquier tecla para continuar...
pause >nul
echo Se ha generado: out\AutomataCompiler.exe
echo.
pause
exit /b 0
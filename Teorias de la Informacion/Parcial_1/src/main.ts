
import * as readline from 'readline';
import { Source } from './compresion/core/base';
import { Huffman, Fano, Shannon } from './compresion/estaticas/estaticas';
import { ASCII, MinASCII } from './compresion/estaticas/ASCII';
import { Arithmetic } from './compresion/dinamicas/aritmetico';
import { LZ, LZW } from './compresion/dinamicas/LZ';
import { AdaptiveHuffman } from './compresion/dinamicas/huffman';
import { Markov } from './compresion/markov';
import BurrowsWheelerTransform from './compresion/utils/burrowWheeler';
import SucesiveSymbolsEncoding from './compresion/estaticas/sucesiveSymbols';

// Interfaz para configuración de readline
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Función para hacer preguntas de forma promisificada
function question(prompt: string): Promise<string> {
  return new Promise((resolve) => {
    rl.question(prompt, resolve);
  });
}

// Función para limpiar consola
function clearConsole() {
  console.clear();
}

// Función para mostrar el menú principal
function showMainMenu() {
  console.log('\n=== SISTEMA DE COMPRESIÓN DE DATOS ===\n');
  console.log('1. Métodos Estáticos');
  console.log('2. Métodos Dinámicos');
  console.log('3. Cadenas de Markov');
  console.log('4. Transformaciones Auxiliares');
  console.log('5. Comparar Métodos');
  console.log('6. Análisis de Fuente Independiente');
  console.log('0. Salir\n');
}

// Función para mostrar métodos estáticos
function showStaticMethods() {
  console.log('\n=== MÉTODOS ESTÁTICOS ===\n');
  console.log('1. Huffman');
  console.log('2. Fano');
  console.log('3. Shannon');
  console.log('4. ASCII Mínimo');
  console.log('5. ASCII Estándar');
  console.log('6. Codificación por Símbolos Sucesivos (RLE)');
  console.log('0. Volver al menú principal\n');
}

// Función para mostrar métodos dinámicos
function showDynamicMethods() {
  console.log('\n=== MÉTODOS DINÁMICOS ===\n');
  console.log('1. Huffman Adaptativo');
  console.log('2. Aritmético');
  console.log('3. LZ (Lempel-Ziv)');
  console.log('4. LZW (Lempel-Ziv-Welch)');
  console.log('0. Volver al menú principal\n');
}

// Función para mostrar opciones de Markov
function showMarkovMethods() {
  console.log('\n=== CADENAS DE MARKOV ===\n');
  console.log('1. Markov + Huffman');
  console.log('2. Markov + Fano');
  console.log('3. Markov + Shannon');
  console.log('4. Matriz de Transición (Orden 1)');
  console.log('0. Volver al menú principal\n');
}

// Función para mostrar transformaciones auxiliares
function showTransformMethods() {
  console.log('\n=== TRANSFORMACIONES AUXILIARES ===\n');
  console.log('1. Burrows-Wheeler - Codificar');
  console.log('2. Burrows-Wheeler - Decodificar');
  console.log('0. Volver al menú principal\n');
}

// Función para obtener texto del usuario
async function getInputText(): Promise<string> {
  const text = await question('Ingrese el texto a comprimir: ');
  if (text.trim() === '') {
    console.log('⚠️ El texto no puede estar vacío.');
    return await getInputText();
  }
  return text.trim();
}

// Función para obtener parámetros numéricos
async function getNumberInput(prompt: string, min: number = 1, max?: number): Promise<number> {
  const input = await question(prompt);
  const num = parseInt(input);
  
  if (isNaN(num) || num < min || (max !== undefined && num > max)) {
    console.log(`⚠️ Por favor ingrese un número válido entre ${min}${max ? ` y ${max}` : ' o mayor'}.`);
    return await getNumberInput(prompt, min, max);
  }
  
  return num;
}


// Función para mostrar matriz de transición
function showTransitionMatrix(matrix: any, symbols: string[], frequencies: number[][], originalText: string) {
  console.log('\n=== MATRIZ DE TRANSICIÓN ===');
  console.log(`Texto analizado: "${originalText}"`);
  console.log(`Orden de Markov: 1 (cada fila es t, cada columna es t+1)\n`);
  
  // Mostrar matriz de frecuencias
  console.log('📊 MATRIZ DE FRECUENCIAS:');
  console.log('┌─────────┬' + '─'.repeat(symbols.length * 8 + 1) + '┐');
  
  // Encabezado con símbolos de destino (t+1)
  let header = '│  t\\t+1  │';
  symbols.forEach(symbol => {
    const displaySymbol = symbol === ' ' ? 'ESP' : symbol === '\n' ? '\\n' : symbol === '\t' ? '\\t' : symbol;
    header += `   ${displaySymbol.padEnd(3)}  │`;
  });
  console.log(header);
  console.log('├─────────┼' + '─'.repeat(symbols.length * 8 + 1) + '┤');
  
  // Filas con frecuencias
  symbols.forEach((rowSymbol, i) => {
    const displayRowSymbol = rowSymbol === ' ' ? 'ESP' : rowSymbol === '\n' ? '\\n' : rowSymbol === '\t' ? '\\t' : rowSymbol;
    let row = `│    ${displayRowSymbol.padEnd(3)} │`;
    symbols.forEach((_, j) => {
      row += `   ${frequencies[i]![j]!.toString().padStart(3)}  │`;
    });
    console.log(row);
  });
  console.log('└─────────┴' + '─'.repeat(symbols.length * 8 + 1) + '┘');
  
  console.log('\n🎯 MATRIZ DE PROBABILIDADES:');
  console.log('┌─────────┬' + '─'.repeat(symbols.length * 12 + 1) + '┐');
  
  // Encabezado para probabilidades
  header = '│  t\\t+1  │';
  symbols.forEach(symbol => {
    const displaySymbol = symbol === ' ' ? 'ESP' : symbol === '\n' ? '\\n' : symbol === '\t' ? '\\t' : symbol;
    header += `     ${displaySymbol.padEnd(6)}     │`;
  });
  console.log(header);
  console.log('├─────────┼' + '─'.repeat(symbols.length * 12 + 1) + '┤');
  
  // Filas con probabilidades
  symbols.forEach((rowSymbol, i) => {
    const displayRowSymbol = rowSymbol === ' ' ? 'ESP' : rowSymbol === '\n' ? '\\n' : rowSymbol === '\t' ? '\\t' : rowSymbol;
    let row = `│    ${displayRowSymbol.padEnd(3)} │`;
    symbols.forEach((_, j) => {
      const prob = matrix[i]![j]!;
      const probDisplay = prob.valueOf() === 0 ? '0' : 
                         prob.denominator === 1 ? prob.numerator.toString() :
                         `${prob.numerator}/${prob.denominator}`;
      row += `  ${probDisplay.padStart(10)}  │`;
    });
    console.log(row);
  });
  console.log('└─────────┴' + '─'.repeat(symbols.length * 12 + 1) + '┘');
  
  // Mostrar estadísticas adicionales
  console.log('\n📈 ESTADÍSTICAS:');
  console.log(`Total de transiciones analizadas: ${originalText.length - 1}`);
  console.log(`Símbolos únicos encontrados: ${symbols.length}`);
  
  // Mostrar transiciones más frecuentes
  let maxTransitions: Array<{from: string, to: string, count: number}> = [];
  symbols.forEach((fromSymbol, i) => {
    symbols.forEach((toSymbol, j) => {
      const count = frequencies[i]![j]!;
      if (count > 0) {
        maxTransitions.push({ from: fromSymbol, to: toSymbol, count });
      }
    });
  });
  
  maxTransitions.sort((a, b) => b.count - a.count);
  
  if (maxTransitions.length > 0) {
    console.log('\n🔥 TRANSICIONES MÁS FRECUENTES:');
    maxTransitions.slice(0, 5).forEach((trans, index) => {
      const fromDisplay = trans.from === ' ' ? 'ESPACIO' : trans.from === '\n' ? '\\n' : trans.from === '\t' ? '\\t' : trans.from;
      const toDisplay = trans.to === ' ' ? 'ESPACIO' : trans.to === '\n' ? '\\n' : trans.to === '\t' ? '\\t' : trans.to;
      console.log(`${index + 1}. '${fromDisplay}' → '${toDisplay}': ${trans.count} veces`);
    });
  }
}

// Función para mostrar tabla de códigos
function showCodeTable(codes: Record<string, string>, title: string = 'TABLA DE CÓDIGOS') {
  console.log(`\n=== ${title} ===`);
  console.log('┌─────────────┬──────────────────┐');
  console.log('│   Símbolo   │      Código      │');
  console.log('├─────────────┼──────────────────┤');
  
  // Ordenar símbolos para mejor visualización
  const sortedEntries = Object.entries(codes).sort(([a], [b]) => {
    // Primero letras, luego números, luego símbolos especiales
    if (a.match(/[a-zA-Z]/) && !b.match(/[a-zA-Z]/)) return -1;
    if (!a.match(/[a-zA-Z]/) && b.match(/[a-zA-Z]/)) return 1;
    return a.localeCompare(b);
  });
  
  sortedEntries.forEach(([symbol, code]) => {
    const displaySymbol = symbol === ' ' ? 'ESPACIO' : symbol === '\n' ? '\\n' : symbol === '\t' ? '\\t' : symbol;
    console.log(`│     '${displaySymbol.padEnd(3)}'     │  ${code.padEnd(14)}  │`);
  });
  
  console.log('└─────────────┴──────────────────┘');
  console.log(`Total de símbolos: ${Object.keys(codes).length}`);
}

// Función para mostrar información de frecuencias
function showFrequencyTable(source: Source, originalText: string, title: string = 'FRECUENCIAS Y PROBABILIDADES') {
  console.log(`\n=== ${title} ===`);
  console.log('┌─────────────┬─────────────┬──────────────────┐');
  console.log('│   Símbolo   │ Frecuencia  │   Probabilidad   │');
  console.log('├─────────────┼─────────────┼──────────────────┤');
  
  // Ordenar por probabilidad descendente
  const sortedEntries = Object.entries(source.probabilities)
    .sort(([,a], [,b]) => b.subtract(a).valueOf());
  
  const totalLength = originalText.length;
  
  sortedEntries.forEach(([symbol, prob]) => {
    const displaySymbol = symbol === ' ' ? 'ESPACIO' : symbol === '\n' ? '\\n' : symbol === '\t' ? '\\t' : symbol;
    // Calcular frecuencia real sin simplificar
    const count = originalText.split(symbol).length - 1;
    const frequency = `${count}/${totalLength}`;
    const percentage = (prob.valueOf() * 100).toFixed(2) + '%';
    console.log(`│     '${displaySymbol.padEnd(3)}'     │  ${frequency.padEnd(9)}  │  ${percentage.padStart(14)}  │`);
  });
  
  console.log('└─────────────┴─────────────┴──────────────────┘');
  console.log(`Entropía: ${source.entropy().toFraction()} (${source.entropy().valueOf().toFixed(4)} bits)`);
}

// Función para mostrar resultados (versión mejorada)
function showResults(method: string, original: string, encoded: any, decoded?: string, codeTable?: Record<string, string>, source?: Source) {
  console.log('\n' + '='.repeat(60));
  console.log(`=== RESULTADOS - ${method.toUpperCase()} ===`);
  console.log('='.repeat(60));
  
  // Mostrar información básica
  console.log(`\n📝 INFORMACIÓN BÁSICA:`);
  console.log(`Texto original: "${original}"`);
  console.log(`Tamaño original: ${original.length} caracteres (${original.length * 8} bits)`);
  
  // Mostrar tabla de frecuencias si hay source
  if (source) {
    showFrequencyTable(source, original);
  }
  
  // Mostrar tabla de códigos si está disponible
  if (codeTable) {
    showCodeTable(codeTable);
  }
  
  // Mostrar resultados de codificación
  console.log(`\n🔧 RESULTADOS DE CODIFICACIÓN:`);
  if (typeof encoded === 'string') {
    console.log(`Texto codificado: "${encoded}"`);
    console.log(`Tamaño codificado: ${encoded.length} bits`);
    console.log(`Ratio de compresión: ${((original.length * 8) / encoded.length).toFixed(2)}:1`);
    console.log(`Porcentaje de compresión: ${(((original.length * 8 - encoded.length) / (original.length * 8)) * 100).toFixed(2)}%`);
    
    // Mostrar eficiencia por símbolo
    const avgBitsPerSymbol = encoded.length / original.length;
    console.log(`Promedio de bits por símbolo: ${avgBitsPerSymbol.toFixed(6)} bits`);
  } else {
    console.log(`Resultado codificado:`, encoded);
  }
  
  // Mostrar verificación de decodificación
  if (decoded) {
    console.log(`\n✅ VERIFICACIÓN:`);
    console.log(`Texto decodificado: "${decoded}"`);
    console.log(`Estado: ${original === decoded ? '✅ EXITOSA' : '❌ FALLIDA'}`);
    
    if (original !== decoded) {
      console.log(`⚠️ Error de decodificación detectado!`);
    }
  }
  
  console.log('\n' + '='.repeat(60));
}

// Función para manejar métodos estáticos
async function handleStaticMethods() {
  while (true) {
    clearConsole();
    showStaticMethods();
    
    const choice = await question('Seleccione una opción: ');
    
    switch (choice) {
      case '1': // Huffman
        try {
          const text = await getInputText();
          const source = Source.fromString(text);
          const huffman = new Huffman(source);
          const encoded = huffman.encode(text);
          const decoded = huffman.decode(encoded);
          
          
          showResults('Huffman', text, encoded, decoded, huffman.codes, source);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '2': // Fano
        try {
          const text = await getInputText();
          const source = Source.fromString(text);
          const fano = new Fano(source);
          const encoded = fano.encode(text);
          const decoded = fano.decode(encoded);
          
          
          showResults('Fano', text, encoded, decoded, fano.codes, source);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '3': // Shannon
        try {
          const text = await getInputText();
          const source = Source.fromString(text);
          const shannon = new Shannon(source);
          const encoded = shannon.encode(text);
          const decoded = shannon.decode(encoded);
          
          
          showResults('Shannon', text, encoded, decoded, shannon.codes, source);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '4': // ASCII Mínimo
        try {
          const text = await getInputText();
          const minAscii = MinASCII.fromString(text);
          const encoded = minAscii.encode(text);
          const decoded = minAscii.decode(encoded);
          showResults('ASCII Mínimo', text, encoded, decoded, minAscii.codes, minAscii.source);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '5': // ASCII Estándar
        try {
          const text = await getInputText();
          const encoded = ASCII.encode(text);
          const decoded = ASCII.decode(encoded);
          
          // Crear tabla de códigos ASCII para mostrar
          const asciiCodes: Record<string, string> = {};
          for (const char of text) {
            if (!asciiCodes[char]) {
              asciiCodes[char] = char.charCodeAt(0).toString(2).padStart(8, '0');
            }
          }
          
          showResults('ASCII Estándar', text, encoded, decoded, asciiCodes);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '6': // RLE
        try {
          const text = await getInputText();
          const ascii = (str: string) => str.charCodeAt(0);
          const [encoded, charBits, countBits] = SucesiveSymbolsEncoding.encode(text, ascii);
          const decoded = SucesiveSymbolsEncoding.decode(encoded, charBits, countBits);
          console.log('\n=== RESULTADOS RLE ===');
          console.log(`Texto original: "${text}"`);
          console.log(`Texto codificado: "${encoded}"`);
          console.log(`Bits por carácter: ${charBits}`);
          console.log(`Bits por conteo: ${countBits}`);
          console.log(`Texto decodificado: "${decoded}"`);
          console.log(`✅ Decodificación ${text === decoded ? 'exitosa' : 'fallida'}`);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '0':
        return;
        
      default:
        console.log('❌ Opción no válida.');
    }
    
    await question('\nPresione Enter para continuar...');
  }
}

// Función para manejar métodos dinámicos
async function handleDynamicMethods() {
  while (true) {
    clearConsole();
    showDynamicMethods();
    
    const choice = await question('Seleccione una opción: ');
    
    switch (choice) {
      case '1': // Huffman Adaptativo
        try {
          const text = await getInputText();
          const source = Source.fromString(text);
          
          // Preguntar si quiere ver el proceso paso a paso
          const interactive = await question('¿Desea ver el proceso de construcción paso a paso? (s/n): ');
          const isInteractive = interactive.toLowerCase() === 's';
          
          const adaptiveHuffman = new AdaptiveHuffman(undefined, undefined, isInteractive, question);
          
          if (isInteractive) {
            console.log('\n🔄 Iniciando codificación con Huffman Adaptativo (modo paso a paso)...\n');
            console.log('💡 Se mostrará automáticamente cada iteración con una pausa de 1.5 segundos entre pasos.\n');
          } else {
            console.log('\n🔄 Iniciando codificación con Huffman Adaptativo...\n');
          }
          
          let encoded: string;
          if (isInteractive) {
            encoded = await adaptiveHuffman.encode(text);
          } else {
            encoded = adaptiveHuffman.encodeSync(text);
          }
          
          const decoded = adaptiveHuffman.decode(encoded);
          const codes = adaptiveHuffman.getCodes();
          
          if (!isInteractive) {
            showResults('Huffman Adaptativo', text, encoded, decoded, codes, source);
          }
          
          // Opción para mostrar el árbol final
          const showTree = await question('\n¿Desea ver el árbol final de Huffman? (s/n): ');
          if (showTree.toLowerCase() === 's') {
            adaptiveHuffman.printTree();
          }
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '2': // Aritmético
        try {
          const text = await getInputText();
          const source = Source.fromString(text);
          const arithmetic = new Arithmetic(source);
          const encoded = arithmetic.encode(text);
          const decoded = arithmetic.decode(encoded);
          showResults('Aritmético', text, encoded, decoded);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '3': // LZ
        try {
          const text = await getInputText();
          const windowSize = await getNumberInput('Ingrese el tamaño de ventana (potencia de 2, ej: 8, 16, 32): ');
          
          // Verificar que sea potencia de 2
          if ((windowSize & (windowSize - 1)) !== 0) {
            console.log('❌ El tamaño de ventana debe ser una potencia de 2.');
            break;
          }
          
          const lz = new LZ(windowSize);
          const encoded = lz.encode(text);
          const decoded = lz.decode(encoded);
          showResults(`LZ (ventana: ${windowSize})`, text, encoded, decoded);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '4': // LZW
        try {
          const text = await getInputText();
          const windowSize = await getNumberInput('Ingrese el tamaño de ventana (potencia de 2, ej: 8, 16, 32): ');
          
          if ((windowSize & (windowSize - 1)) !== 0) {
            console.log('❌ El tamaño de ventana debe ser una potencia de 2.');
            break;
          }
          
          const lzw = new LZW(windowSize);
          const encoded = lzw.encode(text);
          const decoded = lzw.decode(encoded);
          console.log('\n=== RESULTADOS LZW ===');
          console.log(`Texto original: "${text}"`);
          console.log(`Tamaño original: ${text.length * 8} bits`);
          console.log(`Texto codificado: "${encoded}"`);
          console.log(`Tamaño codificado: ${encoded.length * 8} bits (cada carácter representa un código)`);
          console.log(`Texto decodificado: "${decoded}"`);
          console.log(`✅ Decodificación ${text === decoded ? 'exitosa' : 'fallida'}`);
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '0':
        return;
        
      default:
        console.log('❌ Opción no válida.');
    }
    
    await question('\nPresione Enter para continuar...');
  }
}

// Función para manejar métodos de Markov
async function handleMarkovMethods() {
  while (true) {
    clearConsole();
    showMarkovMethods();
    
    const choice = await question('Seleccione una opción: ');
    
    if (choice === '0') return;
    
    if (['1', '2', '3', '4'].includes(choice)) {
      try {
        if (choice === '4') {
          // Opción para mostrar matriz de transición
          const text = await getInputText();
          
          // Crear instancia de Markov con orden 1 (solo para obtener la matriz)
          const markov = new Markov(text, 1, Huffman);
          const transitionData = markov.getTransitionMatrix(text);
          
          showTransitionMatrix(
            transitionData.matrix, 
            transitionData.symbols, 
            transitionData.frequencies, 
            text
          );
          
        } else {
          // Opciones existentes de compresión con Markov
          const text = await getInputText();
          const order = await getNumberInput('Ingrese el orden de Markov (1, 2, 3, etc.): ');
          
          let markov: any;
          let methodName = '';
          
          switch (choice) {
            case '1':
              markov = new Markov(text, order, Huffman);
              methodName = `Markov (orden ${order}) + Huffman`;
              break;
            case '2':
              markov = new Markov(text, order, Fano);
              methodName = `Markov (orden ${order}) + Fano`;
              break;
            case '3':
              markov = new Markov(text, order, Shannon);
              methodName = `Markov (orden ${order}) + Shannon`;
              break;
          }
          
          const encoded = markov.encode(text);
          const decoded = markov.decode(encoded);
          showResults(methodName, text, encoded, decoded);
        }
        
      } catch (error) {
        console.log(`❌ Error: ${(error as Error).message}`);
      }
    } else {
      console.log('❌ Opción no válida.');
    }
    
    await question('\nPresione Enter para continuar...');
  }
}

// Función para manejar transformaciones auxiliares
async function handleTransformMethods() {
  while (true) {
    clearConsole();
    showTransformMethods();
    
    const choice = await question('Seleccione una opción: ');
    
    switch (choice) {
      case '1': // Burrows-Wheeler Codificar
        try {
          const text = await getInputText();
          const indicator = '$'; // Indicador por defecto
          
          console.log('\n=== CODIFICACIÓN BURROWS-WHEELER ===');
          console.log(`Texto original: "${text}"`);
          const encoded = BurrowsWheelerTransform.encode(text, indicator);
          console.log(`\n✅ Texto transformado: "${encoded}"`);
          
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '2': // Burrows-Wheeler Decodificar
        try {
          const encodedText = await question('Ingrese el texto codificado con Burrows-Wheeler: ');
          if (encodedText.trim() === '') {
            console.log('⚠️ El texto no puede estar vacío.');
            break;
          }
          
          const indicator = '$'; // Indicador por defecto
          
          console.log('\n=== DECODIFICACIÓN BURROWS-WHEELER ===');
          console.log(`Texto codificado: "${encodedText}"`);
          const decoded = BurrowsWheelerTransform.decodeStepByStep(encodedText, indicator);
          console.log(`\n✅ Texto original recuperado: "${decoded}"`);
          
        } catch (error) {
          console.log(`❌ Error: ${(error as Error).message}`);
        }
        break;
        
      case '0':
        return;
        
      default:
        console.log('❌ Opción no válida.');
    }
    
    await question('\nPresione Enter para continuar...');
  }
}

// Función para comparar métodos
async function handleComparisonMethods() {
  console.log('\n=== COMPARACIÓN DE MÉTODOS ===\n');
  
  try {
    const text = await getInputText();
    const source = Source.fromString(text);
    
    console.log('\n📊 Comparando métodos de compresión...\n');
    console.log(`Texto original: "${text}"`);
    console.log(`Tamaño original: ${text.length} caracteres (${text.length * 8} bits)\n`);
    
    const results: Array<{method: string, size: number, ratio: number}> = [];
    
    // Métodos estáticos
    try {
      const huffman = new Huffman(source);
      const huffmanEncoded = huffman.encode(text);
      results.push({
        method: 'Huffman',
        size: huffmanEncoded.length,
        ratio: (text.length * 8) / huffmanEncoded.length
      });
    } catch (e) { /* ignorar errores */ }
    
    try {
      const fano = new Fano(source);
      const fanoEncoded = fano.encode(text);
      results.push({
        method: 'Fano',
        size: fanoEncoded.length,
        ratio: (text.length * 8) / fanoEncoded.length
      });
    } catch (e) { /* ignorar errores */ }
    
    try {
      const shannon = new Shannon(source);
      const shannonEncoded = shannon.encode(text);
      results.push({
        method: 'Shannon',
        size: shannonEncoded.length,
        ratio: (text.length * 8) / shannonEncoded.length
      });
    } catch (e) { /* ignorar errores */ }
    
    try {
      const minAscii = MinASCII.fromString(text);
      const minAsciiEncoded = minAscii.encode(text);
      results.push({
        method: 'ASCII Mínimo',
        size: minAsciiEncoded.length,
        ratio: (text.length * 8) / minAsciiEncoded.length
      });
    } catch (e) { /* ignorar errores */ }
    
    try {
      const asciiEncoded = ASCII.encode(text);
      results.push({
        method: 'ASCII Estándar',
        size: asciiEncoded.length,
        ratio: (text.length * 8) / asciiEncoded.length
      });
    } catch (e) { /* ignorar errores */ }
    
    // Métodos dinámicos
    try {
      const adaptiveHuffman = new AdaptiveHuffman();
      const adaptiveEncoded = adaptiveHuffman.encodeSync(text);
      results.push({
        method: 'Huffman Adaptativo',
        size: adaptiveEncoded.length,
        ratio: (text.length * 8) / adaptiveEncoded.length
      });
    } catch (e) { /* ignorar errores */ }
    
    // Método aritmético
    try {
      const arithmetic = new Arithmetic(source);
      const arithmeticEncoded = arithmetic.encode(text);
      results.push({
        method: 'Aritmético',
        size: arithmeticEncoded.toString().length * 8, // Aproximación
        ratio: (text.length * 8) / (arithmeticEncoded.toString().length * 8)
      });
    } catch (e) { /* ignorar errores */ }
    
    // Ordenar por ratio de compresión
    results.sort((a, b) => b.ratio - a.ratio);
    
    console.log('🏆 RESULTADOS (ordenados por eficiencia):');
    console.log('─'.repeat(60));
    console.log('| Método          | Tamaño (bits) | Ratio | Eficiencia |');
    console.log('─'.repeat(60));
    
    results.forEach((result, index) => {
      const efficiency = (((text.length * 8 - result.size) / (text.length * 8)) * 100).toFixed(1);
      const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : '  ';
      console.log(`| ${medal} ${result.method.padEnd(12)} | ${result.size.toString().padStart(11)} | ${result.ratio.toFixed(2).padStart(5)} | ${efficiency.padStart(8)}% |`);
    });
    
    console.log('─'.repeat(60));
    
  } catch (error) {
    console.log(`❌ Error: ${(error as Error).message}`);
  }
  
  await question('\nPresione Enter para continuar...');
}

// Función para manejar el análisis de fuente independiente
async function handleSourceAnalysis() {
  console.log('\n=== ANÁLISIS DE FUENTE INDEPENDIENTE ===\n');
  
  try {
    const text = await getInputText();
    const source = Source.fromString(text);
    
    console.log('\n📊 Analizando propiedades de la fuente...\n');
    console.log(`Texto analizado: "${text}"`);
    console.log(`Tamaño: ${text.length} caracteres\n`);
    
    // Mostrar tabla de frecuencias
    console.log('📈 TABLA DE FRECUENCIAS:');
    console.log('─'.repeat(50));
    console.log('| Símbolo | Frecuencia | Probabilidad |');
    console.log('─'.repeat(50));
    
    const symbols = source.symbols;
    const totalChars = text.length;
    
    for (const symbol of symbols) {
      const prob = source.probabilities[symbol]!;
      const frequency = Math.round(prob.valueOf() * totalChars);
      const displaySymbol = symbol === ' ' ? 'ESPACIO' : 
                           symbol === '\n' ? '\\n' : 
                           symbol === '\t' ? '\\t' : 
                           symbol;
      
      console.log(`| ${displaySymbol.padEnd(7)} | ${frequency.toString().padStart(10)} | ${prob.valueOf().toFixed(4).padStart(12)} |`);
    }
    console.log('─'.repeat(50));
    
    // Calcular métricas
    const entropy = source.entropy().valueOf();
    const maxEntropy = Math.log2(symbols.length);
    const efficiency = entropy / maxEntropy;
    const redundancy = 1 - efficiency;
    
    console.log('\n🔍 MÉTRICAS DE LA FUENTE:');
    console.log('─'.repeat(50));
    console.log(`📏 Entropía (H): ${entropy.toFixed(4)} bits/símbolo`);
    console.log(`📏 Entropía máxima: ${maxEntropy.toFixed(4)} bits/símbolo`);
    console.log(`📏 Eficiencia (η): ${efficiency.toFixed(4)} (${(efficiency * 100).toFixed(2)}%)`);
    console.log(`📏 Redundancia (R): ${redundancy.toFixed(4)} (${(redundancy * 100).toFixed(2)}%)`);
    console.log(`📏 Redundancia absoluta: ${(redundancy * maxEntropy).toFixed(4)} bits/símbolo`);
    console.log('─'.repeat(50));
    
    console.log('\n📚 INTERPRETACIÓN:');
    if (efficiency > 0.9) {
      console.log('✅ La fuente es muy eficiente (baja redundancia)');
    } else if (efficiency > 0.7) {
      console.log('⚠️  La fuente tiene eficiencia moderada');
    } else {
      console.log('❌ La fuente tiene alta redundancia (baja eficiencia)');
    }
    
    console.log(`💡 La fuente utiliza ${(efficiency * 100).toFixed(1)}% de su capacidad máxima de información`);
    console.log(`💡 La redundancia es del ${(redundancy * 100).toFixed(1)}%`);
    
    if (redundancy > 0.1) {
      const bitsSaved = redundancy * maxEntropy;
      console.log(`💡 Se podrían ahorrar aproximadamente ${bitsSaved.toFixed(2)} bits por símbolo con compresión óptima`);
    }
    
  } catch (error) {
    console.log(`❌ Error: ${(error as Error).message}`);
  }
  
  await question('\nPresione Enter para continuar...');
}

// Función principal
async function main() {
  console.log('🚀 Iniciando Sistema de Compresión de Datos...');
  
  while (true) {
    clearConsole();
    showMainMenu();
    
    const choice = await question('Seleccione una opción: ');
    
    switch (choice) {
      case '1':
        await handleStaticMethods();
        break;
        
      case '2':
        await handleDynamicMethods();
        break;
        
      case '3':
        await handleMarkovMethods();
        break;
        
      case '4':
        await handleTransformMethods();
        break;
        
      case '5':
        await handleComparisonMethods();
        break;
        
      case '6':
        await handleSourceAnalysis();
        break;
        
      case '0':
        console.log('\n👋 ¡Gracias por usar el Sistema de Compresión de Datos!');
        rl.close();
        process.exit(0);
        
      default:
        console.log('❌ Opción no válida. Por favor seleccione una opción del menú.');
        await question('Presione Enter para continuar...');
    }
  }
}

// Manejo de errores globales
process.on('unhandledRejection', (error) => {
  console.error('❌ Error no manejado:', error);
  rl.close();
  process.exit(1);
});

process.on('SIGINT', () => {
  console.log('\n\n👋 Programa interrumpido por el usuario.');
  rl.close();
  process.exit(0);
});

// Ejecutar programa principal
if (require.main === module) {
  main().catch((error) => {
    console.error('❌ Error fatal:', error);
    rl.close();
    process.exit(1);
  });
}
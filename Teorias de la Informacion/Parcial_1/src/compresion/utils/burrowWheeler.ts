import { assert } from 'console';

export default class BurrowsWheelerTransform {
  public static encode(str: string, indicator = '$'): string {
    str += indicator;
    const rotations = Array(str.length)
      .fill(0)
      .map((_, i) => str.slice(i) + str.slice(0, i));

    console.log('Rotaciones sin ordenar');
    console.log(rotations.join('\n'));

    const sorted = rotations.sort();

    const encoded = sorted.map((str) => str[str.length - 1]).join('');

    console.log();
    console.log('Rotaciones ordenadas');
    console.log(sorted.join('\n'));
    console.log();
    console.log(`Encoded: ${encoded}`);

    return encoded;
  }

  public static decode(str: string, indicator = '$'): string {
    const l_shift = Array.from(str)
      .map((_, i) => i)
      .sort((a, b) => str[a]!.localeCompare(str[b]!));

    console.log(l_shift);

    const decoded = Array(str.length);

    let x = str.indexOf(indicator);
    for (let i = 0; i < str.length; i++) {
      x = l_shift[x]!;
      decoded[i] = str[x]!;
    }

    return decoded.join('').slice(0, -1);
  }

  public static decodeStepByStep(str: string, indicator = '$'): string {
    console.log('\n🔄 PROCESO DE DECODIFICACIÓN PASO A PASO');
    console.log('═'.repeat(50));
    
    // Última columna (texto transformado)
    const lastColumn = str.split('');
    console.log(`\n📝 Entrada - Última columna (transformada): [${lastColumn.join(', ')}]`);
    
    // Crear tabla paso a paso - inicializamos con strings vacíos
    let table: string[] = new Array(str.length).fill('');
    
    console.log('\n🏁 CONSTRUCCIÓN DE LA MATRIZ PASO A PASO:');
    console.log('Vamos añadiendo la última columna al principio y ordenando en cada paso\n');
    
    // Construir tabla paso a paso
    for (let step = 0; step < str.length; step++) {
      // Añadir la última columna al principio de cada string
      for (let i = 0; i < str.length; i++) {
        table[i] = lastColumn[i]! + table[i]!;
      }
      
      console.log(`➕ PASO ${step + 1}a: Añadir última columna al principio`);
      this.printTableStep(table, step + 1, false);
      
      // Ordenar alfabéticamente ($ es menor que cualquier letra)
      table.sort((a, b) => this.compareWithIndicator(a, b, indicator));
      
      console.log(`📊 PASO ${step + 1}b: Ordenar alfabéticamente ($ < A < B < C...)`);
      this.printTableStep(table, step + 1, true);
    }
    
    console.log('\n🎯 TABLA FINAL COMPLETA:');
    this.printFinalTable(table, indicator);
    
    // Encontrar la fila que termina con el indicador
    const originalRow = table.find(row => row.endsWith(indicator));
    if (!originalRow) {
      throw new Error(`No se encontró una fila que termine con el indicador '${indicator}'`);
    }
    
    const originalText = originalRow.slice(0, -1); // Remover el indicador
    
    console.log(`\n✨ La fila que termina con '${indicator}' contiene el texto original:`);
    console.log(`🔤 Texto original recuperado: "${originalText}"`);
    
    return originalText;
  }

  private static printTableStep(table: string[], _step: number, isAfterSort: boolean) {
    const stepType = isAfterSort ? 'ORDENADO' : 'ANTES DE ORDENAR';
    const maxLength = Math.max(...table.map(s => s.length));
    
    console.log(`\n┌─ ${stepType} ${'─'.repeat(Math.max(0, maxLength * 2 - stepType.length))}┐`);
    
    table.forEach((row) => {
      const paddedRow = row.padEnd(maxLength);
      const indicator = row.endsWith('$') ? ' ← 🎯' : '';
      console.log(`│ ${paddedRow} │${indicator}`);
    });
    
    console.log('└─' + '─'.repeat(maxLength + 2) + '┘');
  }

  private static printFinalTable(table: string[], indicator: string) {
    const maxLength = Math.max(...table.map(s => s.length));
    
    console.log('\n┌─' + '─'.repeat(maxLength + 2) + '┐');
    console.log('│ ' + 'MATRIZ FINAL COMPLETA'.padEnd(maxLength) + ' │');
    console.log('├─' + '─'.repeat(maxLength + 2) + '┤');
    
    table.forEach((row) => {
      const paddedRow = row.padEnd(maxLength);
      const isOriginal = row.endsWith(indicator) ? ' ← 🎯 ORIGINAL' : '';
      console.log(`│ ${paddedRow} │${isOriginal}`);
    });
    
    console.log('└─' + '─'.repeat(maxLength + 2) + '┘');
  }

  private static compareWithIndicator(a: string, b: string, indicator: string): number {
    for (let i = 0; i < Math.min(a.length, b.length); i++) {
      const charA = a[i];
      const charB = b[i];
      
      // Si uno es el indicador y el otro no
      if (charA === indicator && charB !== indicator) return -1;
      if (charA !== indicator && charB === indicator) return 1;
      
      // Comparación normal
      if (charA! < charB!) return -1;
      if (charA! > charB!) return 1;
    }
    
    // Si son iguales hasta aquí, el más corto va primero
    return a.length - b.length;
  }

  public static encodeNoIndicator(str: string): [string, number] {
    const rotations = Array(str.length)
      .fill(0)
      .map((_, i) => str.slice(i) + str.slice(0, i));
    const sorted = rotations.sort();

    console.log(sorted.join('\n'));

    const rotationIndex = sorted.indexOf(str);
    const encoded = sorted.map((str) => str.slice(-1)).join('');

    return [encoded, rotationIndex];
  }

  public static decodeNoIndicator(str: string, rotationIndex: number): string {
    const table = str.split('');

    for (let i = 0; i < str.length - 1; i++) {
      table.sort();
      for (let j = 0; j < str.length; j++) {
        table[j] = str[j]! + table[j];
      }
    }

    table.sort();

    return table[rotationIndex]!;
  }
}

const test = (testStr: string) => {
  const encoded = BurrowsWheelerTransform.encode(testStr);
  const decoded = BurrowsWheelerTransform.decode(encoded);

  assert(testStr === decoded);

  // const encoded2 = BurrowsWheelerTransform.encodeNoIndicator(testStr);
  //
  // console.log(`Encoded ${encoded2}`);
  //
  // const decoded2 = BurrowsWheelerTransform.decodeNoIndicator(...encoded2);
  //
  // assert(testStr === decoded2);
};

if (require.main === module) {
  // test('banana');
  test('ABRACADABRA');
  // test('abracadabra'.repeat(100));
  // test('anana');
  // test('sdgarewgarfh');
  // test('asdgfasdg');
  // test('jdtykfhjg');
}

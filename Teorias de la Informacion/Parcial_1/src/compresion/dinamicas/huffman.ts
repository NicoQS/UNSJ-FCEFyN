import { CodificationWithOne } from '../core/base';
import { ASCII } from '../estaticas/ASCII';

class HuffmanNode {
  constructor(
    public weight = 0,
    public parent: HuffmanNode | null = null,
    public symbol: string | null = null
  ) {}
  public right: HuffmanNode | null = null;
  public left: HuffmanNode | null = null;

  public replace(a: HuffmanNode, b: HuffmanNode): void {
    if (this.right === a) {
      this.right = b;
    } else if (this.left === a) {
      this.left = b;
    } else {
      throw new Error('Node not found');
    }
  }

  get isLeaf(): boolean {
    return this.left === null && this.right === null;
  }

  get code(): string {
    return this.parent
      ? this.parent.code + (this.parent.right === this ? '1' : '0')
      : '';
  }
}

class HuffmanTree {
  constructor() {
    this.emptyNode = this.root = new HuffmanNode();
    this.nodes = {};
  }
  public emptyNode: HuffmanNode;
  public root: HuffmanNode;
  public nodes: Record<string, HuffmanNode>;

  protected getCodeForSymbol(c: string): string | null {
    return this.nodes[c]?.code || null;
  }

  protected getNodeFromCode(code: string): HuffmanNode {
    let p: HuffmanNode = this.root;
    if (p.isLeaf) return p;

    for (const bit of code) {
      p = bit === '1' ? p.right! : p.left!;

      if (p.isLeaf) return p; // will not reach the end of the code
    }

    if (!p.isLeaf) throw new Error('Invalid code');

    return p;
  }

  protected addNew(c: string): string {
    const code = this.emptyNode.code || '0';

    const parent = this.emptyNode;
    const rightNode = new HuffmanNode(0, parent, c);
    const leftNode = new HuffmanNode(0, parent);

    this.nodes[c] = rightNode;
    parent.right = rightNode;
    parent.left = leftNode;
    this.emptyNode = leftNode;

    return code;
  }

  protected update(node: HuffmanNode | null) {
    while (node) {
      const leader = this._leaderOfWeight(node.weight);

      if (leader !== node && leader !== node.parent) {
        HuffmanTree.swap(leader, node);
      }

      node.weight++;
      node = node.parent;
    }
  }

  protected close(): void {
    // eliminate empty node
    const parent = this.emptyNode.parent!;
    const parentParent = parent.parent;
    const sibling =
      parent.left === this.emptyNode ? parent.right! : parent.left!;

    if (parentParent) {
      parentParent!.replace(parent, sibling);
      sibling.parent = parentParent;
    }
  }

  private _leaderOfWeight(w: number): HuffmanNode {
    const list = [this.root];

    for (const node of list) {
      if (node.weight === w) return node;
      if (!node.isLeaf) list.push(node.right!, node.left!);
    }

    throw new Error('Never should reach here');
  }

  private static swap(a: HuffmanNode, b: HuffmanNode): void {
    const temp = b.parent!.right;

    a.parent!.replace(a, b);

    if (temp === b) {
      b.parent!.right = a;
    } else {
      b.parent!.left = a;
    }

    [a.parent, b.parent] = [b.parent, a.parent];
  }

  public print(): void {
    try {
      const printTree = require('print-tree');
      printTree(
        this.root,
        (node: HuffmanNode) => {
          if (node === this.emptyNode) return `EMPTY [${node.code || '0'}]`;
          if (node.isLeaf) return `${node.weight} (${node.symbol}: ${node.code})`;

          return `${node.weight.toString()} [${node.code}]`;
        },
        (node: HuffmanNode) => (node.isLeaf ? [] : [node.right!, node.left!])
      );
    } catch (error) {
      // Si print-tree no está disponible, usar una representación simple
      console.log('Árbol de Huffman (representación simplificada):');
      this.printSimple(this.root, '', true);
    }
  }

  private printSimple(node: HuffmanNode | null, prefix: string = '', isLast: boolean = true): void {
    if (!node) return;
    
    const connector = isLast ? '└── ' : '├── ';
    const nodeInfo = node === this.emptyNode ? `EMPTY [${node.code || '0'}]` : 
                     node.isLeaf ? `${node.symbol} (${node.weight}) [${node.code}]` : 
                     `Peso: ${node.weight} [${node.code}]`;
    
    console.log(prefix + connector + nodeInfo);
    
    if (!node.isLeaf) {
      const newPrefix = prefix + (isLast ? '    ' : '│   ');
      if (node.right) this.printSimple(node.right, newPrefix, false);
      if (node.left) this.printSimple(node.left, newPrefix, true);
    }
  }
}

const ALL_ASCII: string[] = Array.from({ length: 256 }, (_, i) =>
  String.fromCharCode(i)
);

// Pseudo ASCII con longitud fija basado en el universo de símbolos
class PseudoASCII implements CodificationWithOne<string> {
  private codeTable: Record<string, string> = {};
  private decodeTable: Record<string, string> = {};
  private bitsPerSymbol: number;

  constructor(symbols: string[] | string) {
    const uniqueSymbols = Array.from(new Set(symbols));
    this.bitsPerSymbol = Math.ceil(Math.log2(uniqueSymbols.length)) || 1;
    
    // Crear tabla de códigos de longitud fija
    uniqueSymbols.forEach((symbol, index) => {
      const code = index.toString(2).padStart(this.bitsPerSymbol, '0');
      this.codeTable[symbol] = code;
      this.decodeTable[code] = symbol;
    });
  }

  encode(symbol: string): string {
    const code = this.codeTable[symbol];
    if (code === undefined) {
      throw new Error(`Símbolo '${symbol}' no encontrado en la tabla de códigos`);
    }
    return code;
  }

  decode(code: string): string {
    const symbol = this.decodeTable[code];
    if (symbol === undefined) {
      throw new Error(`Código '${code}' no encontrado en la tabla de decodificación`);
    }
    return symbol;
  }

  decodeOne(str: string): [string, string] {
    const code = str.substring(0, this.bitsPerSymbol);
    const symbol = this.decode(code);
    return [symbol, code];
  }

  getCodes(): Record<string, string> {
    return { ...this.codeTable };
  }

  getBitsPerSymbol(): number {
    return this.bitsPerSymbol;
  }
}

class AdaptiveHuffmanEncoder extends HuffmanTree {
  constructor(
    public defaultCode: CodificationWithOne<string> = ASCII,
    allSymbols: string[] | string = ALL_ASCII,
    private interactive: boolean = false,
    private questionCallback?: (prompt: string) => Promise<string>
  ) {
    super();
    this.allSymbols = new Set(allSymbols);
    
    // Si se proporciona un conjunto específico de símbolos, usar PseudoASCII
    if (allSymbols !== ALL_ASCII && Array.isArray(allSymbols)) {
      this.defaultCode = new PseudoASCII(allSymbols);
    } else if (typeof allSymbols === 'string' && allSymbols.length > 0) {
      this.defaultCode = new PseudoASCII(allSymbols);
    }
  }
  private allSymbols: Set<string>;

  // Getter para acceder a los nodos desde fuera
  get nodesCodes(): Record<string, HuffmanNode> {
    return this.nodes;
  }

  async encode(str: string): Promise<string> {
    let encoded = '';
    
    if (this.interactive) {
      console.log(`\n🎯 ANÁLISIS DEL UNIVERSO DE SÍMBOLOS:`);
      const uniqueSymbols = Array.from(new Set(str));
      console.log(`Símbolos únicos encontrados: ${uniqueSymbols.join(', ')}`);
      console.log(`Total de símbolos únicos: ${uniqueSymbols.length}`);
      const bitsNeeded = Math.ceil(Math.log2(uniqueSymbols.length)) || 1;
      console.log(`Bits necesarios para representar todos los símbolos: ${bitsNeeded}`);
      
      if (this.defaultCode instanceof PseudoASCII) {
        console.log(`\n📋 TABLA DE CÓDIGOS FIJOS (Pseudo ASCII):`);
        const codes = this.defaultCode.getCodes();
        Object.entries(codes).forEach(([symbol, code]) => {
          console.log(`  '${symbol}' → ${code}`);
        });
      }
      
      console.log(`\n🔄 PROCESO DE CODIFICACIÓN PASO A PASO:`);
      console.log('─'.repeat(50));
    }
    
    for (let i = 0; i < str.length; i++) {
      const char = str.charAt(i);
      
      if (this.interactive) {
        const isFirstIteration = Object.keys(this.nodes).length === 0;
        
        console.log(`\n📍 Iteración ${i + 1}/${str.length}: Procesando '${char}'`);
        
        if (isFirstIteration) {
          console.log(`🌟 Primera iteración: El árbol solo contiene el nodo EMPTY`);
          console.log(`💡 Se codificará directamente con PseudoASCII (sin prefijo)`);
        } else {
          console.log(`🔄 Iteración normal: El carácter se buscará en el árbol`);
        }
        
        console.log(`Estado actual del árbol:`);
        this.print();
      }
      
      const charCode = this.encodeOne(char);
      encoded += charCode;
      
      if (this.interactive) {
        console.log(`✅ Carácter '${char}' codificado como: ${charCode}`);
        console.log(`Código acumulado: ${encoded}`);
        console.log('─'.repeat(50));
        
        // Pausa para que el usuario pueda leer
        if (this.questionCallback) {
          await new Promise(resolve => setTimeout(resolve, 1500)); // Pausa de 1.5 segundos
        }
      }
    }

    if (this.interactive) {
      console.log(`\n🏁 RESULTADO FINAL:`);
      console.log(`Texto original: "${str}"`);
      console.log(`Texto codificado: ${encoded}`);
      console.log(`Longitud original: ${str.length * 8} bits (ASCII estándar)`);
      console.log(`Longitud codificada: ${encoded.length} bits`);
      const compression = ((str.length * 8 - encoded.length) / (str.length * 8) * 100).toFixed(1);
      console.log(`Compresión obtenida: ${compression}%`);
    }

    return encoded;
  }

  // Versión síncrona para compatibilidad
  encodeSync(str: string): string {
    let encoded = '';
    for (const char of str) {
      encoded += this.encodeOne(char);
    }
    return encoded;
  }

  encodeOne(c: string): string {
    let code = this.getCodeForSymbol(c);
    if (!code) {
      // Verificar si es la primera iteración (solo existe el nodo EMPTY)
      const isFirstIteration = Object.keys(this.nodes).length === 0;
      
      if (isFirstIteration) {
        // En la primera iteración, usar solo el código PseudoASCII
        code = this.defaultCode.encode(c);
      } else {
        // En iteraciones posteriores, usar código del nodo EMPTY + PseudoASCII
        code = this.addNew(c) + this.defaultCode.encode(c);
      }
      
      // Si es la primera iteración, realizar addNew después de obtener el código
      if (isFirstIteration) {
        this.addNew(c);
      }

      this.allSymbols.delete(c);
      if (this.allSymbols.size === 0) this.close();
    }

    this.update(this.nodes[c] || null);
    return code;
  }
}

class AdaptiveHuffmanDecoder extends HuffmanTree {
  constructor(
    public defaultCode: CodificationWithOne<string> = ASCII,
    allSymbols?: string[] | string
  ) {
    super();
    this.allSymbols = new Set(allSymbols);
    if (!this.defaultCode.decodeOne)
      throw new Error('DecodeOne not implemented');
      
    // Si se proporciona un conjunto específico de símbolos, usar PseudoASCII
    if (allSymbols && Array.isArray(allSymbols)) {
      this.defaultCode = new PseudoASCII(allSymbols);
    } else if (typeof allSymbols === 'string' && allSymbols.length > 0) {
      this.defaultCode = new PseudoASCII(allSymbols);
    }
  }
  private allSymbols: Set<string>;

  decode(str: string): string {
    let decoded = '';
    let i = 0;

    while (i < str.length) {
      const [symbol, code] = this.decodeOne(str.slice(i));
      decoded += symbol;
      i += code.length;

      // Comentamos el print para no sobrecargar la consola
      // this.print();
    }

    return decoded;
  }

  decodeOne(str: string): [string, string] {
    const node = this.getNodeFromCode(str);

    if (node.symbol) {
      this.update(node);
      return [node.symbol, node.code];
    }
    if (node !== this.emptyNode) {
      throw new Error('Invalid code');
    }

    // Verificar si es la primera iteración (solo existe el nodo EMPTY)
    const isFirstIteration = Object.keys(this.nodes).length === 0;
    
    if (isFirstIteration) {
      // En la primera iteración, decodificar directamente con PseudoASCII
      const [symbol, code] = this.defaultCode.decodeOne!(str);
      this.addNew(symbol);
      this.update(this.nodes[symbol] || null);
      this.allSymbols.delete(symbol);
      if (this.allSymbols.size === 0) this.close();
      
      return [symbol, code];
    } else {
      // En iteraciones posteriores, usar código del nodo EMPTY + PseudoASCII
      str = str.slice(node.code.length);
      const emptyNodeCode = this.emptyNode.code || '0';
      const [symbol, code] = this.defaultCode.decodeOne!(str);

      this.addNew(symbol);
      this.update(this.nodes[symbol] || null);
      this.allSymbols.delete(symbol);
      if (this.allSymbols.size === 0) this.close();

      return [symbol, emptyNodeCode + code];
    }
  }
}

// Clase principal para Huffman Adaptativo que combina encoder y decoder
export class AdaptiveHuffman {
  private encoder: AdaptiveHuffmanEncoder;
  private decoder: AdaptiveHuffmanDecoder;
  private lastText: string = '';

  constructor(
    defaultCode: CodificationWithOne<string> = ASCII, 
    allSymbols?: string[] | string,
    private interactive: boolean = false,
    private questionCallback?: (prompt: string) => Promise<string>
  ) {
    this.encoder = new AdaptiveHuffmanEncoder(defaultCode, allSymbols, this.interactive, this.questionCallback);
    this.decoder = new AdaptiveHuffmanDecoder(defaultCode, allSymbols);
  }

  /**
   * Codifica una cadena de texto usando Huffman adaptativo
   */
  async encode(text: string): Promise<string> {
    this.lastText = text;
    // Reiniciar el encoder para cada nueva codificación
    this.encoder = new AdaptiveHuffmanEncoder(
      this.encoder.defaultCode, 
      text, 
      this.interactive, 
      this.questionCallback
    );
    return await this.encoder.encode(text);
  }

  /**
   * Codifica de forma síncrona (sin interactividad)
   */
  encodeSync(text: string): string {
    this.lastText = text;
    this.encoder = new AdaptiveHuffmanEncoder(this.encoder.defaultCode, text, false);
    return this.encoder.encodeSync(text);
  }

  /**
   * Decodifica una cadena codificada usando Huffman adaptativo
   */
  decode(encodedText: string, originalText?: string): string {
    const textToUse = originalText || this.lastText;
    if (!textToUse) {
      throw new Error('No se puede decodificar sin conocer el texto original o haber codificado previamente');
    }
    // Reiniciar el decoder con los símbolos del texto original
    this.decoder = new AdaptiveHuffmanDecoder(this.decoder.defaultCode, textToUse);
    return this.decoder.decode(encodedText);
  }

  /**
   * Obtiene información sobre los códigos generados después de la codificación
   */
  getCodes(): Record<string, string> {
    const codes: Record<string, string> = {};
    
    // Agregar códigos del árbol de Huffman adaptativo
    for (const [symbol, node] of Object.entries(this.encoder.nodesCodes)) {
      if (node && node.code !== undefined) {
        codes[`${symbol} (Huffman)`] = node.code;
      }
    }
    
    // Agregar códigos del PseudoASCII si está disponible
    if (this.encoder.defaultCode instanceof PseudoASCII) {
      const pseudoCodes = this.encoder.defaultCode.getCodes();
      for (const [symbol, code] of Object.entries(pseudoCodes)) {
        codes[`${symbol} (PseudoASCII)`] = code;
      }
    }
    
    return codes;
  }

  /**
   * Muestra el árbol de Huffman (para debugging)
   */
  printTree(): void {
    console.log('\n=== Árbol de Huffman Adaptativo ===');
    this.encoder.print();
  }

  /**
   * Habilita o deshabilita el modo interactivo
   */
  setInteractive(interactive: boolean, questionCallback?: (prompt: string) => Promise<string>): void {
    this.interactive = interactive;
    this.questionCallback = questionCallback;
  }
}

// Exportar también las clases individuales para uso avanzado
export { AdaptiveHuffmanEncoder, AdaptiveHuffmanDecoder };

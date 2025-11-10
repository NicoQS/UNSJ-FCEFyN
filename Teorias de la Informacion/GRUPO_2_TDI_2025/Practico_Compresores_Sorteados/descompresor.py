"""
===============================================================================
MÓDULO DE DESCOMPRESIÓN - LZW + HUFFMAN ADAPTATIVO
===============================================================================

Este módulo implementa el proceso inverso de compresión, realizando la
descompresión en dos etapas:

ETAPA 1: Descompresión Huffman Adaptativa (FGK/NYT)
    - Reconstruye el árbol Huffman dinámicamente (igual que en compresión)
    - Lee el bitstream comprimido y recupera los bytes del output LZW
    - Mantiene sincronización perfecta con el compresor

ETAPA 2: Descompresión LZW (Lempel-Ziv-Welch)
    - Deserializa el output LZW (diccionario + códigos)
    - Reconstruye el diccionario a partir de parent_bytes
    - Decodifica los códigos LZW para obtener datos originales

PROCESO COMPLETO:
    Archivo .comp → Huffman Decompressor → Output LZW → LZW Decompressor → Datos originales

El resultado de la descompresión es IDÉNTICO byte por byte al archivo original.

Autor: Grupo 2 - Teorías de la Información 2025
Fecha: Noviembre 2025
===============================================================================
"""

import struct

# ============================================================================
# SECCIÓN 1: DESCOMPRESIÓN LZW
# ============================================================================

def lzw_decompress(codes, parent_bytes):
    """
    Descomprime códigos LZW usando el diccionario reconstruido.
    
    El algoritmo de descompresión LZW funciona así:
    1. Reconstruir diccionario inicial (256 entradas) + entradas generadas
    2. Para cada código en la secuencia:
       - Si el código existe en el diccionario: usar su entrada
       - Si el código == tamaño del diccionario: caso especial (código futuro)
       - Agregar nueva entrada al diccionario combinando entradas anteriores
    3. El resultado es la concatenación de todas las entradas decodificadas
    
    CASO ESPECIAL (código == len(diccionario)):
    Ocurre cuando el compresor emitió un código para una entrada que
    acababa de crear. En este caso, la nueva entrada es la entrada anterior
    más su propio primer byte.
    
    Args:
        codes (list): Lista de códigos LZW a decodificar
        parent_bytes (list): Lista de tuplas (parent_idx, new_byte) que
                            representa las entradas del diccionario generadas
    
    Returns:
        bytes: Datos descomprimidos originales
    
    Raises:
        ValueError: Si se encuentra un código LZW inválido
    
    Ejemplo:
        Si codes = [72, 101, 108, 256, 111]
        y parent_bytes = [(108, 108)]
        Diccionario: 0-255 (bytes) + 256=dictionary[108]+b'l'
        Resultado: H e l ll o
    """
    # Límite del diccionario (mismo que en compresión)
    MAX_DICT_SIZE = 1024
    
    # ========================================
    # RECONSTRUCCIÓN DEL DICCIONARIO
    # ========================================
    # Inicializar con entradas 0-255 (todos los bytes posibles)
    dictionary = [bytes([i]) for i in range(256)]
    
    # Agregar entradas generadas durante la compresión
    for parent_idx, new_byte in parent_bytes:
        # Nueva entrada = entrada del padre + nuevo byte
        entry = dictionary[parent_idx] + bytes([new_byte])
        dictionary.append(entry)
    
    # Validar que hay códigos para decodificar
    if not codes:
        return b''
    
    # ========================================
    # DECODIFICACIÓN DE CÓDIGOS
    # ========================================
    result = bytearray()
    
    # Procesar primer código
    prev_code = codes[0]
    result.extend(dictionary[prev_code])
    
    # Procesar códigos restantes
    for code in codes[1:]:
        # Determinar la entrada para este código
        if code < len(dictionary):
            # Código existe en el diccionario
            entry = dictionary[code]
        elif code == len(dictionary):
            # CASO ESPECIAL: código para entrada que acabamos de crear
            # La entrada es: entrada_anterior + primer_byte(entrada_anterior)
            entry = dictionary[prev_code] + dictionary[prev_code][:1]
        else:
            # Código inválido (no debería ocurrir con datos válidos)
            raise ValueError(f"Código LZW inválido: {code}")
        
        # Agregar entrada decodificada al resultado
        result.extend(entry)
        
        # Agregar nueva entrada al diccionario si hay espacio
        if len(dictionary) < MAX_DICT_SIZE:
            # Nueva entrada = entrada_anterior + primer_byte(entrada_actual)
            dictionary.append(dictionary[prev_code] + entry[:1])
        
        # Actualizar código anterior
        prev_code = code
    
    return bytes(result)


def deserialize_lzw_output(lzw_bytes):
    """
    Deserializa el output de LZW para obtener códigos y diccionario.
    
    Esta función es el inverso de serialize_lzw_output() del compresor.
    Lee el formato binario y extrae el diccionario y los códigos.
    
    FORMATO ESPERADO:
    
     1. Header del diccionario (2 bytes)                         
        - Número de entradas del diccionario                     
     2. Entradas del diccionario (3 bytes cada una)              
        Para cada entrada:                                       
        - parent_idx (2 bytes): índice del padre                 
        - new_byte (1 byte): byte que se agrega                  
     3. Header de códigos (4 bytes)                              
        - Número total de códigos                                
     4. Códigos comprimidos (12 bits cada uno)                   
        - Códigos LZW empaquetados en bits                       
    
    Args:
        lzw_bytes (bytes): Datos serializados del output LZW
    
    Returns:
        tuple: (codes, parent_bytes)
            - codes (list): Lista de códigos LZW
            - parent_bytes (list): Lista de tuplas (parent_idx, new_byte)
    
    Raises:
        ValueError: Si los datos están incompletos o son inválidos
    """
    pos = 0  # Posición actual en el buffer
    
    # ========================================
    # 1. LEER HEADER DEL DICCIONARIO
    # ========================================
    if pos + 2 > len(lzw_bytes):
        raise ValueError("Archivo LZW incompleto")
    # Leer número de entradas (2 bytes, big-endian)
    num_dict_entries = struct.unpack('>H', lzw_bytes[pos:pos+2])[0]
    pos += 2
    
    # ========================================
    # 2. LEER DICCIONARIO
    # ========================================
    parent_bytes = []
    for _ in range(num_dict_entries):
        # Verificar que hay suficientes bytes
        if pos + 3 > len(lzw_bytes):
            raise ValueError("Diccionario LZW incompleto")
        
        # Leer parent_idx (2 bytes)
        parent_idx = struct.unpack('>H', lzw_bytes[pos:pos+2])[0]
        pos += 2
        
        # Leer new_byte (1 byte)
        new_byte = lzw_bytes[pos]
        pos += 1
        
        parent_bytes.append((parent_idx, new_byte))
    
    # ========================================
    # 3. LEER HEADER DE CÓDIGOS
    # ========================================
    if pos + 4 > len(lzw_bytes):
        raise ValueError("Header de códigos LZW incompleto")
    # Leer número de códigos (4 bytes, big-endian)
    num_codes = struct.unpack('>I', lzw_bytes[pos:pos+4])[0]
    pos += 4
    
    # ========================================
    # 4. LEER CÓDIGOS
    # ========================================
    # Crear lector de bits para los códigos
    br = BitReader(lzw_bytes[pos:])
    codes = []
    
    # Leer cada código (12 bits cada uno)
    for _ in range(num_codes):
        code = br.read_bits(12)
        codes.append(code)
    
    return codes, parent_bytes


# ============================================================================
# SECCIÓN 2: HUFFMAN ADAPTATIVO (FGK/NYT) - DESCOMPRESIÓN
# ============================================================================

class HuffmanNode:
    """
    Nodo del árbol Huffman adaptativo (descompresión).
    
    Idéntico a la clase HuffmanNode del compresor. Es crucial que ambos
    (compresor y descompresor) utilicen la misma estructura y lógica para
    mantener árboles sincronizados.
    
    Attributes:
        symbol (int|None): Símbolo representado (None para nodos internos/NYT)
        weight (int): Frecuencia acumulada
        parent (HuffmanNode|None): Nodo padre
        left (HuffmanNode|None): Hijo izquierdo
        right (HuffmanNode|None): Hijo derecho
        order (int): Orden del nodo (para algoritmo FGK)
    """
    def __init__(self, symbol=None, weight=0, parent=None, order=0):
        self.symbol = symbol
        self.weight = weight
        self.parent = parent
        self.left = None
        self.right = None
        self.order = order


class AdaptiveHuffman:
    """
    Árbol Huffman Adaptativo para descompresión.
    
    Esta clase DEBE mantener sincronización perfecta con el AdaptiveHuffman
    del compresor. Ambos deben:
    - Inicializarse de la misma manera
    - Actualizar el árbol en el mismo orden
    - Realizar los mismos swaps de nodos
    
    La sincronización garantiza que el descompresor pueda interpretar
    correctamente los caminos en el árbol enviados por el compresor.
    
    Attributes:
        next_order (int): Siguiente orden disponible
        NYT (HuffmanNode): Nodo Not Yet Transmitted
        root (HuffmanNode): Raíz del árbol
        leaves (dict): Mapeo símbolo -> nodo hoja
        all_nodes (list): Lista de todos los nodos
    """
    def __init__(self):
        # Inicialización idéntica al compresor
        self.next_order = 512
        self.NYT = HuffmanNode(symbol=None, weight=0, order=self.next_order)
        self.next_order -= 1
        self.root = self.NYT
        self.leaves = {}
        self.all_nodes = [self.NYT]

    def _find_leader(self, node):
        """
        Encuentra el líder del bloque (idéntico al compresor).
        
        Ver documentación en compresor.py para detalles completos.
        """
        max_order = -1
        leader = None
        for n in self.all_nodes:
            if n.weight == node.weight and n.order > node.order and n != node.parent:
                if n.order > max_order:
                    max_order = n.order
                    leader = n
        return leader

    def _swap_nodes(self, a, b):
        """
        Intercambia dos nodos (idéntico al compresor).
        
        Ver documentación en compresor.py para detalles completos.
        """
        a_parent = a.parent
        b_parent = b.parent
        
        if a_parent:
            if a_parent.left == a:
                a_parent.left = b
            else:
                a_parent.right = b
        
        if b_parent:
            if b_parent.left == b:
                b_parent.left = a
            else:
                b_parent.right = a
        
        a.parent, b.parent = b_parent, a_parent
        a.order, b.order = b.order, a.order
        
        if self.root == a:
            self.root = b
        elif self.root == b:
            self.root = a
        
        if a.symbol is not None:
            self.leaves[a.symbol] = a
        if b.symbol is not None:
            self.leaves[b.symbol] = b

    def update(self, symbol):
        """
        Actualiza el árbol después de decodificar un símbolo (idéntico al compresor).
        
        CRÍTICO: Este método DEBE ejecutarse exactamente de la misma manera
        que en el compresor para mantener sincronización de árboles.
        
        Args:
            symbol (int): Símbolo decodificado (0-255)
        """
        if symbol in self.leaves:
            # Símbolo ya existe: incrementar desde su hoja
            node = self.leaves[symbol]
            while node:
                leader = self._find_leader(node)
                if leader and leader != node.parent:
                    self._swap_nodes(node, leader)
                node.weight += 1
                node = node.parent
        else:
            # Símbolo nuevo: dividir NYT
            old_NYT = self.NYT
            new_NYT = HuffmanNode(symbol=None, weight=0, parent=old_NYT, order=self.next_order)
            self.next_order -= 1
            new_leaf = HuffmanNode(symbol=symbol, weight=0, parent=old_NYT, order=self.next_order)
            self.next_order -= 1
            
            old_NYT.left = new_NYT
            old_NYT.right = new_leaf
            self.leaves[symbol] = new_leaf
            self.NYT = new_NYT
            
            self.all_nodes.append(new_NYT)
            self.all_nodes.append(new_leaf)
            
            node = old_NYT
            while node:
                leader = self._find_leader(node)
                if leader and leader != node.parent:
                    self._swap_nodes(node, leader)
                node.weight += 1
                node = node.parent


# ============================================================================
# SECCIÓN 3: UTILIDADES DE LECTURA DE BITS
# ============================================================================

class BitReader:
    """
    Clase para leer bits individuales desde un buffer de bytes.
    
    Idéntica a la clase BitReader del compresor. Permite leer datos que
    fueron escritos a nivel de bits por el BitWriter.
    
    Attributes:
        data (bytes): Datos de entrada
        pos (int): Posición actual en los datos
        bit_pos (int): Posición del bit en el byte actual
        curr (int): Byte actual siendo leído
    """
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0
        self.bit_pos = 8  # Forzar carga del primer byte
        self.curr = 0

    def _ensure_byte(self):
        """
        Asegura que hay un byte disponible para leer.
        
        Raises:
            EOFError: Si no hay más datos
        """
        if self.bit_pos == 8:
            if self.pos >= len(self.data):
                raise EOFError("Fin de datos")
            self.curr = self.data[self.pos]
            self.pos += 1
            self.bit_pos = 0

    def read_bit(self):
        """
        Lee un solo bit.
        
        Returns:
            int: Bit leído (0 o 1)
        """
        self._ensure_byte()
        bit = (self.curr >> (7 - self.bit_pos)) & 1
        self.bit_pos += 1
        return bit

    def read_bits(self, n):
        """
        Lee múltiples bits como un entero.
        
        Args:
            n (int): Número de bits a leer
        
        Returns:
            int: Valor leído
        """
        v = 0
        for _ in range(n):
            v = (v << 1) | self.read_bit()
        return v


# ============================================================================
# SECCIÓN 4: FUNCIONES DE DESCOMPRESIÓN PRINCIPAL
# ============================================================================

def huffman_adapt_decompress_bytes(data: bytes):
    """
    Descomprime bytes usando Huffman Adaptativo FGK/NYT.
    
    Esta función lee el bitstream comprimido y reconstruye los bytes
    originales. El proceso es:
    
    1. Leer header con el tamaño original
    2. Para cada byte a reconstruir:
       a. Navegar por el árbol Huffman actual siguiendo los bits
       b. Al llegar a una hoja o NYT:
          - Si es NYT: leer siguiente byte completo (8 bits)
          - Si es hoja: usar el símbolo de la hoja
       c. Actualizar el árbol Huffman (mismo método que compresor)
    3. Retornar bytes reconstruidos
    
    FORMATO DE ENTRADA:
    
     Header (4 bytes):                              
       - Tamaño original de los datos               

     Bitstream comprimido:                          
       Para cada byte original:                     
       - Camino en árbol Huffman (bits variables)  
       - Si NYT: byte completo (8 bits)             
    
    
    Args:
        data (bytes): Datos comprimidos (header + bitstream)
    
    Returns:
        bytes: Bytes descomprimidos (output LZW serializado)
    
    Raises:
        ValueError: Si los datos están incompletos
        EOFError: Si el bitstream termina inesperadamente
    
    Sincronización:
        Esta función DEBE mantener el árbol Huffman sincronizado con el
        compresor, actualizándolo exactamente de la misma manera y en el
        mismo orden para cada símbolo decodificado.
    """
    # Verificar tamaño mínimo
    if len(data) < 4:
        raise ValueError("Archivo Huffman incompleto")
    
    # ========================================
    # LEER HEADER
    # ========================================
    # Leer tamaño original (4 bytes, big-endian)
    original_size = struct.unpack('>I', data[:4])[0]
    
    # Crear lector de bits para el bitstream
    br = BitReader(data[4:])

    # ========================================
    # INICIALIZAR ÁRBOL HUFFMAN
    # ========================================
    huff = AdaptiveHuffman()
    result = []

    # ========================================
    # DECODIFICAR CADA BYTE
    # ========================================
    for _ in range(original_size):
        # Comenzar desde la raíz
        node = huff.root
        
        # Navegar por el árbol hasta llegar a una hoja o NYT
        while node.left or node.right:
            # Leer siguiente bit
            bit = br.read_bit()
            
            # Moverse en la dirección indicada
            node = node.left if bit == 0 else node.right
        
        # Llegamos a una hoja o NYT
        if node.symbol is None:
            # Es NYT: símbolo nuevo, leer byte completo (8 bits)
            symbol = br.read_bits(8)
        else:
            # Es hoja: usar el símbolo almacenado
            symbol = node.symbol
        
        # Agregar símbolo al resultado
        result.append(symbol)
        
        # CRÍTICO: Actualizar árbol (mismo orden que compresor)
        huff.update(symbol)

    return bytes(result)


def decompress(input_file, output_file):
    """
    Función principal de descompresión - Ejecuta pipeline completo inverso.
    
    PIPELINE DE DESCOMPRESIÓN:
    
     1. LECTURA                                                      
        - Lee archivo comprimido (.comp)                            

     2. DESCOMPRESIÓN HUFFMAN                                        
        - Reconstruye árbol Huffman dinámicamente                   
        - Decodifica bitstream para obtener output LZW              
     3. DESERIALIZACIÓN LZW                                          
        - Extrae diccionario y códigos del output LZW               
     4. DESCOMPRESIÓN LZW                                            
        - Reconstruye diccionario                                   
        - Decodifica códigos LZW                                    
     5. ESCRITURA                                                    
        - Escribe archivo descomprimido (idéntico al original)     
    
    
    Args:
        input_file (str): Ruta del archivo comprimido (.comp)
        output_file (str): Ruta del archivo de salida descomprimido
    
    Raises:
        FileNotFoundError: Si el archivo de entrada no existe
        ValueError: Si el archivo está corrupto o incompleto
        IOError: Si hay problemas de lectura/escritura
    
    Garantías:
        - El archivo descomprimido es IDÉNTICO byte por byte al original
        - No se pierde ni se corrompe información en el proceso
    """
    # ========================================
    # ETAPA 1: LECTURA
    # ========================================
    with open(input_file, 'rb') as f:
        data = f.read()

    # ========================================
    # ETAPA 2: DESCOMPRESIÓN HUFFMAN
    # ========================================
    # Descomprimir Huffman para obtener el output de LZW serializado
    lzw_output = huffman_adapt_decompress_bytes(data)
    
    # ========================================
    # ETAPA 3: DESERIALIZACIÓN LZW
    # ========================================
    # Deserializar output de LZW para obtener diccionario y códigos
    codes, parent_bytes = deserialize_lzw_output(lzw_output)
    
    # ========================================
    # ETAPA 4: DESCOMPRESIÓN LZW
    # ========================================
    # Descomprimir LZW usando códigos y diccionario
    original = lzw_decompress(codes, parent_bytes)

    # ========================================
    # ETAPA 5: ESCRITURA
    # ========================================
    # Escribir datos originales reconstruidos
    with open(output_file, 'wb') as f:
        f.write(original)

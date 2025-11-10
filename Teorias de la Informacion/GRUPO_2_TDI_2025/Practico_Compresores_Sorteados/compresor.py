"""
===============================================================================
MÓDULO DE COMPRESIÓN - LZW + HUFFMAN ADAPTATIVO
===============================================================================

Este módulo implementa un sistema de compresión en dos etapas:

ETAPA 1: Compresión LZW (Lempel-Ziv-Welch)
    - Algoritmo de compresión basado en diccionarios
    - Genera un diccionario dinámico de secuencias repetidas
    - Produce una secuencia de códigos que representan estas secuencias
    - Tamaño de diccionario limitado a 1024 entradas (códigos de 12 bits)

ETAPA 2: Compresión Huffman Adaptativa (FGK/NYT)
    - Algoritmo de compresión estadística con árbol dinámico
    - No requiere pasar dos veces sobre los datos
    - Utiliza el algoritmo FGK (Faller-Gallager-Knuth) con nodo NYT
    - Comprime el output completo de LZW (diccionario + códigos)

FORMATO DEL ARCHIVO COMPRIMIDO:
    - Solo contiene el flujo Huffman comprimido
    - El flujo Huffman contiene internamente el output LZW serializado
    - El output LZW contiene: diccionario + códigos

Autor: Grupo 2 - Teorías de la Información 2025
Fecha: Noviembre 2025
===============================================================================
"""

import struct

# ============================================================================
# SECCIÓN 1: COMPRESIÓN LZW (LEMPEL-ZIV-WELCH)
# ============================================================================

def lzw_compress(data: bytes):
    """
    Comprime datos usando el algoritmo LZW con diccionario limitado.
    
    El algoritmo LZW funciona:
    1. Inicializa el diccionario con todos los bytes posibles (0-255)
    2. Lee secuencias de bytes cada vez más largas
    3. Cuando encuentra una secuencia no vista, emite el código de la
       secuencia anterior y agrega la nueva secuencia al diccionario
    4. Continúa hasta procesar todos los datos
    
    Args:
        data (bytes): Datos de entrada a comprimir
    
    Returns:
        tuple: (codes, parent_bytes)
            - codes (list): Lista de códigos LZW (enteros)
            - parent_bytes (list): Lista de tuplas (parent_idx, new_byte)
                                  que representa el diccionario generado
    
    Características:
        - Diccionario limitado a 1024 entradas (MAX_DICT_SIZE)
        - Códigos de 12 bits (pueden representar 0-4095)
        - Cuando el diccionario se llena, deja de crecer
    """
    # Límite del diccionario: 1024 entradas (deja espacio para Huffman)
    MAX_DICT_SIZE = 1024
    
    # Tamaño inicial del diccionario: 256 (todos los bytes posibles)
    dict_size = 256
    
    # Inicializar diccionario con todos los bytes individuales (0-255)
    dictionary = {bytes([i]): i for i in range(256)}

    # Lista para guardar el diccionario generado: (parent_idx, new_byte)
    parent_bytes = []
    
    # Lista de códigos de salida
    codes = []
    
    # Secuencia actual siendo procesada
    w = b''
    
    # Procesar cada byte de los datos de entrada
    for byte in data:
        c = bytes([byte])  # Convertir byte a bytes
        wc = w + c  # Concatenar secuencia actual con nuevo byte
        
        # Si la secuencia wc ya está en el diccionario
        if wc in dictionary:
            # Extender la secuencia actual
            w = wc
        else:
            # La secuencia wc NO está en el diccionario
            
            # Emitir el código de la secuencia actual w
            codes.append(dictionary[w])
            
            # Guardar entrada del diccionario para reconstrucción
            parent_idx = dictionary[w]
            parent_bytes.append((parent_idx, byte))
            
            # Agregar la nueva secuencia wc al diccionario si hay espacio
            if dict_size < MAX_DICT_SIZE:
                dictionary[wc] = dict_size
                dict_size += 1
            
            # Comenzar nueva secuencia con el byte actual
            w = c
    
    # Emitir el código de la última secuencia
    if w:
        codes.append(dictionary[w])

    return codes, parent_bytes


def serialize_lzw_output(codes, parent_bytes):
    """
    Serializa el output completo de LZW en un formato binario compacto.
    
    Esta función convierte el diccionario y los códigos LZW en una
    secuencia de bytes que puede ser almacenada o procesada posteriormente.
    
    FORMATO DE SERIALIZACIÓN:
    
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
        codes (list): Lista de códigos LZW
        parent_bytes (list): Lista de tuplas (parent_idx, new_byte)
    
    Returns:
        bytes: Datos serializados listos para escribir o comprimir
    """
    buf = bytearray()
    
    # 1. Header: número de entradas del diccionario (2 bytes, big-endian)
    buf.extend(struct.pack('>H', len(parent_bytes)))
    
    # 2. Diccionario: cada entrada es (parent_idx: 2 bytes, new_byte: 1 byte)
    for parent_idx, new_byte in parent_bytes:
        buf.extend(struct.pack('>H', parent_idx))  # parent_idx: 2 bytes
        buf.append(new_byte)  # new_byte: 1 byte
    
    # 3. Número de códigos (4 bytes, big-endian)
    buf.extend(struct.pack('>I', len(codes)))
    
    # 4. Códigos comprimidos (12 bits fijos cada uno)
    bw = BitWriter()
    for code in codes:
        bw.write_bits(code, 12)  # Cada código usa exactamente 12 bits
    buf.extend(bw.finish())
    
    return bytes(buf)


# ============================================================================
# SECCIÓN 2: HUFFMAN ADAPTATIVO (FGK/NYT)
# ============================================================================

class HuffmanNode:
    """
    Nodo del árbol Huffman adaptativo.
    
    El árbol Huffman adaptativo es un árbol binario que se ajusta dinámicamente
    a medida que procesa los datos. Cada nodo puede ser:
    - Nodo interno: tiene hijos izquierdo y derecho
    - Nodo hoja: representa un símbolo específico
    - Nodo NYT (Not Yet Transmitted): marca símbolos aún no vistos
    
    Attributes:
        symbol (int|None): Símbolo representado (None para nodos internos/NYT)
        weight (int): Frecuencia acumulada (número de veces que aparece)
        parent (HuffmanNode|None): Nodo padre en el árbol
        left (HuffmanNode|None): Hijo izquierdo
        right (HuffmanNode|None): Hijo derecho
        order (int): Orden del nodo (usado en algoritmo FGK para swaps)
    """
    def __init__(self, symbol=None, weight=0, parent=None, order=0):
        self.symbol = symbol  # None para nodos internos o NYT
        self.weight = weight  # Frecuencia del nodo
        self.parent = parent  # Padre en el árbol
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
        self.order = order  # Orden para el algoritmo FGK


class AdaptiveHuffman:
    """
    Implementación del algoritmo Huffman Adaptativo (FGK/NYT).
    
    Este algoritmo construye y mantiene un árbol Huffman dinámico que se
    actualiza a medida que procesa cada símbolo. Las características principales:
    
    - No requiere conocer las frecuencias de antemano (una sola pasada)
    - Utiliza un nodo especial NYT (Not Yet Transmitted) para símbolos nuevos
    - Mantiene la propiedad sibling (hermanos con pesos similares)
    - Implementa swapping de nodos para mantener el árbol balanceado
    
    El algoritmo FGK garantiza que el compresor y descompresor mantengan
    árboles idénticos si siguen el mismo proceso de actualización.
    
    Attributes:
        next_order (int): Siguiente orden disponible para nuevos nodos
        NYT (HuffmanNode): Nodo especial para símbolos no vistos
        root (HuffmanNode): Raíz del árbol Huffman
        leaves (dict): Mapeo de símbolos a sus nodos hoja
        all_nodes (list): Lista de todos los nodos para búsquedas rápidas
    """
    def __init__(self):
        # Orden inicial alto, se decrementa para nuevos nodos
        self.next_order = 512
        
        # Crear nodo NYT inicial (representa símbolos no vistos)
        self.NYT = HuffmanNode(symbol=None, weight=0, order=self.next_order)
        self.next_order -= 1
        
        # El árbol comienza con solo el nodo NYT
        self.root = self.NYT
        
        # Diccionario para acceso rápido a hojas por símbolo
        self.leaves = {}
        
        # Lista de todos los nodos para el algoritmo de bloques
        self.all_nodes = [self.NYT]

    def _find_leader(self, node):
        """
        Encuentra el líder del bloque para un nodo dado.
        
        En el algoritmo FGK, los nodos con el mismo peso forman un "bloque".
        El líder del bloque es el nodo con el mayor orden en ese bloque.
        Esto es importante para mantener la propiedad sibling del árbol.
        
        Args:
            node (HuffmanNode): Nodo para el cual buscar el líder
        
        Returns:
            HuffmanNode|None: Líder del bloque, o None si no hay uno
        
        Condiciones:
            - Debe tener el mismo peso que el nodo
            - Debe tener mayor orden que el nodo
            - No puede ser el padre del nodo
        """
        # Buscar nodo con mismo peso y mayor orden
        max_order = -1
        leader = None
        for n in self.all_nodes:
            # Verificar condiciones del líder
            if n.weight == node.weight and n.order > node.order and n != node.parent:
                if n.order > max_order:
                    max_order = n.order
                    leader = n
        return leader

    def _swap_nodes(self, a, b):
        """
        Intercambia dos nodos en el árbol Huffman.
        
        El swap de nodos es fundamental en el algoritmo FGK para mantener
        la propiedad sibling. Cuando un nodo aumenta su peso, puede necesitar
        intercambiarse con el líder de su bloque.
        
        Este método intercambia:
        - Las posiciones en el árbol (actualiza padres e hijos)
        - Los valores de orden
        - Las referencias en el diccionario de hojas
        - La raíz si es necesario
        
        Args:
            a (HuffmanNode): Primer nodo a intercambiar
            b (HuffmanNode): Segundo nodo a intercambiar
        """
        # Guardar padres originales
        a_parent = a.parent
        b_parent = b.parent
        
        # Actualizar referencias en el padre de 'a'
        if a_parent:
            if a_parent.left == a:
                a_parent.left = b
            else:
                a_parent.right = b
        
        # Actualizar referencias en el padre de 'b'
        if b_parent:
            if b_parent.left == b:
                b_parent.left = a
            else:
                b_parent.right = a
        
        # Intercambiar padres
        a.parent, b.parent = b_parent, a_parent
        
        # Intercambiar órdenes (importante para FGK)
        a.order, b.order = b.order, a.order
        
        # Actualizar raíz si es necesario
        if self.root == a:
            self.root = b
        elif self.root == b:
            self.root = a
        
        # Actualizar diccionario de hojas si los nodos son hojas
        if a.symbol is not None:
            self.leaves[a.symbol] = a
        if b.symbol is not None:
            self.leaves[b.symbol] = b

    def update(self, symbol):
        """
        Actualiza el árbol Huffman después de procesar un símbolo.
        
        Este es el corazón del algoritmo Huffman adaptativo. Hay dos casos:
        
        CASO 1: Símbolo ya visto (existe en el árbol)
            - Encuentra la hoja del símbolo
            - Incrementa pesos desde la hoja hasta la raíz
            - Realiza swaps con líderes de bloque cuando sea necesario
        
        CASO 2: Símbolo nuevo (no existe en el árbol)
            - Divide el nodo NYT en dos hijos:
                * Nuevo nodo NYT (izquierdo)
                * Nueva hoja para el símbolo (derecho)
            - Incrementa pesos desde el padre de la nueva hoja hasta la raíz
        
        Args:
            symbol (int): Símbolo (byte) a procesar (0-255)
        
        Proceso:
            1. Verificar si el símbolo ya existe
            2. Si existe: actualizar pesos subiendo por el árbol
            3. Si no existe: crear nueva hoja y nuevo NYT
            4. Realizar swaps necesarios para mantener propiedad sibling
        """
        if symbol in self.leaves:
            # CASO 1: Símbolo ya visto - incrementar desde su hoja
            node = self.leaves[symbol]
            
            # Subir por el árbol hasta la raíz
            while node:
                # Buscar líder del bloque actual
                leader = self._find_leader(node)
                
                # Si hay líder y no es el padre, intercambiar
                if leader and leader != node.parent:
                    self._swap_nodes(node, leader)
                
                # Incrementar peso del nodo
                node.weight += 1
                
                # Subir al padre
                node = node.parent
        else:
            # CASO 2: Símbolo nuevo - dividir NYT
            old_NYT = self.NYT
            
            # Crear nuevo nodo NYT (hijo izquierdo)
            new_NYT = HuffmanNode(symbol=None, weight=0, parent=old_NYT, order=self.next_order)
            self.next_order -= 1
            
            # Crear nueva hoja para el símbolo (hijo derecho)
            new_leaf = HuffmanNode(symbol=symbol, weight=0, parent=old_NYT, order=self.next_order)
            self.next_order -= 1
            
            # Conectar hijos al antiguo NYT
            old_NYT.left = new_NYT
            old_NYT.right = new_leaf
            
            # Actualizar referencias
            self.leaves[symbol] = new_leaf
            self.NYT = new_NYT
            
            # Agregar nuevos nodos a la lista
            self.all_nodes.append(new_NYT)
            self.all_nodes.append(new_leaf)
            
            # Incrementar pesos desde el padre de la nueva hoja
            node = old_NYT
            while node:
                # Buscar líder del bloque
                leader = self._find_leader(node)
                
                # Realizar swap si es necesario
                if leader and leader != node.parent:
                    self._swap_nodes(node, leader)
                
                # Incrementar peso
                node.weight += 1
                
                # Subir al padre
                node = node.parent

    def _path_to_node(self, node):
        """
        Obtiene el camino desde la raíz hasta un nodo específico.
        
        El camino se representa como una secuencia de bits:
        - 0 = ir al hijo izquierdo
        - 1 = ir al hijo derecho
        
        Args:
            node (HuffmanNode): Nodo destino
        
        Returns:
            list: Lista de bits (0s y 1s) que representa el camino
        
        Ejemplo:
            Si el camino es [0, 1, 0], significa:
            raíz -> izquierda -> derecha -> izquierda -> nodo
        """
        path = []
        # Subir desde el nodo hasta la raíz, guardando direcciones
        while node.parent:
            if node.parent.left is node:
                path.append(0)  # Nodo es hijo izquierdo
            else:
                path.append(1)  # Nodo es hijo derecho
            node = node.parent
        
        # Invertir porque construimos de hoja a raíz
        path.reverse()
        return path

    def get_path_for(self, symbol):
        """
        Obtiene el camino para codificar un símbolo.
        
        Args:
            symbol (int): Símbolo a codificar (0-255)
        
        Returns:
            tuple: (path, is_new)
                - path (list): Camino de bits hacia el nodo
                - is_new (bool): True si el símbolo es nuevo (no visto)
        
        Comportamiento:
            - Si el símbolo ya fue visto: retorna camino a su hoja
            - Si el símbolo es nuevo: retorna camino al nodo NYT
              (el símbolo real se enviará después en 8 bits)
        """
        if symbol in self.leaves:
            # Símbolo visto: camino a su hoja
            return self._path_to_node(self.leaves[symbol]), False
        else:
            # Símbolo nuevo: camino a NYT
            return self._path_to_node(self.NYT), True


# ============================================================================
# SECCIÓN 3: UTILIDADES DE LECTURA/ESCRITURA DE BITS
# ============================================================================

class BitWriter:
    """
    Clase para escribir bits individuales en un buffer de bytes.
    
    Esta clase permite escribir datos a nivel de bits, lo cual es esencial
    para algoritmos de compresión que necesitan empaquetar datos en menos
    de 8 bits por símbolo.
    
    Funcionamiento:
        - Acumula bits en un byte temporal
        - Cuando se completa un byte (8 bits), lo escribe al buffer
        - Al finalizar, escribe el byte parcial con padding si es necesario
    
    Attributes:
        buf (bytearray): Buffer donde se acumulan los bytes completos
        byte (int): Byte temporal para acumular bits
        nbits (int): Número de bits acumulados en el byte temporal
    
    Ejemplo de uso:
        writer = BitWriter()
        writer.write_bit(1)
        writer.write_bit(0)
        writer.write_bits(5, 3)  # Escribe 101 (5 en binario, 3 bits)
        data = writer.finish()
    """
    def __init__(self):
        self.buf = bytearray()  # Buffer de salida
        self.byte = 0  # Byte temporal
        self.nbits = 0  # Bits en el byte temporal

    def write_bit(self, bit):
        """
        Escribe un solo bit.
        
        Args:
            bit (int): Bit a escribir (0 o 1)
        """
        # Desplazar byte a la izquierda y agregar nuevo bit
        self.byte = (self.byte << 1) | (1 if bit else 0)
        self.nbits += 1
        
        # Si completamos un byte, escribirlo al buffer
        if self.nbits == 8:
            self.buf.append(self.byte & 0xFF)
            self.byte = 0
            self.nbits = 0

    def write_bits(self, value, nbits):
        """
        Escribe múltiples bits de un valor entero.
        
        Args:
            value (int): Valor a escribir
            nbits (int): Número de bits a escribir (de los bits menos significativos)
        
        Ejemplo:
            write_bits(5, 3) escribe 101 (5 en binario, usando 3 bits)
        """
        # Escribir bits de más significativo a menos significativo
        for i in range(nbits - 1, -1, -1):
            # Extraer bit i-ésimo y escribirlo
            self.write_bit((value >> i) & 1)

    def finish(self):
        """
        Finaliza la escritura y retorna los bytes escritos.
        
        Si hay bits pendientes (byte incompleto), los escribe con padding
        de ceros a la derecha.
        
        Returns:
            bytes: Todos los datos escritos como bytes
        """
        # Si hay bits pendientes, completar con ceros
        if self.nbits > 0:
            self.byte <<= (8 - self.nbits)  # Padding con ceros a la derecha
            self.buf.append(self.byte & 0xFF)
        return bytes(self.buf)

# ============================================================================
# SECCIÓN 4: FUNCIONES DE COMPRESIÓN PRINCIPAL
# ============================================================================

def compress_huff_adapt_nyt_on_bytes(data_bytes):
    """
    Comprime bytes usando Huffman Adaptativo FGK/NYT.
    
    Esta función aplica compresión Huffman adaptativa sobre una secuencia
    de bytes. Para cada byte:
    1. Obtiene el camino en el árbol Huffman actual
    2. Escribe el camino como secuencia de bits
    3. Si es un símbolo nuevo, escribe el byte completo (8 bits)
    4. Actualiza el árbol Huffman
    
    FORMATO DE SALIDA:
    
     Header (4 bytes):                              
       - Tamaño original de data_bytes              

     Bitstream comprimido:                          
       Para cada byte en data_bytes:                
       - Camino en árbol Huffman (bits variables)  
       - Si nuevo: byte completo (8 bits)           
    
    
    Args:
        data_bytes (bytes): Datos a comprimir
    
    Returns:
        bytes: Datos comprimidos (header + bitstream Huffman)
    
    Características:
        - No requiere pasar dos veces sobre los datos
        - Árbol se construye dinámicamente durante la compresión
        - Tamaño original incluido para facilitar descompresión
    """
    # Inicializar árbol Huffman adaptativo
    huff = AdaptiveHuffman()
    
    # Inicializar escritor de bits
    bw = BitWriter()
    
    # Header: escribir tamaño original (4 bytes = 32 bits)
    bw.write_bits(len(data_bytes), 32)

    # Procesar cada byte
    for byte_val in data_bytes:
        # Obtener camino en el árbol Huffman actual
        path, is_new = huff.get_path_for(byte_val)
        
        # Escribir camino como bits
        for b in path:
            bw.write_bit(b)
        
        # Si es símbolo nuevo, escribir su valor (8 bits)
        if is_new:
            bw.write_bits(byte_val, 8)
        
        # Actualizar árbol Huffman (importante: mismo orden que descompresor)
        huff.update(byte_val)

    return bw.finish()


def compress(input_file, output_file):
    """
    Función principal de compresión - Ejecuta pipeline completo LZW + Huffman.
    
    PIPELINE DE COMPRESIÓN:
    
    1. LECTURA
       - Lee archivo de entrada en modo binario             
    
    2. COMPRESIÓN LZW                                        
       - Genera diccionario de secuencias repetidas         
       - Produce códigos LZW (12 bits cada uno)             
       - Serializa diccionario + códigos                    
    
    3. COMPRESIÓN HUFFMAN                                    
       - Aplica Huffman adaptativo sobre output LZW completo
       - Produce bitstream comprimido final                 
    
    4. ESCRITURA                                             
       - Escribe archivo comprimido (.comp)                 
    
    
    Args:
        input_file (str): Ruta del archivo a comprimir
        output_file (str): Ruta del archivo de salida (.comp)
    
    Returns:
        int: Tamaño final del archivo comprimido en bytes
    
    Raises:
        FileNotFoundError: Si el archivo de entrada no existe
        IOError: Si hay problemas de lectura/escritura
    
    Métricas mostradas:
        - Tamaño original
        - Tamaño después de LZW
        - Tamaño final después de Huffman
        - Porcentajes de reducción en cada etapa
    """
    # ========================================
    # ETAPA 1: LECTURA
    # ========================================
    print("Etapa 1: Leyendo el archivo de entrada...")
    with open(input_file, 'rb') as f:
        data = f.read()
    original_size = len(data)
    print(f"Tamaño original: {original_size} bytes")

    # ========================================
    # ETAPA 2: COMPRESIÓN LZW
    # ========================================
    print("Etapa 2: Aplicando compresión LZW...")
    # Comprimir con LZW y obtener códigos + diccionario
    codes, parent_bytes = lzw_compress(data)
    
    # Serializar el output completo de LZW
    lzw_output = serialize_lzw_output(codes, parent_bytes)
    
    # Calcular métricas de LZW
    lzw_size = len(lzw_output)
    red_lzw = (1 - lzw_size / original_size) * 100 if original_size > 0 else 0.0
    print(f"Tamaño después de LZW (diccionario + códigos): {lzw_size} bytes")
    print(f"Porcentaje de reducción en LZW: {red_lzw:.2f}%")

    # ========================================
    # ETAPA 3: COMPRESIÓN HUFFMAN
    # ========================================
    print("Etapa 3: Aplicando compresión Huffman adaptativa sobre el output de LZW...")
    # Comprimir TODO el output de LZW con Huffman adaptativo
    huff_stream = compress_huff_adapt_nyt_on_bytes(lzw_output)

    # El archivo final contiene solo el flujo Huffman
    final_output = huff_stream
    final_size = len(final_output)

    # Calcular métricas finales
    huff_payload_bytes = len(huff_stream) - 4  # Restar 4 bytes del header
    red_huff = (1 - (huff_payload_bytes / lzw_size)) * 100 if lzw_size > 0 else 0.0
    total_reduction = (1 - final_size / original_size) * 100 if original_size > 0 else 0.0

    print(f"Tamaño final después de Huffman: {final_size} bytes")
    print(f"Porcentaje de reducción en Huffman (vs LZW output): {red_huff:.2f}%")
    print(f"Porcentaje de reducción total: {total_reduction:.2f}%")

    # ========================================
    # ETAPA 4: ESCRITURA
    # ========================================
    print("Etapa 4: Escribiendo el archivo comprimido...")
    with open(output_file, 'wb') as f:
        f.write(final_output)
    print("Compresión completada.")
    
    return final_size

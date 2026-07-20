# Resumen práctico — Listas definidas por el programador (POO)

> Pensado para repasar antes del recuperatorio. Convención usada en los Ejercicios 6, 7 y 8 del Práctico 3 (clase `Nodo` + clase `Lista` con `__comienzo` y `__siguiente`).

---

## 0. Regla de oro del profesor (NO romper encapsulamiento)

**Romper encapsulamiento = sacar el objeto de la lista hacia afuera.**

Por eso están **prohibidos**:

- `return self.__comienzo` — entregás la cabeza.
- `return nodo` — entregás un Nodo entero.
- `return nodo.getDato()` (o cualquier `return objeto`) hecho desde la Lista hacia el `Main` — entregás el objeto que vive adentro.

Regla práctica: **la operación se resuelve adentro de la Lista**. La Lista puede devolver tipos primitivos (`int`, `bool`, `str`, `float`), imprimir, o recibir un colaborador (ej. un `objectEncoder`) para delegar. Nunca devuelve el objeto contenido.

---

## 1. Estructura mínima

Dos clases:

1. **`Nodo`**: contiene un objeto (`__dato`) y un puntero al siguiente nodo (`__siguiente`).
2. **`Lista`**: contiene la referencia al primer nodo (`__comienzo`) y todos los métodos de operación.

El `Main` solo conoce a la `Lista`. **Nunca** crea, ni toca, ni recibe `Nodo`s.

```
Main  --conoce-->  Lista  --tiene-->  Nodo -> Nodo -> Nodo -> None
                                        |       |       |
                                       obj     obj     obj
```

---

## 2. Plantilla — `ClaseNodo.py`

```python
class Nodo:
    __dato = None
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__dato
```

Notas:

- `getDato()` **se usa SOLO dentro de la Lista**. No es para el `Main`.
- El atributo se llama `__dato` por convención genérica; en los ejercicios aparece como `__aparato`, `__personal`, etc. Es lo mismo.

---

## 3. Plantilla — `ClaseLista.py` (esqueleto)

```python
from ClaseNodo import Nodo

class Lista:
    __comienzo = None
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__tope = 0

    # --- alta ---
    def insertarInicio(self, objeto):
        nodo = Nodo(objeto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1

    def insertarFinal(self, objeto):
        nodo = Nodo(objeto)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            cabeza = self.__comienzo
            while cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            cabeza.setSiguiente(nodo)
        self.__tope += 1

    def insertarEnPosicion(self, pos, objeto):
        if pos <= 1 or self.__comienzo is None:
            self.insertarInicio(objeto)
            return
        cabeza = self.__comienzo
        cont = 1
        while cont < pos - 1 and cabeza.getSiguiente() is not None:
            cabeza = cabeza.getSiguiente()
            cont += 1
        nuevo = Nodo(objeto)
        nuevo.setSiguiente(cabeza.getSiguiente())
        cabeza.setSiguiente(nuevo)
        self.__tope += 1

    # --- consulta ---
    def estaVacia(self):
        return self.__comienzo is None

    def cantidad(self):
        return self.__tope
```

---

## 4. La receta universal de recorrido (memorizar)

**Cada vez que necesites recorrer la lista, copiá esto:**

```python
cabeza = self.__comienzo
while cabeza is not None:
    dato = cabeza.getDato()
    # ... operar sobre 'dato' acá adentro ...
    cabeza = cabeza.getSiguiente()
```

Tres pasos: **tomar `__comienzo`**, **mientras no sea `None`**, **avanzar con `getSiguiente()`**. Todo lo demás es relleno encima de esto.

---

## 5. Operaciones típicas (todas plantillas)

### 5.1 Listar / mostrar todo

```python
def listarTodos(self):
    cabeza = self.__comienzo
    while cabeza is not None:
        dato = cabeza.getDato()
        print(dato)                # usa __str__ del objeto
        cabeza = cabeza.getSiguiente()
```

### 5.2 Contar con condición

```python
def contarPorMarca(self, marca):
    cont = 0
    cabeza = self.__comienzo
    while cabeza is not None:
        dato = cabeza.getDato()
        if dato.getMarca().lower() == marca.lower():
            cont += 1
        cabeza = cabeza.getSiguiente()
    return cont       # devolver primitivo: OK
```

### 5.3 Buscar e informar (sin sacar el objeto)

```python
def informarPorCodigo(self, cod):
    cabeza = self.__comienzo
    encontrado = False
    while cabeza is not None and not encontrado:
        dato = cabeza.getDato()
        if dato.getCodigo() == cod:
            print("Encontrado: {}".format(dato))
            encontrado = True
        cabeza = cabeza.getSiguiente()
    if not encontrado:
        print("No existe el codigo {}".format(cod))
```

### 5.4 Modificar un atributo de un objeto que vive en la lista

```python
def modificarSueldo(self, cuil, nuevoSueldo):
    cabeza = self.__comienzo
    band = False
    while cabeza is not None and not band:
        dato = cabeza.getDato()
        if dato.getCuil() == cuil:
            dato.setSueldo(nuevoSueldo)   # mutamos por su setter
            band = True
        cabeza = cabeza.getSiguiente()
    if not band:
        print("CUIL no encontrado")
```

### 5.5 Listado ordenado (truco con lista auxiliar de Python)

> El objeto debe implementar `__lt__` o `__gt__` para que `sorted` sepa ordenarlos.

```python
def listadoOrdenado(self):
    aux = []
    cabeza = self.__comienzo
    while cabeza is not None:
        aux.append(cabeza.getDato())
        cabeza = cabeza.getSiguiente()
    for elem in sorted(aux):
        print(elem)
```

Esto NO rompe encapsulamiento: `aux` es local al método y no sale del scope de la Lista.

### 5.6 Borrar por criterio (eliminar nodo)

```python
def borrarPorCodigo(self, cod):
    if self.__comienzo is None:
        return False
    # caso 1: borra la cabeza
    if self.__comienzo.getDato().getCodigo() == cod:
        self.__comienzo = self.__comienzo.getSiguiente()
        self.__tope -= 1
        return True
    # caso 2: borra en el medio o al final
    anterior = self.__comienzo
    actual = anterior.getSiguiente()
    while actual is not None:
        if actual.getDato().getCodigo() == cod:
            anterior.setSiguiente(actual.getSiguiente())
            self.__tope -= 1
            return True
        anterior = actual
        actual = actual.getSiguiente()
    return False
```

Clave: mantener **dos punteros** (`anterior` y `actual`) y "saltar" el nodo a borrar conectando `anterior` con `actual.getSiguiente()`.

---

## 6. Lista iterable — para qué sirven `__actual`, `__indice` y `__tope`

Para que `for x in lista` funcione desde el `Main`, la Lista implementa `__iter__` / `__next__`. Estos tres atributos son el **estado del cursor interno**:

| Atributo | Para qué sirve |
|---|---|
| `__comienzo` | Referencia fija al primer nodo. **Nunca** se modifica durante una iteración. |
| `__actual` | Cursor que avanza nodo por nodo durante el `for`. Es "dónde estoy ahora". |
| `__indice` | Contador de cuántos elementos ya entregué en el `for` actual. |
| `__tope` | Cantidad total de nodos. Cuando `__indice == __tope`, terminó la iteración. |

```python
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0

    def __iter__(self):
        return self                              # la propia Lista es su iterador

    def __next__(self):
        if self.__indice == self.__tope:         # ya recorrí todo
            self.__actual = self.__comienzo      # reseteo el cursor para el proximo for
            self.__indice = 0
            raise StopIteration                  # señal de "no hay más"
        self.__indice += 1
        dato = self.__actual.getDato()
        self.__actual = self.__actual.getSiguiente()
        return dato
```

**Cómo se usa desde el `Main`:**

```python
for persona in lista:        # Python llama __iter__ una vez y __next__ N veces
    print(persona)
```

**Tres claves para no confundirse:**

1. **`__comienzo` es la cabeza permanente, `__actual` es el cursor temporal.** El recorrido manual (`while cabeza is not None`) usa una variable local llamada `cabeza`, pero `__iter__/__next__` usa el atributo `__actual` porque tiene que recordar dónde quedó entre llamadas.
2. **`__tope` se incrementa SIEMPRE que insertás y se decrementa cuando borrás.** Si te olvidás de actualizarlo, la iteración termina antes de tiempo o se cuelga.
3. **`raise StopIteration` no es un error**, es la forma estándar de Python de decir "se terminó el `for`".

**Limitación a tener presente:** como hay UN solo cursor compartido, si hacés dos `for` anidados sobre la misma lista los cursores se pisan. Para esos casos, mejor recorrer manualmente con la receta del punto 4.

> Nota de encapsulamiento: técnicamente `__next__` SÍ entrega el objeto al `Main`. Algunos profes lo aceptan como protocolo Python; otros no. Si te lo piden, úsalo. Si no, mantené todas las operaciones dentro de la Lista.

---

## 7. Cómo se usa desde `Main.py`

```python
from ClaseLista import Lista
from ClasePersona import Persona

lista = Lista()
lista.insertarFinal(Persona("Ana", 30))
lista.insertarFinal(Persona("Beto", 25))

lista.listarTodos()
print("Cantidad:", lista.cantidad())
lista.modificarEdad("Ana", 31)
lista.borrarPorNombre("Beto")
```

El `Main` **nunca** ve un `Nodo`. Solo llama métodos de `Lista` y le pasa objetos del dominio (`Persona`, `Aparato`, `Personal`, etc.).

---

## 8. Checklist de encapsulamiento (revisalo antes de entregar)

- [ ] Todos los atributos de `Nodo` y `Lista` empiezan con `__` (doble guion bajo).
- [ ] Ningún método de `Lista` hace `return self.__comienzo`.
- [ ] Ningún método de `Lista` hace `return` de un `Nodo`.
- [ ] Ningún método de `Lista` hace `return` del objeto contenido para que el `Main` lo use.
- [ ] Si necesito mostrar, **imprimo dentro** de la Lista.
- [ ] Si necesito ordenar, uso lista auxiliar **dentro** del método.
- [ ] Si necesito modificar, recibo los datos y llamo al setter del objeto **dentro** del método.
- [ ] El `Main` solo importa la clase de dominio y `Lista`. Nunca `Nodo`.

---

## 9. Combinando con HERENCIA (caso del Ejercicio 7 y 8)

La lista guarda objetos de **distinto tipo** que comparten una superclase:

```
Personal (abstracta)
 ├── Docente
 ├── Investigador
 ├── DocenteInvestigador (Docente, Investigador)
 └── PersonalApoyo
```

### 9.1 Polimorfismo dentro del recorrido

Cada subclase redefine (`override`) un método. Llamás al método de la superclase y Python resuelve cuál usar:

```python
def actualizarSueldos(self):
    cabeza = self.__comienzo
    while cabeza is not None:
        dato = cabeza.getDato()
        dato.calculaSueldo()       # polimorfismo: cada clase calcula a su manera
        cabeza = cabeza.getSiguiente()
```

### 9.2 Filtrar por tipo concreto

```python
def contarPorTipo(self):
    docentes = 0
    invest = 0
    cabeza = self.__comienzo
    while cabeza is not None:
        dato = cabeza.getDato()
        if type(dato) is DocenteInvestigador:
            docentes += 1
        elif type(dato) is Investigador:
            invest += 1
        cabeza = cabeza.getSiguiente()
    print("DocInv:", docentes, "Invest:", invest)
```

- `type(dato) is Clase` → match exacto (no incluye subclases).
- `isinstance(dato, Clase)` → match incluyendo subclases. Útil cuando querés agrupar "todo lo que sea Docente, incluido DocenteInvestigador".

### 9.3 Plantilla de subclase

```python
from ClasePersonal import Personal

class Docente(Personal):
    __cargo: str

    def __init__(self, **kwargs):
        self.__cargo = kwargs["cargo"]
        super().__init__(**kwargs)     # delega atributos comunes al padre

    def calculaSueldo(self):           # override
        total = self.getSueldo()
        # ... lógica propia ...
        self.setSueldo(total)
```

Conceptos a tener claros:

- **`super().__init__(...)`**: invoca el constructor del padre. Imprescindible para que se inicialicen los atributos heredados.
- **Override**: redefinir un método del padre con la misma firma.
- **Abstracta**: en `Personal`, los métodos `calculaSueldo` y `getTipoAgente` son `pass` para forzar que las subclases los implementen.
- **Herencia múltiple** (`DocenteInvestigador(Docente, Investigador)`): el orden importa. Python usa MRO (Method Resolution Order) — primero busca en `Docente`, después en `Investigador`.

---

## 10. Composición vs Agregación — con plantillas

Las dos significan "un objeto contiene a otro", pero se diferencian en **el ciclo de vida** de las partes.

### Diferencia conceptual

| Criterio | Composición | Agregación |
|---|---|---|
| ¿Quién crea las partes? | El todo, adentro suyo | Vienen ya creadas desde afuera |
| ¿Pueden existir sin el todo? | NO | SÍ |
| Si destruyo el todo… | …las partes mueren con él | …las partes siguen vivas |
| Ejemplo típico | Casa–Habitación, Libro–Capítulo | Universidad–Profesor, Equipo–Jugador |
| UML | Rombo **lleno** (◆) del lado del todo | Rombo **vacío** (◇) del lado del todo |

Regla mnemónica para el código:

- **Composición** → el constructor del todo **construye** las partes a partir de datos crudos.
- **Agregación** → un método del todo **recibe** las partes ya construidas por parámetro.

---

### 10.1 Plantilla de COMPOSICIÓN

Caso: una `Factura` tiene `Items`. Los items no tienen sentido fuera de la factura: cuando la factura se borra, sus items también. El constructor de `Factura` recibe **datos crudos** y crea los `Item` adentro.

**`ClaseItem.py`**

```python
class Item:
    __descripcion: str
    __precio: float

    def __init__(self, descripcion, precio):
        self.__descripcion = descripcion
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def __str__(self):
        return "Item: {} - ${}".format(self.__descripcion, self.__precio)
```

**`ClaseFactura.py`** (composición — la lista de items NACE adentro)

```python
from ClaseLista import Lista
from ClaseItem import Item

class Factura:
    __numero: int
    __items: Lista          # composición: lista definida por el programador

    def __init__(self, numero, datosItems):
        self.__numero = numero
        self.__items = Lista()                # 1) creo la lista vacía
        for d in datosItems:                  # 2) construyo cada Item desde datos crudos
            item = Item(d["desc"], d["precio"])
            self.__items.insertarFinal(item)

    def total(self):                          # operación interna, no expone los items
        suma = 0
        # truco para no exponer: la propia Factura le pide a la Lista que sume.
        # Si Lista no tiene "sumarPrecios", la agregamos como método ahi adentro.
        return self.__items.sumarPrecios()

    def mostrar(self):
        print("Factura N°{}".format(self.__numero))
        self.__items.listarTodos()
```

**Uso desde `Main.py`:**

```python
datos = [
    {"desc": "Lapicera", "precio": 100},
    {"desc": "Cuaderno", "precio": 500},
]
f = Factura(1, datos)        # los Item NO existen antes de esta linea
f.mostrar()
print("Total:", f.total())
```

Lo clave: el `Main` **nunca crea un `Item` a mano**. La `Factura` los construye en su `__init__` a partir de datos primitivos. Sin Factura, no hay Item.

---

### 10.2 Plantilla de AGREGACIÓN

Caso: un `Equipo` tiene `Jugadores`. Los jugadores existen antes de pertenecer al equipo y pueden cambiar de equipo. Los `Jugador` se construyen en otro lado y se le **pasan** al equipo.

**`ClaseJugador.py`**

```python
class Jugador:
    __nombre: str
    __dni: str

    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    def getDni(self):
        return self.__dni

    def __str__(self):
        return "Jugador: {} (DNI {})".format(self.__nombre, self.__dni)
```

**`ClaseEquipo.py`** (agregación — recibe Jugadores ya creados)

```python
from ClaseLista import Lista

class Equipo:
    __nombre: str
    __jugadores: Lista

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugadores = Lista()        # contenedor vacio

    def agregarJugador(self, jugador):    # llega YA CREADO desde afuera
        self.__jugadores.insertarFinal(jugador)

    def mostrar(self):
        print("Equipo: {}".format(self.__nombre))
        self.__jugadores.listarTodos()
```

**Uso desde `Main.py`:**

```python
# los jugadores se crean ANTES del equipo y existen por su cuenta
j1 = Jugador("Messi", "111")
j2 = Jugador("Di Maria", "222")

equipoA = Equipo("Argentina")
equipoA.agregarJugador(j1)        # le paso el jugador YA construido
equipoA.agregarJugador(j2)

# si manana borro equipoA, j1 y j2 siguen existiendo
equipoB = Equipo("PSG")
equipoB.agregarJugador(j1)        # el mismo jugador en otro equipo
```

Lo clave: el `Main` crea los `Jugador` por separado. El equipo es solo un **contenedor** que los referencia.

---

### 10.3 ¿Y dónde está cada caso en tu Práctico 3?

| Ejercicio | Relación | Tipo | Por qué |
|---|---|---|---|
| Ej. 1 — Facultad/Carrera | Facultad tiene carreras | Composición | Cada Facultad construye su propia lista de Carreras en `__init__`. Una Carrera no tiene sentido fuera de su Facultad. |
| Ej. 3 — Equipo/Jugador/Contrato | Equipo tiene contratos | Agregación | El equipo recibe contratos vía `agregarContrato(...)`. Los contratos viven en su propio Manejador. |

Cuando rindas, **mirá el constructor**:

- ¿Hace `self.__partes = [Parte(dato1), Parte(dato2)]` o las construye en un loop? → **composición**.
- ¿Solo hace `self.__partes = Lista()` y después aparece un método `agregarParte(parte)`? → **agregación**.

---

## 11. Tabla resumen para repasar de memoria

| Pregunta | Respuesta corta |
|---|---|
| ¿Cómo recorro la lista? | `cabeza = self.__comienzo` → `while cabeza is not None` → `cabeza = cabeza.getSiguiente()` |
| ¿Cómo accedo al objeto? | `dato = cabeza.getDato()` — **adentro** de la Lista |
| ¿Cómo inserto al inicio? | `nodo.setSiguiente(self.__comienzo); self.__comienzo = nodo` |
| ¿Cómo inserto al final? | Avanzar hasta `getSiguiente() is None` y enganchar |
| ¿Cómo borro? | Dos punteros (`anterior`, `actual`), saltar el nodo |
| ¿Cómo ordeno? | Vuelco a lista auxiliar local, `sorted(aux)`, recorro |
| ¿Cómo distingo subtipos? | `type(dato) is Clase` o `isinstance(dato, Clase)` |
| ¿Qué NO devuelvo nunca? | `__comienzo`, un `Nodo`, ni el objeto contenido |
| ¿Qué SÍ devuelvo? | Primitivos (`int`, `bool`, `str`), o nada (imprimo adentro) |
| ¿Composición o agregación? | ¿La parte nace adentro? → composición. ¿Llega de afuera? → agregación |

---

## 12. Plantilla mínima lista para copiar en el examen

**`ClaseNodo.py`**

```python
class Nodo:
    __dato = None
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__dato
```

**`ClaseLista.py`**

```python
from ClaseNodo import Nodo

class Lista:
    __comienzo = None
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__tope = 0

    def insertarFinal(self, objeto):
        nodo = Nodo(objeto)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            cabeza = self.__comienzo
            while cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            cabeza.setSiguiente(nodo)
        self.__tope += 1

    def listarTodos(self):
        cabeza = self.__comienzo
        while cabeza is not None:
            print(cabeza.getDato())
            cabeza = cabeza.getSiguiente()

    def cantidad(self):
        return self.__tope
```

Con esto solo, ya tenés base para insertar, mostrar y contar. El resto son variantes del **mismo recorrido**.

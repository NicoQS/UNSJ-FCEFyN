# Ejercicio 14 - Timestamp ordering, optimista hacia atras y 2PC

## Datos

Marcas de tiempo de transacciones:

| Transaccion | Marca |
|---|---:|
| `T` | 10 |
| `U` | 12 |

Marcas de lectura:

| Objeto | `MT_R` |
|---|---:|
| `i` | 12 |
| `k` | 12 |
| `j` | 12 |

Marcas de escritura:

| Objeto | `MT_W` |
|---|---:|
| `i` | 14 |
| `j` | 18 |

No se informa `MT_W(k)`. Cuando haga falta usarlo, se lo tratara como no restrictivo salvo que el inciso indique una escritura previa sobre `k`.

## Reglas usadas

### Timestamp ordering

Una lectura es valida si:

```text
read_X(o) es valida si MT(X) >= MT_W(o)
```

Si la lectura es valida:

```text
MT_R(o) = max(MT_R(o), MT(X))
```

Una escritura es valida si:

```text
write_X(o) es valida si:
  MT(X) >= MT_R(o)
  MT(X) >= MT_W(o)
```

Si la escritura es valida:

```text
MT_W(o) = max(MT_W(o), MT(X))
```

### Control optimista

En control optimista, las operaciones se ejecutan de forma tentativa y el control de concurrencia se aplica al intentar hacer `commit`.

Conjuntos de operaciones:

| Transaccion | Conjunto de lectura | Conjunto de escritura |
|---|---|---|
| `T` | `{ i }` | `{ k, j }` |
| `U` | `{ j }` | `{ j }` |

#### Validacion hacia atras

La condicion principal es:

```text
Read(Tv) intersect Write(Ti) = vacio
```

Donde:

```text
Tv = transaccion que quiere validar / hacer commit
Ti = transaccion solapada que ya hizo commit
```

Si la interseccion no es vacia, `Tv` no puede hacer commit.

#### Validacion hacia adelante

Otra forma de resolverlo es validar hacia adelante:

```text
Write(Tv) intersect Read(Ti) = vacio
```

Donde:

```text
Tv = transaccion que quiere validar / hacer commit
Ti = transaccion solapada que sigue activa
```

Si la interseccion no es vacia, `Tv` no puede hacer commit porque invalidaria lecturas ya realizadas por otra transaccion activa.

## Serializacion dada

Segun la imagen:

| T | U |
|---|---|
| `openTransaction` | `openTransaction` |
| `x = read(i);` | |
| | `y = read(j);` |
| `write(k, 54);` | `write(j, 28);` |
| `write(j, 62);` | `commit` |
| `commit` | |

Esta tabla muestra las operaciones de `T` y `U`. Para los incisos de marcas de tiempo se siguen usando las marcas dadas por el enunciado, no la posicion visual de la tabla.

## a. U puede hacer commit? Y si aplico optimista hacia atras?

### Con timestamp ordering

Respuesta:

```text
U no puede hacer commit.
```

Justificacion resumida segun el orden por marcas de tiempo:

```text
MT(T) = 10
MT(U) = 12

MT(T) < MT(U)
```

Entonces:

```text
No, porque MT(U) > MT(T).
```

`U` no puede adelantarse a `T` en el orden serial definido por las marcas de tiempo.

### Con optimista hacia atras

Conjuntos:

```text
Read(U) = { j }
Write(T) = { k, j }
```

Validacion:

```text
Read(U) intersect Write(T)
{ j } intersect { k, j } = { j }
```

Como hay solape en `j`:

```text
U no puede hacer commit con optimista hacia atras.
```

La frase `MT(U) > MT(T)` sirve para ubicar a `T` antes que `U`; la validacion formal se completa con el solape entre `Read(U)` y `Write(T)`.

### Alternativa: optimista hacia adelante

Se usa:

```text
Write(Tv) intersect Read(Ti)
```

Aplicando validacion hacia adelante:

```text
Write(T) intersect Read(U)
{ k, j } intersect { j } = { j }
```

Con esta variante, `T` no podria hacer commit porque invalidaria una lectura de `U`.

Para `U`:

```text
Write(U) intersect Read(T)
{ j } intersect { i } = vacio
```

Entonces, bajo validacion hacia adelante, `U` si podria hacer commit.

Este punto es una alternativa de resolucion, no la respuesta principal del inciso si la catedra pide optimista hacia atras.

## b. T puede escribir j? T puede hacer commit?

`T` tiene:

```text
MT(T) = 10
```

Para escribir `j`:

```text
T: write(j, 62)

MT(T) >= MT_R(j)
10 >= 12   // falso

MT(T) >= MT_W(j)
10 >= 18   // falso
```

La escritura no es valida.

Entonces:

```text
T no puede escribir j.
T no puede hacer commit.
```

De hecho, `T` ya tenia problemas antes:

```text
T: x = read(i)

MT(T) >= MT_W(i)
10 >= 14   // falso
```

Y tambien:

```text
T: write(k, 54)

MT(T) >= MT_R(k)
10 >= 12   // falso
```

Asi que `T` no llega correctamente al commit bajo timestamp ordering.

## c. Si V hizo commit antes de T y realizo write(k, 32), T puede leer k?

Si "antes de `T`" significa antes en el serializado por marcas de tiempo, entonces:

```text
MT(V) < MT(T)
MT(V) < 10
```

Como `V` escribio `k`, la ultima escritura de `k` queda con la marca de `V`:

```text
MT_W(k) = MT(V)
```

Para que `T` lea `k`:

```text
MT(T) >= MT_W(k)
10 >= MT(V)
```

Como `MT(V) < 10`, la lectura es valida.

Por lo tanto:

```text
T puede leer k y lee el valor 32.
```

La marca de lectura de `k` queda:

```text
MT_R(k) = max(12, 10) = 12
```

Ojo: `MT_R(k)=12` no bloquea una lectura. La lectura se valida contra `MT_W(k)`, no contra `MT_R(k)`.

Si en cambio `V` hizo commit antes en tiempo real, pero su marca de tiempo fuera mayor que `10`, entonces no alcanzaria con decir que hizo commit antes: timestamp ordering decide por marca de tiempo, no por reloj real de llegada al commit.

## d. Si W hace openTransaction despues de U, podra leer i y j?

Si `W` abre despues de `U`, entonces:

```text
MT(W) > MT(U)
MT(W) > 12
```

Pero eso solo no alcanza.

Para leer `i`:

```text
MT(W) >= MT_W(i)
MT(W) >= 14
```

Para leer `j`:

```text
MT(W) >= MT_W(j)
MT(W) >= 18
```

Entonces:

```text
W puede leer i y j solamente si MT(W) >= 18.
```

Si `W` recibe, por ejemplo, `MT(W)=13`, no puede leer ni `i` ni `j`.

Si recibe `MT(W)=15`, puede leer `i`, pero no `j`.

Si recibe `MT(W)=18` o una marca mayor, puede leer ambos.

## e. Transaccion X: y = read(j); write(k, 28)

Operaciones de `X`:

```text
y = read(j);
write(k, 28);
```

Para que `X` pueda hacer commit, se la ubica despues de las operaciones de `T` y `U`, con una marca mayor que las marcas restrictivas:

```text
MT(X) = 20
```

Serializacion propuesta:

| T | U | X |
|---|---|---|
| `openTransaction` | `openTransaction` | |
| `x = read(i);` | | |
| | `y = read(j);` | |
| `write(k, 54);` | `write(j, 28);` | |
| `write(j, 62);` | `commit` | |
| `commit` | | `openTransaction` |
| | | `y = read(j);` |
| | | `write(k, 28);` |
| | | `commit` |

La tabla sigue el mismo formato que la imagen: muestra una serializacion de operaciones. Las marcas de tiempo siguen siendo las del enunciado.

Validacion de `X`:

```text
X: read(j)
MT(X) >= MT_W(j)
20 >= 18   // verdadero
```

```text
X: write(k, 28)
MT(X) >= MT_R(k)
20 >= 12   // verdadero
```

Entonces:

```text
X puede hacer commit con MT(X)=20.
```

La condicion general para ubicar a `X` en el serializado es:

```text
MT(X) >= max(MT_W(j), MT_R(k), MT_W(k))
```

Como no se informa `MT_W(k)`, alcanza con elegir una marca posterior a `18`, por ejemplo `MT(X)=20`.

## f. Logs del protocolo commit a dos fases y momento del control de concurrencia

Los logs se plantean con el formato de la catedra: una tabla por log. El control de concurrencia se aplica al recibir `CAN COMMIT`, antes de responder `HAVE COMMIT` o `HAVE ABORT`.

### Caso con timestamp ordering

Con las marcas del enunciado:

```text
T: read(i)
MT(T) >= MT_W(i)
10 >= 14   // falso

U: read(j)
MT(U) >= MT_W(j)
12 >= 18   // falso
```

Por lo tanto, ambos participantes responden abort.

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` a `T` y `U` |
| Recibe `HAVE ABORT` de `T` |
| Recibe `HAVE ABORT` de `U` |
| Envia `DO ABORT` a `T` y `U` |
| Registra `ABORT` |
| Close |

| Log de `T` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia: falla `read(i)` |
| Envia `HAVE ABORT` |
| Recibe `DO ABORT` |
| Abort |

| Log de `U` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia: falla `read(j)` |
| Envia `HAVE ABORT` |
| Recibe `DO ABORT` |
| Abort |

### Caso con optimista hacia atras

Validacion:

| Transaccion | Verificacion | Resultado |
|---|---|---|
| `T` | `Read(T) intersect Write(U) = { i } intersect { j }` | `vacio` |
| `U` | `Read(U) intersect Write(T) = { j } intersect { k, j }` | `{ j }` |

Entonces `T` puede votar `HAVE COMMIT`, pero `U` debe votar `HAVE ABORT`.

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` a `T` y `U` |
| Recibe `HAVE COMMIT` de `T` |
| Recibe `HAVE ABORT` de `U` |
| Envia `DO ABORT` a `T` y `U` |
| Registra `ABORT` |
| Close |

| Log de `T` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia: no hay solape |
| Envia `HAVE COMMIT` |
| Recibe `DO ABORT` |
| Abort |

| Log de `U` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia: hay solape en `j` |
| Envia `HAVE ABORT` |
| Recibe `DO ABORT` |
| Abort |

### Alternativa con optimista hacia adelante

Validacion:

| Transaccion | Verificacion | Resultado |
|---|---|---|
| `T` | `Write(T) intersect Read(U) = { k, j } intersect { j }` | `{ j }` |
| `U` | `Write(U) intersect Read(T) = { j } intersect { i }` | `vacio` |

Entonces `T` vota `HAVE ABORT` y `U` podria votar `HAVE COMMIT`; el coordinador igual decide abort porque no todos votan commit.

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` a `T` y `U` |
| Recibe `HAVE ABORT` de `T` |
| Recibe `HAVE COMMIT` de `U` |
| Envia `DO ABORT` a `T` y `U` |
| Registra `ABORT` |
| Close |

| Log de `T` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia: hay solape en `j` |
| Envia `HAVE ABORT` |
| Recibe `DO ABORT` |
| Abort |

| Log de `U` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia: no hay solape |
| Envia `HAVE COMMIT` |
| Recibe `DO ABORT` |
| Abort |

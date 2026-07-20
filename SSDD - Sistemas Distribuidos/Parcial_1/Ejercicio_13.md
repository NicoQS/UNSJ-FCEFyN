# Ejercicio 13 - Timestamp ordering y 2PC

## Datos

Transaccion `T` con tres subtransacciones:

```text
T1: read(x); read(y);
T2: read(y); write(z);
T3: write(x); read(z);
```

Marcas dadas:

| Elemento | Marca |
|---|---:|
| `MT(T1)` | 10 |
| `MT(T2)` | 15 |
| `MT(T3)` | 18 |
| `MT(T4)` | 16 |
| `MT_r(x)` | 8 |
| `MT_r(y)` | 10 |
| `MT_r(z)` | 10 |
| `MT_w(x)` | 9 |
| `MT_w(y)` | 9 |
| `MT_w(z)` | 9 |

Reglas usadas:

```text
read_i(o) es valida si MT(Ti) >= MT_w(o)

write_i(o) es valida si:
  MT(Ti) >= MT_r(o)
  MT(Ti) >= MT_w(o)
```

Si una lectura es valida:

```text
MT_r(o) = max(MT_r(o), MT(Ti))
```

Si una escritura es valida:

```text
MT_w(o) = max(MT_w(o), MT(Ti))
```

## a. Marcas de tiempo

Como `T1 < T2 < T3`, las marcas respetan:

```text
MT(T1) = 10
MT(T2) = 15
MT(T3) = 18
```

Por lo tanto:

```text
T1 < T2 < T3
```

## b. Marcas de los objetos

Marcas de lectura iniciales:

```text
MT_r(x) = 8
MT_r(y) = 10
MT_r(z) = 10
```

Marcas de escritura iniciales:

```text
MT_w(x) = 9
MT_w(y) = 9
MT_w(z) = 9
```

## c. Que transaccion puede hacer commit

Supuesto usado: el commit respeta el orden de marcas de tiempo.

### c.i. Si `T2` ya hizo commit

Puede hacer commit `T3`.

Justificacion:

```text
MT(T2) = 15 < MT(T3) = 18
```

Como `T2` ya confirmo, la siguiente transaccion segun el orden de timestamps es `T3`.

### c.ii. Si `T1` ya hizo commit

Puede hacer commit `T2`.

Justificacion:

```text
MT(T1) = 10 < MT(T2) = 15
```

Como `T1` ya confirmo, la siguiente transaccion segun el orden de timestamps es `T2`.

### c.iii. Si `T1`, `T2` y `T3` estan ejecutandose

Puede hacer commit `T1`.

Justificacion:

```text
MT(T1) = 10
MT(T2) = 15
MT(T3) = 18
```

La menor marca de tiempo es la de `T1`; por lo tanto, `T1` debe confirmar primero.

## d. Lecturas y escrituras

### d.i. Lecturas

Estado inicial:

```text
MT_w(x) = 9
MT_w(y) = 9
MT_w(z) = 9
```

#### `T1: read(x)`

```text
MT(T1) >= MT_w(x)
10 >= 9
```

La lectura es valida.

```text
MT_r(x) = max(8, 10) = 10
```

#### `T1: read(y)`

```text
MT(T1) >= MT_w(y)
10 >= 9
```

La lectura es valida.

```text
MT_r(y) = max(10, 10) = 10
```

#### `T2: read(y)`

```text
MT(T2) >= MT_w(y)
15 >= 9
```

La lectura es valida.

```text
MT_r(y) = max(10, 15) = 15
```

#### `T3: read(z)`

```text
MT(T3) >= MT_w(z)
18 >= 9
```

La lectura es valida.

```text
MT_r(z) = max(10, 18) = 18
```

Resultado luego de las lecturas:

| Objeto | `MT_r` final |
|---|---:|
| `x` | 10 |
| `y` | 15 |
| `z` | 18 |

Este resultado responde al subinciso d.i considerado de forma aislada. Para el subinciso d.ii no se toma que todas las lecturas ocurrieron antes que todas las escrituras, sino que se respeta la serializacion `T1 < T2 < T3`.

### d.ii. Escrituras

Para este inciso se toma que las transacciones estan serializadas por marca de tiempo:

```text
T1 < T2 < T3
```

Por lo tanto, no se evalua como "primero todas las lecturas y despues todas las escrituras". Se evalua respetando el orden serial equivalente de las transacciones.

Antes de las escrituras, las marcas relevantes son:

```text
MT_r(x) = 10   // por T1: read(x)
MT_r(y) = 15   // por T1: read(y) y T2: read(y)
MT_r(z) = 10   // T3 todavia no ejecuto read(z)

MT_w(x) = 9
MT_w(y) = 9
MT_w(z) = 9
```

#### `T2: write(z)`

Condiciones:

```text
MT(T2) >= MT_r(z)
15 >= 10   // verdadero

MT(T2) >= MT_w(z)
15 >= 9    // verdadero
```

La escritura es valida.

Resultado:

```text
MT_w(z) = max(9, 15) = 15
```

#### `T3: write(x)`

Condiciones:

```text
MT(T3) >= MT_r(x)
18 >= 10   // verdadero

MT(T3) >= MT_w(x)
18 >= 9    // verdadero
```

La escritura es valida.

```text
MT_w(x) = max(9, 18) = 18
```

Resultado luego de las escrituras:

| Objeto | `MT_w` final |
|---|---:|
| `x` | 18 |
| `y` | 9 |
| `z` | 15 |

Luego, cuando `T3` ejecute `read(z)`, la lectura tambien es valida:

```text
MT(T3) >= MT_w(z)
18 >= 15
```

Y queda:

```text
MT_r(z) = max(10, 18) = 18
```

## e. Transaccion `T4`

Se indica:

```text
T1 < T2 < T4 < T3
```

### e.i. Marca de tiempo de `T4`

Como `T4` esta entre `T2` y `T3`:

```text
MT(T2) = 15
MT(T4) = 16
MT(T3) = 18
```

Entonces:

```text
MT(T4) = 16
```

### e.ii. Puede hacer commit `T4`

`T4` puede hacer commit despues de `T1` y `T2`, pero antes de `T3`.

Justificacion:

```text
MT(T1) = 10 < MT(T2) = 15 < MT(T4) = 16 < MT(T3) = 18
```

Por lo tanto, si `T1` y `T2` ya confirmaron, `T4` puede confirmar. Si `T3` confirma antes, se rompe el orden esperado por timestamps.

### e.iii. Puede ejecutar `read(x)`, `read(y)`, `write(z)`

Evaluando con las marcas iniciales del enunciado:

```text
MT_r(x) = 8
MT_r(y) = 10
MT_r(z) = 10

MT_w(x) = 9
MT_w(y) = 9
MT_w(z) = 9
```

#### `T4: read(x)`

```text
MT(T4) >= MT_w(x)
16 >= 9
```

La lectura es valida.

```text
MT_r(x) = max(8, 16) = 16
```

#### `T4: read(y)`

```text
MT(T4) >= MT_w(y)
16 >= 9
```

La lectura es valida.

```text
MT_r(y) = max(10, 16) = 16
```

#### `T4: write(z)`

Condiciones:

```text
MT(T4) >= MT_r(z)
16 >= 10   // verdadero

MT(T4) >= MT_w(z)
16 >= 9    // verdadero
```

La escritura es valida.

```text
MT_w(z) = max(9, 16) = 16
```

Resultado:

```text
T4 puede ejecutar read(x), read(y), write(z)
```

Nota: si `T3` ya hubiera leido `z`, entonces `MT_r(z)` seria `18`. En ese escenario:

```text
MT(T4) >= MT_r(z)
16 >= 18   // falso
```

Por lo tanto, `T4: write(z)` no podria ejecutarse.

## f. Logs del protocolo commit a dos fases

Si `T` hace commit, los logs se plantean con el formato usado por la catedra:

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` |
| Recibe `HAVE COMMIT` |
| Envia `DO COMMIT` |
| Registra `COMMIT` |
| Close |

| Log de `T2` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia |
| Envia `HAVE COMMIT` |
| Recibe `DO COMMIT` |
| Commit |

El control de concurrencia se aplica cuando `T2` recibe `CAN COMMIT`, antes de responder `HAVE COMMIT`.

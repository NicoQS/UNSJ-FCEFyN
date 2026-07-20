# Guia de resolucion practica para Parcial 1

Esta guia resume como resolver los tipos de ejercicios que aparecen en parciales y practicas: sincronizacion, relojes, cortes, serializacion, control de concurrencia, marcas de tiempo, 2PC y cache. La idea no es memorizar soluciones: es reconocer el patron y aplicar siempre el mismo procedimiento.

## Ruta rapida

| Si el ejercicio pide... | Usa este metodo |
|---|---|
| Sincronizacion entre dispositivos | Identificar estado local, estado remoto, online/offline, sincronizacion sincrona/asinc. |
| Relojes vectoriales | Inicializar vectores, incrementar por evento, adjuntar en mensajes, `max` al recibir. |
| Eventos concurrentes/causales | Comparar vectores componente a componente. |
| Cortes consistentes | Verificar que no haya recepcion sin envio o usar vectores frontera. |
| Multicast causal | Reordenar entregas respetando dependencias causales. |
| Serializados/intercalados | Identificar conflictos y construir grafo/orden equivalente. |
| Control optimista | Armar `Read(T)` y `Write(T)`, validar hacia atras o adelante. |
| Marcas de tiempo | Aplicar reglas `MT(T) >= MT_R/W(obj)` en cada operacion. |
| 2PC | Hacer una tabla por log: coordinador y participantes. |
| Cache hit/miss | Separar probabilidad de hit/miss y calcular tiempo promedio. |

## 1. Sincronizacion entre dispositivos

Ejemplo de parcial: misma cuenta de Google en PC, smartphone y Smart TV.

### Metodo

1. Identificar donde se origina el cambio.
2. Decidir si el cambio necesita respuesta inmediata.
3. Separar dispositivos online y offline.
4. Explicar como se propaga al reconectar.
5. Clasificar sincronizacion:
   - Sincrona: requiere respuesta/confirmacion inmediata para continuar.
   - Asincrona: se registra el cambio y se propaga despues.

### Plantilla de respuesta

| Caso | Dispositivo origen | Dispositivos online | Dispositivos offline | Tipo |
|---|---|---|---|---|
| Busqueda | Guarda evento/historial | Ven el cambio al sincronizar | Lo reciben al reconectar | Normalmente asincrona |
| Borrado historial | Registra eliminacion | Deben aplicar borrado | Al reconectar reciben tombstone/orden de borrado | Asincrona con consistencia eventual |
| Busqueda YouTube | Guarda evento en servicio asociado | Se propaga por cuenta | Se actualiza al reconectar | Asincrona |

### Frase clave

```text
El sistema no necesita que todos los dispositivos esten conectados al mismo tiempo; alcanza con registrar la operacion en el servicio y propagarla luego.
```

## 2. Relojes logicos, totalmente ordenados y vectoriales

## 2.1 Reloj de Lamport

### Reglas

```text
Evento local o envio:
C_i = C_i + 1

Recepcion de mensaje con timestamp t:
C_i = max(C_i, t) + 1
```

### Para resolver

1. Dibujar tabla de procesos y eventos.
2. Recorrer eventos de izquierda a derecha.
3. En envio, adjuntar timestamp.
4. En recepcion, aplicar `max`.
5. Recordar limitacion:

```text
a -> b implica C(a) < C(b)
C(a) < C(b) NO implica necesariamente a -> b
```

## 2.2 Reloj totalmente ordenado

Si hay empate en Lamport, se desempata con el identificador del proceso:

```text
C'(evento) = (C(evento), id_proceso)
```

Orden:

```text
(t1, p1) < (t2, p2)
si t1 < t2
o si t1 = t2 y p1 < p2
```

## 2.3 Relojes vectoriales

### Reglas

Para `n` procesos, cada proceso tiene un vector de `n` posiciones.

```text
Inicial:
V_i = [0,0,...,0]

Evento local o envio en P_i:
V_i[i] = V_i[i] + 1

Recepcion en P_i con vector V_m:
V_i[k] = max(V_i[k], V_m[k]) para todo k
V_i[i] = V_i[i] + 1
```

### Comparar eventos

```text
a -> b si V(a) <= V(b) componente a componente y V(a) != V(b)
a || b si V(a) y V(b) son incomparables
```

### Plantilla para justificar

```text
V(a) = [...]
V(b) = [...]

Como V(a) <= V(b), entonces a -> b.
```

O:

```text
V(a) no <= V(b) y V(b) no <= V(a).
Entonces a || b.
```

## 3. Cortes consistentes

Un corte es consistente si no incluye la recepcion de un mensaje sin incluir su envio.

### Metodo grafico

1. Marcar el corte.
2. Buscar mensajes que cruzan el corte.
3. Si el corte incluye la recepcion pero no el envio, es inconsistente.
4. Si incluye envio sin recepcion, puede ser consistente: el mensaje queda en transito.

### Metodo con vectores frontera

Si el corte incluye hasta:

```text
C = [c1, c2, c3, ..., cn]
```

Cada evento frontera debe cumplir:

```text
V(evento_frontera_i)[j] <= c_j para todo j
```

Si alguna componente supera el corte:

```text
El corte es inconsistente.
```

### Plantilla

| Proceso | Evento frontera | Vector | Verificacion |
|---|---|---|---|
| P1 | e | `[...]` | cada componente `<= C` |

## 4. Multicast causalmente ordenado

### Regla

Si un mensaje `m2` depende causalmente de `m1`, todos deben entregar primero `m1` y despues `m2`.

```text
m1 -> m2 entonces entregar m1 antes que m2
```

### Para resolver

1. Detectar dependencias por mensajes o vectores.
2. Armar lista de mensajes.
3. Reordenar solo los que violan causalidad.
4. No imponer orden total si solo piden orden causal.

## 5. Serializacion y serializados

## 5.1 Detectar conflictos

Dos operaciones conflictuan si:

```text
Son de transacciones distintas
Acceden al mismo objeto
Al menos una es write
```

Casos:

| Par | Conflicto |
|---|---|
| `read(x)` vs `read(x)` | No |
| `read(x)` vs `write(x)` | Si |
| `write(x)` vs `read(x)` | Si |
| `write(x)` vs `write(x)` | Si |
| Acceden a objetos distintos | No |

## 5.2 Determinar si es serializable

### Metodo

1. Listar conflictos.
2. Para cada conflicto, marcar direccion:

```text
T -> U si la operacion de T ocurre antes que la de U.
```

3. Si todas las restricciones permiten un orden sin ciclo, es serializable.
4. Si aparece ciclo:

```text
T -> U y U -> T
```

no es serializable.

### Plantilla

| Objeto | Conflicto | Orden impuesto |
|---|---|---|
| `i` | `T:read(i)` antes de `U:write(i)` | `T -> U` |
| `j` | `U:write(j)` antes de `T:write(j)` | `U -> T` |

Conclusion:

```text
Hay ciclo, no existe orden serial equivalente.
```

## 5.3 Construir un serializado que resuelva problemas

Si el problema pide construir un serializado, usar tabla por transaccion:

| T | U |
|---|---|
| `openTransaction` | `openTransaction` |
| `x = read(i);` | |
| `write(i, 54);` | |
| `write(j, 62);` | |
| `commit` | |
| | `y = read(j);` |
| | `write(j, 28);` |
| | `z = read(i);` |
| | `commit` |

Despues justificar:

```text
Todos los conflictos apuntan T -> U, por lo tanto es equivalente al serial T antes que U.
```

## 5.4 Valores finales por intercalacion

Cuando preguntan valores posibles:

1. Resolver valores seriales validos.
2. Buscar intercalaciones que permitan lecturas intermedias.
3. Ver si el resultado coincide con algun serial.
4. Si no coincide, es no serial/incorrecto.

Plantilla:

| Valor final | Alcanzable | Serial | Justificacion |
|---|---|---|---|
| `X=0` | Si | Si | aparece en orden serial |
| `X=1` | Si | No | una transaccion leyo valor intermedio |

## 6. Transacciones anidadas

### Idea

Una transaccion padre puede tener subtransacciones hijas.

```text
T
|- T1
|  |- T11
|  |- T12
|- T2
   |- T21
   |- T22
```

### Como resolver

1. Dibujar/arbolar padre e hijos.
2. Identificar que subtransacciones acceden a los mismos objetos.
3. Los conflictos entre subtransacciones imponen orden.
4. Las subtransacciones sin conflictos pueden intercalarse libremente.
5. En 2PC, cada nodo intermedio puede comportarse como participante frente a su padre y coordinador frente a sus hijos.

### Frase clave

```text
Las transacciones anidadas aumentan concurrencia porque reducen restricciones de orden entre operaciones independientes.
```

## 7. Control optimista

## 7.1 Armar conjuntos

Primero escribir:

| Transaccion | Read | Write |
|---|---|---|
| `T` | `{...}` | `{...}` |
| `U` | `{...}` | `{...}` |

Las escrituras son tentativas hasta validar.

## 7.2 Validacion hacia atras

Se usa cuando `Tv` quiere validar contra transacciones solapadas que ya hicieron commit.

```text
Read(Tv) intersect Write(Ti)
```

Si hay solape:

```text
Tv aborta / no puede commit.
```

Plantilla:

| Quien valida | Verificacion | Resultado |
|---|---|---|
| `T` | `Read(T) intersect Write(U)` | `vacio` -> commit |
| `U` | `Read(U) intersect Write(T)` | `{j}` -> abort |

## 7.3 Validacion hacia adelante

Se usa cuando `Tv` valida contra transacciones activas.

```text
Write(Tv) intersect Read(Ti)
```

Si hay solape:

```text
Tv aborta / no puede commit.
```

Plantilla:

| Quien valida | Verificacion | Resultado |
|---|---|---|
| `T` | `Write(T) intersect Read(U)` | `{j}` -> abort |
| `U` | `Write(U) intersect Read(T)` | `vacio` -> commit |

## 8. Marcas de tiempo

## 8.1 Reglas

Lectura:

```text
read_T(x)
MT(T) >= MT_W(x)
```

Si procede:

```text
MT_R(x) = max(MT_R(x), MT(T))
```

Escritura:

```text
write_T(x)
MT(T) >= MT_R(x)
MT(T) >= MT_W(x)
```

Si procede:

```text
MT_W(x) = max(MT_W(x), MT(T))
```

Si falla, mantener la regla y evaluar:

```text
MT(T) >= MT_W(i)
10 >= 14   // falso
```

## 8.2 Commit por marca

Si el ejercicio pregunta quien puede hacer commit:

```text
La transaccion con menor MT pendiente debe confirmar primero.
```

Ejemplo:

```text
MT(T1)=10 < MT(T2)=15 < MT(T3)=18
```

Si estan todas ejecutandose:

```text
Puede commit T1.
```

Si `T1` ya hizo commit:

```text
Puede commit T2.
```

## 8.3 Como resolver inciso de lecturas y escrituras

1. Hacer lecturas con regla `MT(T) >= MT_W(obj)`.
2. Actualizar `MT_R`.
3. Hacer escrituras respetando la serializacion que indique la catedra.
4. No mezclar "todas las lecturas antes de todas las escrituras" salvo que el inciso lo diga.

## 8.4 Transaccion nueva entre otras

Si:

```text
T1 < T2 < T4 < T3
```

Elegir una marca entre las dos:

```text
MT(T4) = 16
```

Luego validar sus operaciones con las mismas reglas.

## 9. Two Phase Commit en formato de catedra

## 9.1 Donde se aplica control de concurrencia

En esta catedra:

```text
Participante recibe CAN COMMIT
Aplica control de concurrencia
Responde HAVE COMMIT o HAVE ABORT
```

## 9.2 Commit exitoso

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` |
| Recibe `HAVE COMMIT` |
| Envia `DO COMMIT` |
| Registra `COMMIT` |
| Close |

| Log Participante |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia |
| Envia `HAVE COMMIT` |
| Recibe `DO COMMIT` |
| Commit |

## 9.3 Abort

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` |
| Recibe `HAVE ABORT` |
| Envia `DO ABORT` |
| Registra `ABORT` |
| Close |

| Log Participante |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia |
| Envia `HAVE ABORT` |
| Recibe `DO ABORT` |
| Abort |

## 9.4 Si un participante voto commit pero otro aborta

Coordinador:

| Log Coordinador |
|---|
| Abre log |
| Envia `CAN COMMIT` |
| Recibe `HAVE COMMIT` de `T` |
| Recibe `HAVE ABORT` de `U` |
| Envia `DO ABORT` |
| Registra `ABORT` |
| Close |

Participante que voto commit:

| Log de `T` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia |
| Envia `HAVE COMMIT` |
| Recibe `DO ABORT` |
| Abort |

Participante que voto abort:

| Log de `U` |
|---|
| Log |
| Trabajo |
| Recibe `CAN COMMIT` |
| Aplica control de concurrencia |
| Envia `HAVE ABORT` |
| Recibe `DO ABORT` |
| Abort |

## 9.5 Deadlock en subtransacciones

Si dos subtransacciones estan en deadlock y abortan:

1. Las subtransacciones involucradas responden `HAVE ABORT`.
2. Sus padres propagan abort.
3. El coordinador registra `ABORT`.
4. Todos los participantes reciben `DO ABORT`.

## 10. Cache: hit, miss y tiempos promedio

Este tipo de ejercicio puede aparecer con distintos valores.

Datos tipicos:

```text
Probabilidad de hit = p_hit
Probabilidad de miss = p_miss = 1 - p_hit
T_cache
RTT
T_transferencia
T_disco
```

## 10.1 Tiempo promedio en el servidor

Formula:

```text
T_prom_servidor =
p_hit * T_cache + p_miss * (T_cache + T_disco)
```

Ejemplo:

```text
p_hit = 0.70
p_miss = 0.30
T_cache = 0.1 ms
T_disco = 5 ms

T_prom_servidor = 0.70*0.1 + 0.30*(0.1+5)
T_prom_servidor = 0.07 + 1.53
T_prom_servidor = 1.6 ms
```

## 10.2 Tiempo de hit en el cliente

Formula:

```text
T_hit_cliente = T_cache + RTT + T_transferencia
```

Ejemplo:

```text
T_hit_cliente = 0.1 + 30 + 0.05
T_hit_cliente = 30.15 ms
```

## 10.3 Tiempo de miss en el cliente

Formula:

```text
T_miss_cliente = T_cache + T_disco + RTT + T_transferencia
```

Ejemplo:

```text
T_miss_cliente = 0.1 + 5 + 30 + 0.05
T_miss_cliente = 35.15 ms
```

## 10.4 Tiempo promedio en el cliente

Formula:

```text
T_prom_cliente =
p_hit * T_hit_cliente + p_miss * T_miss_cliente
```

Ejemplo:

```text
T_prom_cliente = 0.70*30.15 + 0.30*35.15
T_prom_cliente = 21.105 + 10.545
T_prom_cliente = 31.65 ms
```

## 10.5 Variante: cambio de disco por SSD

Si cambia:

```text
T_disco = 1 ms
```

Servidor:

```text
T_prom_servidor = 0.70*0.1 + 0.30*(0.1+1)
T_prom_servidor = 0.07 + 0.33
T_prom_servidor = 0.40 ms
```

Cliente:

```text
T_miss_cliente = 0.1 + 1 + 30 + 0.05
T_miss_cliente = 31.15 ms

T_prom_cliente = 0.70*30.15 + 0.30*31.15
T_prom_cliente = 21.105 + 9.345
T_prom_cliente = 30.45 ms
```

Conclusion:

```text
El SSD mejora mucho el servidor, pero en el cliente la mejora es menor si el RTT domina.
```

## 10.6 Variante: mejora de hit rate

Si `p_hit = 0.90` y `p_miss = 0.10`:

```text
T_prom_servidor = 0.90*0.1 + 0.10*(0.1+5)
T_prom_servidor = 0.09 + 0.51
T_prom_servidor = 0.60 ms
```

Cliente:

```text
T_prom_cliente = 0.90*30.15 + 0.10*35.15
T_prom_cliente = 27.135 + 3.515
T_prom_cliente = 30.65 ms
```

Conclusion:

```text
Aumentar hit rate mejora ambos, pero si el RTT es grande, el cliente sigue pagando mucho por red.
```

## 10.7 Variante: mejora de red

Si `RTT = 10 ms`:

```text
T_hit_cliente = 0.1 + 10 + 0.05 = 10.15 ms
T_miss_cliente = 0.1 + 5 + 10 + 0.05 = 15.15 ms

T_prom_cliente = 0.70*10.15 + 0.30*15.15
T_prom_cliente = 7.105 + 4.545
T_prom_cliente = 11.65 ms
```

Conclusion:

```text
Reducir RTT impacta fuerte en el cliente porque se paga tanto en hit como en miss.
```

## 11. Checklist final para cualquier ejercicio

Antes de responder:

- [ ] Identifique el tipo de ejercicio.
- [ ] Escribi los datos dados.
- [ ] No invente marcas de tiempo si el enunciado ya las da.
- [ ] Si hay tabla de operaciones, usala como serializacion, no como fuente de `MT`.
- [ ] En timestamp, escribi la regla formal y despues el calculo.
- [ ] En optimista, arma siempre `Read` y `Write`.
- [ ] En serializacion, lista conflictos y orden impuesto.
- [ ] En 2PC, hace tablas de logs.
- [ ] En cache, separa hit/miss y usa `p_miss = 1 - p_hit`.
- [ ] Cerra con una conclusion corta.

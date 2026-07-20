# Guia teorica para parcial - Transacciones, concurrencia y 2PC

Esta guia ordena las notas de clase y corrige frases que pueden llevar a errores en ejercicios. Usala como mapa mental: primero identifica el protocolo, despues aplica la regla formal.

## Resumen rapido

| Tema | Idea para parcial |
|---|---|
| Serializacion | Ejecutar concurrentemente, pero con resultado equivalente a algun orden serial. No es lo mismo que ejecutar secuencialmente. |
| Secuencial | Operaciones/transacciones una despues de otra, sin intercalado relevante. Es correcto pero reduce concurrencia. |
| Serializable | Propiedad del resultado/historia. No implica que no haya deadlock. |
| 2PL / locking | Garantiza serializacion, pero puede generar deadlock. |
| Timestamp ordering | Ordena por `MT(T)`. Valida cada `read/write` contra marcas de los objetos. |
| Optimista | Trabaja tentativamente y valida al intentar commit. Si hay conflicto, aborta. |
| 2PC | No decide concurrencia; decide atomicidad distribuida: todos commit o todos abort. |

## Correccion de apuntes de clase

| Nota original | Veredicto | Forma correcta para estudiar |
|---|---|---|
| "Serializar no es lo mismo que secuencial" | Correcto. | Serializar significa obtener un resultado equivalente a un orden serial. Puede haber intercalado de operaciones. |
| "Serializacion no esta libre de deadlock" | Correcto con matiz. | La serializabilidad es una propiedad de correccion. El deadlock depende del mecanismo usado. Con locks/2PL puede haber deadlock. |
| "Secuencia grado 0" | Hay que corregir el nombre. | Si habla de grados de consistencia/aislamiento, es "grado 0", no "secuencia grado 0". Es muy debil: protege poco y no equivale a serializable. |
| "0 condicion de carrera con espacio de trabajo privado" | Mal expresado. | El espacio de trabajo privado evita que otros vean cambios tentativos. La carrera/conflicto aparece al validar o publicar los cambios, si no hay control correcto. |
| "Optimista aborta" | Correcto. | Si falla la validacion, aborta y puede reintentarse. |
| "Marcas de tiempo puede esperar" | Depende del contexto. | En timestamp ordering clasico, ante conflicto se aborta/reintenta; no espera por locks. En ejercicios de commit puede aparecer espera por orden de commit o por 2PC, pero eso no es deadlock por locking. |
| "En la practica se usa optimista" | Demasiado absoluto. | Se usa mucho OCC/MVCC cuando los conflictos son raros. Pero tambien se usan locks, MVCC, 2PL y combinaciones. Depende de la carga. |
| "Las marcas de tiempo son relojes logicos vectoriales" | Incorrecto. | Timestamp ordering necesita marcas globalmente unicas y ordenables. Pueden ser relojes logicos escalares combinados con ID de servidor. Los relojes vectoriales sirven para causalidad parcial, no para un orden total simple. |
| "Fisicos si es SSDD en tiempo real" | Matizable. | En sistemas con restricciones de tiempo real o external consistency pueden usarse relojes fisicos sincronizados, pero deben manejar deriva e incertidumbre. |

## Serializacion vs secuencial

Una ejecucion secuencial hace una transaccion completa y despues la siguiente:

```text
T1 completa
T2 completa
T3 completa
```

Una ejecucion serializable puede intercalar operaciones:

```text
T1 read(x)
T2 read(y)
T1 write(x)
T2 write(y)
```

Pero el resultado final debe ser equivalente a algun orden serial, por ejemplo:

```text
T1 < T2
```

Para el parcial, NO confundas:

```text
serializable == correcto respecto de algun orden serial
secuencial == ejecucion una por una
```

## Grado 0 de consistencia

Si aparece "grado 0", pensalo como una forma debil de aislamiento.

En la teoria clasica de grados de consistencia:

| Grado | Idea |
|---|---|
| 0 | Proteccion minima. Evita ciertos problemas de escritura sucia, pero permite muchas anomalias. |
| 1 | Mejora sobre grado 0: protege mejor las escrituras hasta fin de transaccion. |
| 2 | Evita leer datos incorrectos/sucios mediante restricciones sobre lecturas. |
| 3 | Aislamiento fuerte, cercano a serializable. |

Para ejercicios de la catedra, lo importante es:

```text
Grado 0 no implica serializabilidad fuerte.
Grado 0 no implica ausencia de deadlock.
```

## Espacio de trabajo privado

En control optimista, cada transaccion trabaja con versiones tentativas privadas.

Esto significa:

```text
Los cambios no son visibles para otras transacciones hasta commit.
```

Ventaja:

```text
Evita lecturas sucias de valores tentativos.
```

Pero no alcanza solo:

```text
Igual hay que validar antes de commit.
```

Si dos transacciones modifican objetos relacionados, el conflicto aparece en la validacion.

## Timestamp ordering

Cada transaccion recibe una marca al comenzar:

```text
openTransaction(T) -> MT(T)
```

En un sistema distribuido, esa marca debe permitir un orden global. Puede construirse como:

```text
<reloj_logico, id_servidor>
```

Reglas para ejercicios:

### Lectura

```text
read_T(x) es valida si:

MT(T) >= MT_W(x)
```

Si es valida:

```text
MT_R(x) = max(MT_R(x), MT(T))
```

### Escritura

```text
write_T(x) es valida si:

MT(T) >= MT_R(x)
MT(T) >= MT_W(x)
```

Si es valida:

```text
MT_W(x) = max(MT_W(x), MT(T))
```

Cuando falla, escribilo manteniendo la regla:

```text
MT(T) >= MT_W(x)
10 >= 14   // falso
```

No inviertas la comparacion si estas justificando la regla.

## Timestamp ordering: que evita y que no

| Punto | Explicacion |
|---|---|
| Deadlock | No usa locks de espera circular; por eso esta libre de deadlock por locking. |
| Bloqueo | En timestamp ordering clasico no espera por locks: aborta/reintenta ante conflicto. |
| Lecturas sucias | Si solo se leen escrituras confirmadas, evita leer datos tentativos. |
| Abortos | Puede abortar transacciones viejas si intentan leer/escribir datos que ya fueron tocados por transacciones mas nuevas. |
| Orden | El orden serial equivalente lo da `MT(T)`. |

Matiz importante:

```text
Si el ejercicio habla de commit distribuido, puede haber espera por 2PC.
Eso no es deadlock del control por timestamp.
```

## Control optimista

El control optimista supone:

```text
Los conflictos son raros.
```

Fases:

| Fase | Que ocurre |
|---|---|
| Trabajo | La transaccion lee/escribe tentativamente. Se guardan `ReadSet` y `WriteSet`. |
| Validacion | Antes de commit, se revisa si hay conflictos. |
| Actualizacion | Si valida, los cambios tentativos se vuelven permanentes. |

Conjuntos:

```text
Read(T)  = objetos leidos por T
Write(T) = objetos escritos por T
```

## Validacion optimista hacia atras

Se usa cuando `Tv` quiere validar contra transacciones solapadas que ya hicieron commit.

Regla:

```text
Read(Tv) intersect Write(Ti) = vacio
```

Si hay interseccion:

```text
Tv no puede hacer commit.
```

Interpretacion:

```text
Tv leyo algo que Ti escribio.
Si Ti ya confirmo, la lectura de Tv pudo quedar vieja o inconsistente.
```

## Validacion optimista hacia adelante

Se usa cuando `Tv` quiere validar contra transacciones solapadas que siguen activas.

Regla:

```text
Write(Tv) intersect Read(Ti) = vacio
```

Si hay interseccion:

```text
Tv no puede hacer commit.
```

Interpretacion:

```text
Tv quiere confirmar una escritura que invalidaria lecturas ya hechas por Ti.
```

## Optimista vs timestamp

| Criterio | Optimista | Timestamp ordering |
|---|---|---|
| Momento del control | Al commit / validacion. | En cada `read/write`. |
| Informacion que guarda | `ReadSet`, `WriteSet`, versiones tentativas. | `MT(T)`, `MT_R(obj)`, `MT_W(obj)`. |
| Ante conflicto | Aborta en validacion. | Aborta/rechaza operacion segun reglas. |
| Deadlock por locks | No, porque no espera por locks. | No, porque no espera por locks. |
| Carga de trabajo | Buena si hay pocos conflictos. | Buena si conviene detectar temprano y mantener orden por marcas. |
| Escrituras tentativas | Privadas hasta commit. | Depende de implementacion, pero las reglas evitan violar el orden por timestamp. |

No estudies como regla absoluta:

```text
Mas lecturas => siempre timestamp
Mas escrituras => siempre optimista
```

Mejor estudialo asi:

```text
Si hay pocos conflictos y queres validar al final -> optimista.
Si queres detectar conflictos por operacion y sostener un orden global -> timestamp ordering.
Si hay muchos conflictos reales -> optimista puede abortar mucho.
```

## Lecturas sucias

Una lectura sucia ocurre cuando:

```text
T2 lee un dato escrito por T1 antes de que T1 confirme.
```

Problema:

```text
Si T1 aborta, T2 leyo un valor que nunca debio existir.
```

Como lo enfrentan:

| Metodo | Como lo evita |
|---|---|
| Strict 2PL | Mantiene locks hasta commit/abort. |
| Optimista | No publica valores tentativos hasta validar y confirmar. |
| Timestamp ordering | Valida contra `MT_W` y evita leer valores que rompen el orden serial. |

## Deadlock

Deadlock aparece cuando hay espera circular:

```text
T espera recurso de U
U espera recurso de T
```

Con locks distribuidos, un servidor puede ver solo una parte del ciclo. Por eso se necesita:

```text
grafo de espera global
detector centralizado o distribuido
timeouts
eleccion de victima
abort
```

Importante:

```text
Serializabilidad no elimina deadlock.
2PL puede ser serializable y aun asi tener deadlock.
```

## Two Phase Commit

2PC resuelve atomicidad distribuida:

```text
Todos hacen commit o todos hacen abort.
```

No reemplaza al control de concurrencia.

En el formato de la catedra:

| Fase | Coordinador | Participante |
|---|---|---|
| 1 | Envia `CAN COMMIT` | Recibe `CAN COMMIT` |
| 1 | Recibe `HAVE COMMIT` o `HAVE ABORT` | Aplica control de concurrencia y responde |
| 2 commit | Envia `DO COMMIT` | Recibe `DO COMMIT` y confirma |
| 2 abort | Envia `DO ABORT` | Recibe `DO ABORT` y aborta |

## Punto de no retorno

Para un participante:

```text
Recibe CAN COMMIT
Aplica control de concurrencia
Si puede confirmar, registra/listo y envia HAVE COMMIT
```

Despues de enviar `HAVE COMMIT`, queda en estado incierto:

```text
No puede abortar unilateralmente.
Debe esperar DO COMMIT o DO ABORT.
```

Si vence un timer:

```text
Envia GET DECISION al coordinador.
```

Si el coordinador no responde:

```text
Puede quedar bloqueado.
```

Para el coordinador:

```text
Si todos responden HAVE COMMIT -> registra COMMIT y envia DO COMMIT.
Si alguno responde HAVE ABORT o hay timeout -> registra ABORT y envia DO ABORT.
```

## Logs en formato de la catedra

### Commit exitoso

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

### Abort

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

## Errores tipicos en ejercicios

| Error | Como evitarlo |
|---|---|
| Usar la tabla visual como fuente de marcas | Las `MT` salen del enunciado o del `openTransaction` si el ejercicio lo pide. |
| Invertir reglas de timestamp | Escribi siempre `MT(T) >= MT_R/W(obj)` y despues evaluas. |
| Confundir serial con serializable | Serial es sin intercalado; serializable puede tener intercalado. |
| Pensar que 2PC valida concurrencia | 2PC decide commit/abort global; el control de concurrencia se aplica antes del voto. |
| Poner `DO COMMIT` si alguien voto abort | Si alguien envia `HAVE ABORT`, el coordinador envia `DO ABORT`. |
| Decir que optimista evita siempre abortos | Optimista puede abortar mucho si hay muchos conflictos. |
| Decir que timestamps son vectoriales | Vector clocks son para causalidad parcial; timestamp ordering necesita orden total. |

## Referencias usadas

- `UNIDAD 6.pdf`: serializacion, locking, optimista, timestamp ordering, 2PC y deadlocks distribuidos.
- Gray, Lorie, Putzolu y Traiger, "Granularity of Locks and Degrees of Consistency in a Shared Data Base": grados de consistencia. Referencia: https://dsf.berkeley.edu/cs286/papers/granularity-tr1976.pdf

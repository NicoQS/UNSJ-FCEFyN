# Preguntas teoricas asociadas a la practica

Estas preguntas estan pensadas para responder rapido en parcial. Son teoricas, pero conectadas con los ejercicios de sincronizacion, relojes, cortes, serializacion, concurrencia, cache y 2PC.

## Sistemas distribuidos y sincronizacion

### 1. Que problema principal aparece con los relojes en sistemas distribuidos?

No existe un reloj global perfecto. Cada nodo tiene su propio reloj fisico y puede derivar respecto de los demas.

### 2. Para que sirve sincronizar relojes fisicos?

Para aproximar una hora comun entre nodos, ordenar eventos por hora real y registrar auditorias, logs o mediciones de tiempo.

### 3. Que es NTP?

Network Time Protocol. Sirve para sincronizar relojes de computadoras en red usando una jerarquia de servidores de tiempo.

### 4. Que diferencia hay entre `date` y `hwclock`?

`date` consulta el reloj del sistema operativo. `hwclock` consulta el reloj de hardware o RTC, que sigue funcionando aunque la PC este apagada.

### 5. Cuando conviene usar relojes logicos?

Cuando importa el orden causal de eventos y no la hora civil exacta.

### 6. Cuando conviene usar relojes fisicos?

Cuando el sistema necesita tiempo real, auditoria, timestamps legales, mediciones de latencia o sincronizacion con hora externa.

## Relojes logicos

### 7. Que garantiza el reloj de Lamport?

Si `a -> b`, entonces `C(a) < C(b)`.

### 8. Que NO garantiza el reloj de Lamport?

Que `C(a) < C(b)` implique causalidad. Dos eventos concurrentes tambien pueden quedar con timestamps ordenados.

### 9. Como se actualiza Lamport en un evento local?

```text
C_i = C_i + 1
```

### 10. Como se actualiza Lamport al recibir un mensaje?

```text
C_i = max(C_i, timestamp_mensaje) + 1
```

### 11. Para que sirve el reloj totalmente ordenado?

Para desempatar eventos con el mismo reloj logico usando el identificador del proceso.

### 12. Que forma tiene un reloj totalmente ordenado?

```text
(timestamp_lamport, id_proceso)
```

## Relojes vectoriales

### 13. Para que sirven los relojes vectoriales?

Sirven para detectar causalidad y concurrencia entre eventos.

### 14. Como se inicializa un reloj vectorial?

Cada proceso inicia con un vector en cero:

```text
[0,0,...,0]
```

### 15. Como se actualiza un vector en un evento local?

El proceso incrementa su propia posicion.

### 16. Como se actualiza un vector al recibir un mensaje?

Se toma el maximo componente a componente con el vector recibido y luego se incrementa la posicion propia.

### 17. Cuando `a` causa a `b` usando vectores?

Cuando:

```text
V(a) <= V(b) componente a componente
V(a) != V(b)
```

### 18. Cuando dos eventos son concurrentes?

Cuando sus vectores son incomparables: ni `V(a) <= V(b)` ni `V(b) <= V(a)`.

## Cortes y snapshots

### 19. Que es un corte?

Un conjunto de prefijos de las historias de los procesos.

### 20. Cuando un corte es consistente?

Cuando no incluye la recepcion de un mensaje sin incluir tambien su envio.

### 21. Puede un corte consistente tener mensajes en transito?

Si. Puede incluir el envio pero no la recepcion.

### 22. Que vuelve inconsistente a un corte?

Que aparezca una recepcion dentro del corte y el envio correspondiente quede fuera.

### 23. Para que sirve un snapshot global?

Para capturar un estado consistente del sistema sin detenerlo, util para recuperacion, deteccion de deadlocks o terminacion.

### 24. Que algoritmo se usa para snapshots distribuidos?

Chandy-Lamport, usando mensajes marcadores en canales FIFO.

## Multicast y orden

### 25. Que garantiza el multicast causal?

Que si un mensaje depende causalmente de otro, todos los procesos los entreguen en ese orden.

### 26. El multicast causal impone orden total?

No. Solo ordena mensajes causalmente relacionados. Los concurrentes pueden entregarse en distinto orden.

### 27. Que garantiza el multicast total?

Que todos los procesos entreguen los mensajes en el mismo orden.

## Serializacion

### 28. Serializar es lo mismo que ejecutar secuencialmente?

No. Una ejecucion puede estar intercalada y aun asi ser serializable si equivale a algun orden serial.

### 29. Que es una ejecucion serial?

Una ejecucion donde una transaccion termina antes de que empiece la siguiente.

### 30. Que es una ejecucion serializable?

Una ejecucion concurrente cuyo resultado equivale a alguna ejecucion serial.

### 31. Cuando dos operaciones conflictuan?

Cuando pertenecen a transacciones distintas, acceden al mismo objeto y al menos una es escritura.

### 32. `read(x)` y `read(x)` conflictuan?

No. Dos lecturas sobre el mismo objeto no generan conflicto.

### 33. `read(x)` y `write(x)` conflictuan?

Si. Acceden al mismo objeto y una es escritura.

### 34. Como se detecta que una historia no es serializable?

Si los conflictos imponen un ciclo, por ejemplo `T -> U` y `U -> T`.

### 35. Que significa que una ejecucion sea localmente serializable pero no globalmente?

Que en cada servidor parece serializable, pero los servidores imponen ordenes distintos e incompatibles entre las mismas transacciones.

## Transacciones

### 36. Que es una transaccion?

Un conjunto de operaciones tratado como una unidad indivisible.

### 37. Que significa atomicidad?

Todo o nada: se ejecutan todas las operaciones o ninguna queda aplicada.

### 38. Que significa aislamiento?

Que las transacciones concurrentes no deben interferir de forma que produzcan resultados incorrectos.

### 39. Que es una lectura sucia?

Leer un dato escrito por otra transaccion que todavia no hizo commit.

### 40. Por que es peligrosa una lectura sucia?

Porque si la transaccion que escribio aborta, la lectura uso un valor que nunca debio existir.

## Control optimista

### 41. Cual es la idea del control optimista?

Suponer que los conflictos son raros, ejecutar tentativamente y validar al final.

### 42. Cuales son las fases del control optimista?

Trabajo, validacion y actualizacion.

### 43. Que es el `ReadSet`?

El conjunto de objetos leidos por una transaccion.

### 44. Que es el `WriteSet`?

El conjunto de objetos escritos por una transaccion.

### 45. Cuando se aplican las escrituras en control optimista?

Despues de validar exitosamente, en la fase de actualizacion.

### 46. Que verifica la validacion hacia atras?

```text
Read(Tv) intersect Write(Ti)
```

Si hay solape, `Tv` aborta.

### 47. Que verifica la validacion hacia adelante?

```text
Write(Tv) intersect Read(Ti)
```

Si hay solape, `Tv` aborta.

### 48. El control optimista puede abortar?

Si. Si falla la validacion, la transaccion aborta.

### 49. Cuando conviene el control optimista?

Cuando hay pocos conflictos y se quiere evitar bloquear durante la fase de trabajo.

## Marcas de tiempo

### 50. Cuando se asigna `MT(T)`?

Al hacer `openTransaction`, salvo que el enunciado ya de explicitamente la marca.

### 51. Que define `MT(T)`?

El orden serial esperado de la transaccion.

### 52. Que significa `MT_R(x)`?

La mayor marca de tiempo de una transaccion que leyo `x`.

### 53. Que significa `MT_W(x)`?

La mayor marca de tiempo de una transaccion que escribio `x`.

### 54. Regla para leer con timestamp ordering.

```text
MT(T) >= MT_W(x)
```

### 55. Regla para escribir con timestamp ordering.

```text
MT(T) >= MT_R(x)
MT(T) >= MT_W(x)
```

### 56. Que pasa si una lectura no cumple la regla?

La operacion no puede realizarse y la transaccion aborta o se rechaza segun el protocolo usado.

### 57. Que pasa si una escritura no cumple la regla?

La escritura no puede realizarse porque violaria el orden serial por marcas.

### 58. Timestamp ordering usa relojes vectoriales?

No. Necesita timestamps globalmente unicos y ordenables. Los relojes vectoriales sirven para causalidad parcial.

### 59. Timestamp ordering esta libre de deadlock?

Esta libre de deadlock por locks, porque no espera por locks. Ante conflicto, rechaza/aborta.

### 60. Una tabla de operaciones cambia las marcas dadas por el enunciado?

No. Las marcas dadas se usan como datos formales; la tabla solo muestra orden de operaciones.

## 2PC

### 61. Para que sirve el protocolo commit a dos fases?

Para garantizar atomicidad distribuida: todos los participantes hacen commit o todos abortan.

### 62. 2PC resuelve control de concurrencia?

No. El control de concurrencia se aplica antes de votar `HAVE COMMIT` o `HAVE ABORT`.

### 63. Que envia el coordinador en fase 1?

`CAN COMMIT`.

### 64. Que responde un participante si puede confirmar?

`HAVE COMMIT`.

### 65. Que responde un participante si no puede confirmar?

`HAVE ABORT`.

### 66. Que envia el coordinador si todos votan commit?

`DO COMMIT`.

### 67. Que envia el coordinador si alguno vota abort?

`DO ABORT`.

### 68. Que significa estado incierto en 2PC?

El participante voto `HAVE COMMIT` y espera la decision final. No puede decidir solo.

### 69. Que hace un participante si vence el timer esperando decision?

Envia `GET DECISION` al coordinador.

### 70. Por que 2PC puede bloquear?

Porque si el coordinador falla despues de que un participante voto commit, el participante no puede decidir unilateralmente.

### 71. Como se plantean logs segun la catedra?

Como tablas separadas por entidad: log del coordinador y log de cada participante.

### 72. Donde se marca el control de concurrencia en los logs?

Despues de recibir `CAN COMMIT` y antes de enviar `HAVE COMMIT` o `HAVE ABORT`.

## Deadlocks

### 73. Que es un deadlock?

Una espera circular entre transacciones o procesos.

### 74. Que estructura se usa para detectarlo?

El grafo de espera o `wait-for graph`.

### 75. Por que el deadlock distribuido es mas dificil?

Porque cada servidor puede ver solo una parte del ciclo.

### 76. Como se resuelve un deadlock?

Se detecta el ciclo, se elige una transaccion victima y se la aborta.

### 77. 2PL puede tener deadlock?

Si. 2PL garantiza serializabilidad, pero puede generar deadlocks por locks.

## Cache y tiempos

### 78. Que es un hit de cache?

Cuando el dato solicitado se encuentra en cache.

### 79. Que es un miss de cache?

Cuando el dato no esta en cache y hay que buscarlo en un nivel mas lento, por ejemplo disco o servidor.

### 80. Como se calcula la probabilidad de miss?

```text
p_miss = 1 - p_hit
```

### 81. Formula de tiempo promedio en servidor.

```text
T_prom_servidor =
p_hit*T_cache + p_miss*(T_cache + T_disco)
```

### 82. Formula de hit en cliente.

```text
T_hit_cliente = T_cache + RTT + T_transferencia
```

### 83. Formula de miss en cliente.

```text
T_miss_cliente = T_cache + T_disco + RTT + T_transferencia
```

### 84. Formula de tiempo promedio en cliente.

```text
T_prom_cliente =
p_hit*T_hit_cliente + p_miss*T_miss_cliente
```

### 85. Si se cambia disco por SSD, que mejora?

Baja `T_disco`, por lo tanto mejora especialmente el tiempo de miss y el promedio del servidor.

### 86. Si el RTT domina, que mejora mas: SSD o red?

Reducir RTT suele mejorar mas el tiempo del cliente, porque la red se paga tanto en hit como en miss.

### 87. Que mejora aumentar la probabilidad de hit?

Reduce la cantidad de misses y por lo tanto baja el tiempo promedio.

## Sistemas de archivos distribuidos

### 88. Para que sirve cache en sistemas de archivos distribuidos?

Para reducir accesos remotos, trafico de red y latencia.

### 89. Cual es el problema principal de cache distribuida?

La coherencia: otros clientes pueden tener copias viejas si alguien modifica el dato.

### 90. Que es semantica de sesion?

Los cambios de un archivo pueden hacerse visibles al cerrar la sesion o archivo, no necesariamente inmediatamente despues de cada escritura.

### 91. Que es NFS?

Network File System, un sistema de archivos distribuido que permite acceder a archivos remotos como si fueran locales.

### 92. Que usa NFS para comunicarse?

RPC y XDR.

## RPC y comunicacion

### 93. Que es RPC?

Remote Procedure Call: permite invocar procedimientos remotos con apariencia similar a una llamada local.

### 94. Que problema tiene RPC respecto de una llamada local?

Puede fallar por red, servidor caido, timeouts o duplicacion de mensajes.

### 95. Que significa semantica "al menos una vez"?

La operacion se ejecuta una o mas veces. Puede haber duplicados si se reintenta.

### 96. Que significa semantica "a lo sumo una vez"?

La operacion se ejecuta cero o una vez. Evita duplicados, pero puede no ejecutarse si hay falla.

### 97. Que es marshalling?

Convertir datos locales a una representacion transmisible por red.

### 98. Que es unmarshalling?

Reconstruir los datos en el receptor a partir de la representacion recibida.

## Preguntas trampa

### 99. Serializable significa libre de deadlock?

No. Una tecnica puede garantizar serializabilidad y aun asi bloquearse, como 2PL.

### 100. Optimista siempre es mejor que timestamp?

No. Depende de la cantidad de conflictos, tipo de carga y costo de abortar.

### 101. Timestamp ordering puede usar hora fisica real directamente?

Puede usar relojes fisicos si el sistema lo exige y estan sincronizados, pero para ejercicios normalmente se usan marcas logicas dadas por el enunciado.

### 102. Si una transaccion voto `HAVE COMMIT`, puede abortar sola?

No. Debe esperar `DO COMMIT` o `DO ABORT`.

### 103. Si un participante vota `HAVE ABORT`, puede el coordinador decidir commit?

No. Si uno aborta, la decision global es abort.

### 104. En optimista, las escrituras se hacen permanentes durante la fase de trabajo?

No. Son tentativas hasta validar y actualizar.

### 105. Si dos eventos tienen Lamport distinto, ya se causalidad?

No. Lamport distinto no alcanza para probar causalidad; para eso conviene usar vectores.

### 106. En un corte consistente puede haber envio sin recepcion?

Si. Eso representa un mensaje en transito.

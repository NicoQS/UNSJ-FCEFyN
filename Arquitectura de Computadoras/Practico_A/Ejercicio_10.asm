; Realice el seguimiento del siguiente código de programación en assembler del DLX para especificar cuál es
; la tarea que realiza y agregue las directivas para el programa ensamblador.

		ADDI r1, r0, #0x5000	; Coloca en r1 la dirección inicial del bloque de memoria r1 = 0x5000
		ADDI r2, r0, #150		; Inicializa el contador r2 con el valor 150 (número de elementos a procesar)
		ADD r3, r0, r0			; Inicializa el acumulador r3 a 0
		ADDI r4, r0, #40		; Inicializa el límite superior r4 con el valor 40
		ADDI r5, r0, #0x4000	; Coloca en r5 la dirección de inicio para almacenar los resultados
OTRO:	LW r6, 0(r1)			; Carga en r6 el valor almacenado en la dirección apuntada por r1
		SLT r7, r6, r4			; Compara si r6 < 40 = r4, si es así r7 = 1, sino r7 = 0
		BNEZ r7, PROX			; Si r7 != 0 (r6 < 40) salta a la etiqueta 'PROX'
		SW 0(r5), r6			; Almacena el valor de r6 en la dirección apuntada por r5
		ADDI r5, r5, #4			; Incrementa r5 en 4 para apuntar a la siguiente posición de almacenamiento
		ADDI r3, r3, #1			; Incrementa el contador de elementos almacenados en r3
PROX:	ADDI r1, r1, #4			; Incrementa r1 en 4 para apuntar al siguiente elemento
		SUBI r2, r2, #1			; Decrementa el contador r2 en 1
		BNEZ r2, OTRO			; Si r2 != 0, repite el ciclo
		SW 0(r5), r3			; Almacena el número de elementos almacenados en r3
		TRAP 0

; Lo que realiza el programa es copiar todos los elementos de un bloque de memoria de 150 componentes que sean mayores o iguales a 40, a otra ubicación de memoria, y al final almacena en la siguiente posición libre la cantidad de elementos copiados.

; Codigo en directivas para el programa ensamblador.

			.data 0x5000
block:		.word  ...				; Aquí se deben definir o reservar los 150 elementos de memoria que se van a procesar.
			.data 0x4000
result:		.space 604				; reserva de espacio para almacenar los elementos mayores o
									; iguales a 40 (150*4=600 bytes + 4 bytes para almacenar la cantidad)
			.text 0x100				; comienzo del código
main:		ADDI r1, r0, #block	; Coloca en r1 la dirección inicial del bloque de memoria
			ADDI r2, r0, #150		; Inicializa el contador r2 con el valor 150
			ADD r3, r0, r0			; Inicializa el acumulador r3 a 0
			ADDI r4, r0, #40		; Inicializa el límite superior r4 con el valor 40
			ADDI r5, r0, #result	; Coloca en r5 la dirección de inicio para almacenar los resultados
OTRO:		LW r6, 0(r1)			; Carga en r6 el valor almacenado en la dirección apuntada por r1
			SLT r7, r6, r4			; Compara si r6 < 40 = r4
			BNEZ r7, PROX			; Si r7 != 0 (r6 < 40) salta a la etiqueta 'PROX'
			SW 0(r5), r6			; Almacena el valor de r6 en la dirección apuntada por r5
			ADDI r5, r5, #4			; Incrementa r5 en 4 para apuntar a la siguiente posición de almacenamiento
			ADDI r3, r3, #1			; Incrementa el contador de elementos almacenados en r3
PROX:		ADDI r1, r1, #4			; Incrementa r1 en 4 para apuntar al siguiente elemento
			SUBI r2, r2, #1			; Decrementa el contador r2 en 1
			BNEZ r2, OTRO			; Si r2 != 0, repite el ciclo
			SW 0(r5), r3			; Almacena el número de elementos almacenados en r3
			TRAP 0
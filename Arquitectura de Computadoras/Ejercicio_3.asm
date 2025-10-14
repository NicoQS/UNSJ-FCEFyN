; Ejecutar las siguientes operaciones entre dos arreglos de datos [ai] y [bi] almacenados en memoria a partir de
; las direcciones 1000h y 2000h respectivamente. Cada arreglo posee 90 datos enteros de 4 bytes y la variable
; c es un valor entero de 4 bytes almacenado en memoria al final del arreglo [bi].
; [ai] = [bi] + c
; Escribir el código en assembler de DLX con las directivas del programa ensamblador que ejecute dicha tarea.
; Cargar el código a partir de la dirección 100h.

		.data 0x1000
a:		.space 360 				; reservo 360 bytes para los 90 elementos de [ai]
		.data 0x2000
b:		.word 10,20,30,35,40,45 ; los restantes 84 valores no están especificados para simplificar
c:		.word 459
		.text 0x100				; comienzo del código
main:	ADDI r2, r0, #0x1000 	; r2 apunta al vector [ai]
		LW r3, c(r0) 			; cargar en r3 la variable c -> c(r0) = dirección_de_c + 0
		ADDI r4, r0, #90 		; r4 es el contador de iterar
iterar: 	LW r5, 0x1000(r2) 		; cargar en r5 el elemento bi -> 0x1000(r2) = offsett de 1000 + direccion_r2
		ADD r6, r5, r3 			; r6 <- bi + c
		SW 0(r2), r6 			; almacenar el resultado r6 como el elemento ai
		ADDI r2, r2, #4 		; incremento de r2 en 4 para apuntar al próximo dato (elemento ai y bi).
		SUBI r4, r4, #1 		; decremento en 1 del contador de iterar.
		BNEZ r4, iterar
		TRAP 0
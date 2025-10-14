; Repetir el ejercicio 7 considerando que el arreglo posee 25 elementos de 1 byte.
			.data 0x1300
a:			.byte 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25 ; arreglo [ai] de 25 elementos
			.data 0x1600
b:			.space 25 				; reserva de 25 bytes para el arreglo [bi] (25*1=25)
			.text 0x100				; comienzo del código
main:		ADDI r2, r0, #a			; r2 apunta al vector [ai]
			ADDI r3, r0, #b			; r3 apunta al vector [bi]
			ADDI r4, r0, #25 		; r4 es el contador de iterar
iterar: 	LB r5, 0(r2) 			; cargar en r5 el elemento ai (1 byte)
			SB 0(r3), r5 			; almacenar el elemento ai en la posición de bi -> 0(r3) = direccion_r3 + offset 0
			ADDI r2, r2, #1 		; incrementar r2 en 1 para apuntar al próximo dato (elemento ai).
			ADDI r3, r3, #1 		; incrementar r3 en 1 para apuntar al próximo dato (elemento bi).
			SUBI r4, r4, #1 		; decrementar en 1 el contador de iterar.
			BNEZ r4, iterar
			TRAP 0
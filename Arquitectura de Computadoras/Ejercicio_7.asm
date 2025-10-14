; Mover (copiar) un arreglo de datos cargado en memoria a otra ubicación de memoria. El arreglo se encuentra
; a partir de la dirección 1300h y posee 18 elementos de 32 bits. Se desea moverlo a la ubicación de memoria
; que se encuentra a partir de la dirección 1600h.

			.data 0x1300
a:			.word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18	; arreglo [ai] de 18 elementos
			.data 0x1600
b:			.space 72 				; reserva de 72 bytes para el arreglo [bi] (18*4=72)
			.text 0x100				; comienzo del código
main:		ADDI r2, r0, #a			; r2 apunta al vector [ai]
			ADDI r3, r0, #b			; r3 apunta al vector [bi]
			ADDI r4, r0, #18 		; r4 es el contador de iterar
iterar: 	LW r5, 0(r2) 			; cargar en r5 el elemento ai
			SW 0(r3), r5 			; almacenar el elemento ai en la posición de bi -> 0(r3) = direccion_r3 + offset 0
			ADDI r2, r2, #4 		; incrementar r2 en 4 para apuntar al próximo dato (elemento ai).
			ADDI r3, r3, #4 		; incrementar r3 en 4 para apuntar al próximo dato (elemento bi).
			SUBI r4, r4, #1 		; decrementar en 1 el contador de iterar.
			BNEZ r4, iterar
			TRAP 0
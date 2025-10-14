; Incrementar los elementos de un arreglo de datos [ai] de 32 bits de 10 elementos cargado en memoria a partir
; de la dirección 1050h en el valor de una constante c de 32 bits almacenada en memoria al final del arreglo.
; La operación a realizar es: [ai] <- [ai] + c.

			.data 0x1050
a:			.word 1,2,3,4,5,6,7,8,9,10	; arreglo [ai] de 10 elementos
c:			.word 5 					; constante c
			.text 0x100					; comienzo del código	
main:		ADDI r2, r0, #0x1050 		; r2 apunta al vector [ai]
			LW r3, c(r0) 				; cargar en r3 la constante c -> c(r0) = dirección_de_c + 0
			ADDI r4, r0, #10 			; r4 es el contador de iterar
iterar: 	LW r5, 0(r2) 				; cargar en r5 el elemento ai -> 0x1050(r2) = offsett de 1050 + direccion_r2
			ADD r6, r5, r3 				; r6 <- ai + c
			SW 0(r2), r6 				; almacenar el resultado r6 como el elemento ai
			ADDI r2, r2, #4 			; incremento de r2 en 4 para apuntar al próximo dato (elemento ai).
			SUBI r4, r4, #1 			; decremento en 1 del contador de iterar.
			BNEZ r4, iterar
			TRAP 0
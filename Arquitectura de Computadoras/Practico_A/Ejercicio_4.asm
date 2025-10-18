; Intercambiar las ubicaciones en memoria de dos arreglos de datos [ai] y [bi] de 32 bits y 15 elementos
; cargados en memoria a partir de las direcciones 1000h y 1200h respectivamente.

		.data 0x1000
a:		.word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ; arreglo [ai] de 15 elementos
		.data 0x1200
b:		.word 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30 ; arreglo [bi] de 15 elementos
		.text 0x100				; comienzo del código
main:	ADDI r2, r0, #0x1000 	; r2 apunta al vector [ai]
		ADDI r3, r0, #0x1200 	; r3 apunta al vector [bi]
		ADDI r4, r0, #15 		; r4 es el contador de iterar
iterar: 	LW r5, 0(r2) 			; cargar en r5 el elemento ai
		LW r6, 0(r3) 			; cargar en r6 el elemento bi
		SW 0(r3), r5 			; almacenar el elemento ai en la posición de bi
		SW 0(r2), r6 			; almacenar el elemento bi en la posición de ai
		ADDI r2, r2, #4 		; incrementar r2 en 4 para apuntar al próximo dato (elemento ai).
		ADDI r3, r3, #4 		; incrementar r3 en 4 para apuntar al próximo dato (elemento bi).
		SUBI r4, r4, #1 		; decrementar en 1 el contador de iterar.
		BNEZ r4, iterar
		TRAP 0
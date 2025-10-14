; Intercambiar e invertir las ubicaciones en memoria de dos arreglos de datos [ai] y [bi], de manera que el
; primer dato de un arreglo pase a ser el último dato del otro arreglo y así sucesivamente hasta el final. Los
; arreglos son de 20 elementos de 32 bits y están cargados en memoria a partir de las direcciones 1000h y
; 1100h respectivamente.

		.data 0x1000
a:		.word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ; arreglo [ai] de 20 elementos
		.data 0x1100
b:		.word 21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40 ; arreglo [bi] de 20 elementos
		.text 0x100				; comienzo del código
main:	ADDI r2, r0, #0x1000 	; r2 apunta al vector [ai]
		ADDI r3, #b, #20 		; r3 apunta al final del vector [bi] (1100h + 20*4 = 1140h)
		ADDI r4, r0, #20 		; r4 es el contador de iterar
iterar: 	LW r5, 0(r2) 			; cargar en	 r5 el elemento ai
		LW r6, 0(r3) 			; cargar en r6 el elemento bi (desde el final hacia el principio)
		SW 0(r3), r5 			; almacenar el elemento ai en la posición de bi
		SW 0(r2), r6 			; almacenar el elemento bi en la posición de ai
		ADDI r2, r2, #4 		; incrementar r2 en 4 para apuntar al próximo dato (elemento ai).
		SUBI r3, r3, #4 		; decrementar r3 en 4 para apuntar al próximo dato (elemento bi).
		SUBI r4, r4, #1 		; decrementar en 1 el contador de iterar.
		BNEZ r4, iterar
		TRAP 0
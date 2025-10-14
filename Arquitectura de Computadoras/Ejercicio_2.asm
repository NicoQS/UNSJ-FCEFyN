; Calcular el valor máximo de un arreglo de 10 números de 32 bits almacenados en memoria a partir de la
; dirección 500H. Usar el registro r1 para almacenar el máximo, r2 para contener el candidato a máximo y r5
; como contador del iterar. Guardar el resultado al final del arreglo, indicando esta posición de memoria por la
; etiqueta “mayor”.
; Escribir el código en assembler de DLX con las directivas del programa ensamblador que ejecute dicha tarea.

			.data 0x500 			; carga del puntero de datos
			;carga de los datos en memoria a partir de 0x500
inicio: 	.word 150,45,-3,478,32,-56,-70,608,89,145
mayor: 		.space 4 				; reserva de 4 bytes para el resultado
			.text 0x1000 			; carga del puntero de texto
			;carga del código en memoria a partir de 0x1000
main: 		ADDI r7, r0, #inicio 	; r7 apunta al primer dato (r7) = 0x500 en r7
			LW r1, 0(r7) 			; r1 <- 1º dato
			ADDI r5, r0,#9 			; r5 es el contador del iterar (r5) = 9
otro: 		ADDI r7,r7,#4 			; incremento en 4 de r7 (apunta al próximo dato)
			LW r2,0(r7) 			; r2 <- próximo dato (candidato)
			SGT r3, r2, r1 			; si (r2) > (r1) then (r3) = 1
			BEQZ r3, no_mayor
			ADD r1, r2, r0 			; r1 <- r2
no_mayor: 	SUBI r5, r5,#1 			; decremento en 1 de r5
			BNEZ r5, otro
			SW mayor(r0), r1 		; almacen. del resultado en memoria SW mayor(r0) = dirección_de_mayor + 0
			TRAP 0

; Realice el seguimiento del siguiente código de programación en assembler del DLX para especificar cuál es
; la tarea que realiza y agregue las directivas para el programa ensamblador.

		ADDI r1, r0, #0x3000  		; Coloca en r1 la dirección inicial del bloque de memoria r1 = 0x3000
		ADDI r2,r0, #0				; Inicializa el acumulador r2 a 0
		ADDI r3, r0, #100		   ; Inicializa el contador r3 con el valor 100 (número de elementos a procesar)
Loop 	LW r4, 0(r1) 				; Carga en r4 el valor almacenado en la dirección apuntada por r1 -> r4 = Mem[0x3000 + offset]
		SGT r5, r4, #525		   ; Compara si r4 > 525, si es así r5 = 1, sino r5 = 0		
		BEQZ r5, salto				; Si r5 == 0 (r4 <= 525) salta a la etiqueta 'salto'
		ADD r2, r2, r4				; Si r4 > 525, acumula el valor de r4 en r2 -> r2 = r2 + r4
salto 	ADDI r1, r1, #4				; Incrementa r1 en 4 para apuntar al siguiente elemento (asumiendo que son palabras de 4 bytes)
		SUBI r3,r3,#1				; Decrementa el contador r3 en 1
		BNEZ r3, loop 				; Si r3 != 0, repite el ciclo
		SW 0(r1), r2				; Almacena el resultado en la dirección apuntada por r1 + offset -> Mem[0x3000 + offset] = r2
		TRAP 0
; Lo que realiza el programa es sumar todos los elementos de un bloque de memoria de 100 componentes que sean mayores a 525, para finalmente en la ultima componente de memoria almacenar la suma total.

; Codigo en directivas para el programa ensamblador.

			.data 0x3000
block:		.word  1,2,3, ...		; Aquí se deben definir o reservar los 100 elementos de memoria que se van a procesar.
			.text 0x100				; comienzo del código
main:		ADDI r1, r0, #block  	; Coloca en r1 la dirección inicial del bloque de memoria
			ADDI r2,r0, #0			; Inicializa el acumulador r2 a 0
			ADDI r3, r0, #100		; Inicializa el contador
Loop:		LW r4, 0(r1) 			; Carga en r4 el valor almacenado en la dirección apuntada por r1
			SGT r5, r4, #525		; Compara si r4 > 525
			BEQZ r5, salto			; Si r5 == 0 salta a la etiqueta 'salto'
			ADD r2, r2, r4			; Acumula el valor de r4 en r2
salto:		ADDI r1, r1, #4			; Incrementa r1 en 4 para apuntar al siguiente elemento
			SUBI r3,r3,#1			; Decrementa el contador r3 en 1
			BNEZ r3, loop 			; Si r3 != 0, repite el ciclo
			SW 0(r1), r2			; Almacena el resultado en la dirección apuntada por r1
			TRAP 0
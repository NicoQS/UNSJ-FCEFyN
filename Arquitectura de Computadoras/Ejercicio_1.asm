; Escribir el código en assembler de DLX que ejecute las siguientes operaciones: a = b + c y d = e – f
; en donde a, b, c, d, e, f son variables de 4 bytes almacenadas consecutivamente en memoria a partir de la
; dirección 0x64 según se muestra en la figura. La variable a = a3 a2 a1 a0 en donde a3 es el byte más
; significativo y a0 el menos significativo; lo mismo para las otras variables.

	.data 0x64
	;comienzo de los datos
a:	.space	4 ; reservo 4 bytes para el resultado a
b:	.word	150
c:	.word	3480
d:	.space	4 ; reservo 4 bytes para el resultado d
e:	.word	4500
f:	.word	400
	.text	0x100
	; comienzo del código
	LW		r2, b(r0)	; |b3| b2| b1| b0| r2 <- b ayuda -> b(r0) = dirección_de_b + 0 = 0x68
	LW		r3, c(r0)	; |c3| c2| c1| c0| r3 <- c
	ADD		r4, r2, r3	; r4 <- b + c
	SW		a(r0), r4	; a <- r4
	LW		r2, e(r0)	; |e3| e2| e1| e0| r2 <- e
	LW		r3, f(r0)	; |f3| f2| f1| f0| r3 <- f
	SUB		r4, r2, r3	; r4 <- e - f
	SW		d(r0), r4	; d <- r4
	TRAP	0
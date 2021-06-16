;Encontrar el valor más grande del siguiente listado de números: 3, 2, 9, 5, 4, 7, 6, 8, 0, 1,
;4. Mostrar este valor en el display y enviarlo al terminal vía el puerto serie.
sndchr  equ 148h
display equ 11Bh
	org 8000h
	mov R7,#0; R7 hace las veces del numero mayor
	mov R2,#0
	mov R3,#11;Cantidad de elementos del conjunto
loop:
	mov A,R2; A hace las veces de current
	lcall conjunto_numeros
	mov 40h,A
	subb A,R7;Comparo A con R7(A-R7)A<R7 el carry(la bandera C) es uno
	jc no_cambia
	mov R7,40h
no_cambia:
	inc R2
	djnz R3,loop
	mov A,R7
	lcall display
	cpl A
	mov P1,A
	mov A,R7
	add A,#30h
	lcall sndchr
	mov A,#0dh
	lcall sndchr
	mov A,#0ah
	lcall sndchr
	ljmp 2F0h	
conjunto_numeros:
	inc A
	movc A,@A+PC
	ret
	db 3, 2, 9, 5, 4, 7, 6, 8, 0, 1, 4
	end
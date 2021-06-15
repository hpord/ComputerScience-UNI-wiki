;Hacer un programa que calcule el factorial de “5”. Mostrar este resultado en las
;posiciones de memoria 31h, 32h y 33h como dígitos decimales. Este resultado enviarlo
;al terminal.
print   equ 136h
sndchr  equ 148h
getbyt  equ 11Eh
display equ 11Bh
	org 8000h
	mov R3,#1;	R3 hace las veces de F
	mov R4,#1;	R4 hace las veces de i
	lcall print
	db 0dh,0ah,"Ingrese un numero para calcular su factorial :",0ah,0
	lcall getbyt
	mov 30h,A
	lcall display
	cpl A
	mov P1,A
	mov R5,30h
lazo:
	mov A,R3
	mov B,R4
	mul AB
	mov R3,A
	inc R4
	djnz R5,lazo
	mov A,R3	;Resultado del factorial
	mov B,#100
	div AB		;A<--4 y en B<--5
	mov 40h,A
	mov A,B
	mov B,#10
	div AB
	mov 41h,A
	mov 42h,B
	lcall print
	db 0dh,0ah,"El factorial es: ",0ah,0
	mov A,40h
	add A,#30h	;se convierte a CODIGO ASCII
	lcall sndchr	;Envia un caracter al terminal
	mov A,41h
	add A,#30h
	lcall sndchr
	mov A,42h
	add A,#30h
	lcall sndchr
	;Salto de linea
	mov A,#0dh
	lcall sndchr
	mov A,#0ah
	lcall sndchr
	ljmp 2F0h
	end
;Hacer un programa que dado un número hexadecimal por ejemplo “8Ah” lo convierta a
;un número de 3 dígitos decimales almacenados en 40h, 41h y 42h y los envíe al terminal
;serial.
sndchr  equ 148h
print   equ 136h
getbyt  equ 11Eh
	org 8000h
	lcall print
	db 0dh,0ah,"Ingrese un numero a convertir a decimal de 3 digitos :",0ah,0
	lcall getbyt
	mov B,#100
	div AB		;A<--4 y en B<--5
	mov 40h,A
	mov A,B
	mov B,#10
	div AB
	mov 41h,A
	mov 42h,B
	lcall print
	db 0dh,0ah,"El numero en decimal es: ",0ah,0
	mov A,40h
	add A,#30h	;se convierte a CODIGO ASCII
	lcall sndchr	;Envia un caracter al terminal
	mov A,41h
	add A,#30h
	lcall sndchr
	mov A,42h
	add A,#30h
	lcall sndchr
	ljmp 2F0h	;Retorno al monitor
	end
	
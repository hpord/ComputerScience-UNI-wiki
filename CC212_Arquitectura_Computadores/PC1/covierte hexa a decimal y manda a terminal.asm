;Hacer un programa que dado un número hexadecimal por ejemplo “45h” lo convierta a
;un número de 2 dígitos decimales almacenados en 40h y 41h y los envíe al terminal
;serial.
sndchr  equ 148h
print   equ 136h
	org 8000h	
	mov A,#3Ah	;Se puede colocar cualquier numero de 8bits que resulte dos digitos
			;decimales
	mov B,#10
	div AB		;A<--4 y en B<--5
	mov 40h,A
	mov 41h,B
	lcall print
	db 0dh,0ah,"El numero en decimal es: ",0ah,0
	mov A,40h
	add A,#30h	;se convierte a CODIGO ASCII
	lcall sndchr	;Envia un caracter al terminal
	mov A,B
	add A,#30h
	lcall sndchr
	ljmp 2F0h	;Retorno al monitor
	end
	
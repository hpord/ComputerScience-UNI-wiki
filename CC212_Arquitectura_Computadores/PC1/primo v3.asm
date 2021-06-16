;Desarrolle un programa que averigua si un número es primo o no. Si es primo que
;muestre en el display “P” y si no lo es que muestre “0”. Que envie al terminal el mensaje
;“Es Primo” o “No es Primo” según sea el caso. Ingrese el número desde el teclado.
sndchr  equ 148h
print   equ 136h
sdelay  equ 142h
display equ 11Bh
getbyt  equ 11Eh
	org 8000h
	lcall print
	db 0dh,0ah,"Ingrese un numero :",0ah,0
	lcall getbyt
	mov 30h,A
	cjne A,#2,otroNumero
	sjmp SiPrimo
OtroNumero:
	mov R2,#2; Numero entre la cual divido
continua:
	mov A,30h
	mov B,R2
	div AB
	mov A,B
	cjne A,#0,sigue
	sjmp NoPrimo
sigue:
	inc R2
	mov A,R2
	cjne A,30h,continua
	sjmp SiPrimo
NoPrimo:
	lcall print
	db 0dh,0ah,"No es Primo",0dh,0ah,0
	mov A,#0C0h ;
	cpl A
	mov P1,A
	ljmp 2F0h
SiPrimo:
	lcall print
	db 0dh,0ah,"Es Primo",0dh,0ah,0
	mov A,#73h
	mov P1,A
	ljmp 2F0h
	end

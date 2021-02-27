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
	lcall print
	db 0dh,0ah,"Los primos en ese intervalo son :",0ah,0
	mov R3,A
	sjmp SiPrimo
	
inicio:
       mov R3, #2
       mov 31h, R3
       mov R5, #0    ;numero de divisores para que sea primo (1)
OtroNumero:
	mov R2,#2; Numero entre la cual divido
continua:
	mov A,R3
	mov B,R2
	div AB
	mov A,B  ; A tiene el residuo
	cjne A,#0,sigue    ; si A es cero no es primo
	inc R5
	inc R3
	mov 31h, R3
	cjne R5,#1, NoPrimo
	sjmp continua
	
sigue:
	inc R2
	mov A,R2
	cjne A, 31h,continua
	mov R3, A
	mov 31h, R3
	cjne R5,#1, SiPrimo
	sjmp continua
NoPrimo:
	inc R3
	mov 31h, R3
	mov A, R3
	cjne A, 30h, continua
	ljmp 2F0H
SiPrimo:
        mov A, R3
	lcall sndchr
	lcall print
	db 0dh,",  ",0
	inc R3
	mov R5, #0
	mov 31h, R3
	mov A, R3
	cjne A, 30h, OtroNumero
	ljmp 2F0H
	end
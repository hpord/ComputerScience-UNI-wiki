;Hacer un programa que encuentre la serie de Fibonacci para n=6. Los números de esta
;serie enviarlo al terminal. Considerar la serie desde n=1.
;1 1 2 3 5 8 13 21 34 ...
sndchr  equ 148h
print   equ 136h
sdelay  equ 142h
display equ 11Bh
getbyt  equ 11Eh
	org 8000h
	lcall print
	db 0dh,0ah,"Ingrese el numero hasta la cual se muestre la serie :",0ah,0
	lcall getbyt
	cjne A,#0,continua
	ljmp 2F0h
continua:
	cjne A,#1,sigue_calculando
	lcall print
	db 0dh,0ah,"Serie de FIBONACCI :",0ah,0
	mov A,#31h
	lcall sndchr
	mov A,#1
	lcall display
	cpl A
	mov P1,A
	ljmp 2F0h
sigue_calculando:
	clr C
	subb A,#2
	mov 30h,A
	lcall print
	db 0dh,0ah,"Serie de FIBONACCI :",0ah,0
	mov A,#31h
	lcall sndchr
	mov A,#44
	lcall sndchr
	mov A,#1
	lcall display
	cpl A
	mov P1,A
	lcall sdelay
	mov A,#31h
	lcall sndchr
	mov A,#44
	lcall sndchr
	mov A,#1
	lcall display
	cpl A
	mov P1,A
	lcall sdelay
	mov R2,#1; R2 hace las veces de "a"
	mov R3,#1; R3 hace las veces de "b"
	mov R5,30h
	mov A,R5
	cjne A,#0,lazo
	ljmp 2F0h
lazo:
	mov A,R2
	add A,R3
	mov R4,A; R4 hace las veces de "c"
	mov A,R3
	mov R2,A
	mov A,R4
	mov R3,A
	mov A,R4
	mov B,#10
	div AB
	mov 35h,A
	mov 36h,B
	add A,#30h
	lcall sndchr
	mov A,36h
	add A,#30h
	lcall sndchr
	mov A,#44
	lcall sndchr
	mov A,R4
	lcall display
	cpl A
	mov P1,A
	lcall sdelay
	djnz R5,lazo
	ljmp 2F0h

	end
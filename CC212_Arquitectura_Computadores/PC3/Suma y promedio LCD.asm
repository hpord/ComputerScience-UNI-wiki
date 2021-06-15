	org 8000h
	lcall inicioLCD
	lcall print
	db 0dh,0ah,"La suma es:",0
		
	mov A,#1
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "La suma es:",0
	mov R0,#offCur
	lcall wrLCDcom4

	MOV R7,#0 ;Acumula la suma
	MOV R6,#0
	MOV R5,#10 ;Cantidad de numeros
loop:	
	MOV A,R6	
	LCALL numeros
	ADD A,R7
	mov R7,A
	INC R6
	DJNZ R5,loop
	mov A,R7
	lcall three_digits_dec_ascii
	mov A,30h
	lcall sndchr
	mov A,31h
	lcall sndchr
	mov A,32h
	lcall sndchr
	mov R0,30h
	lcall wrLCDdata4
	mov R0,31h
	lcall wrLCDdata4
	mov R0,32h
	lcall wrLCDdata4
	
	
	lcall print
	db 0dh,0ah,"Promedio es:",0
	
	
	mov A,#2
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Promedio es:",0
	
	mov B,#10
	mov A,R7
	div AB
	lcall two_digits_dec_ascii
	mov A,30h
	lcall sndchr
	mov A,31h
	lcall sndchr
	mov R0,30h
	lcall wrLCDdata4
	mov R0,31h
	lcall wrLCDdata4
	
	ljmp 2F0h
numeros:
	inc A
	movc A,@A+PC
	ret
	db 2,15,27,25,41,24,10,30,18,8
	
$INCLUDE(subrutinasLCD.inc)
	end
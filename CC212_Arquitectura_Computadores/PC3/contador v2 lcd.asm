;Problema 3
	org 8000h
	lcall inicioLCD
	MOV A,#2	;FILA 2
	MOV B,#5	;POSICION 5 DEL CURSOR
	lcall placeCur4
	lcall prtLCD4
	db "Contador",0
	mov a,#2
	mov b,#11
	lcall placeCur4
	mov R0,#offCur
	lcall wrLCDcom4
repite:
	mov R6,#10
	mov R4,#30h
loop:
	mov A,R4
	add A,#30h
	mov 30h,A
	lcall sndchr
	mov a,#0dh
	lcall sndchr
	mov R0,30h
	lcall wrLCDdata4
	mov R0,#shLfCur ;
	lcall wrLCDcom4
	lcall sdelay
	inc R4
	djnz R6,loop
	sjmp repite	
	
	ljmp 2F0h
	
$INCLUDE(subrutinasLCD.inc)
	end

	org 8000h
	lcall inicioLCD	;Inicializacion del display LCD
	MOV 30H, #50
	MOV 31H, #'B'
	MOV 32H, #'C'
	mov 33H, #'D'
	mov 34H, #'E'
	mov 35h, #'1'
	mov 36h, #'2'
	mov 37h, #3Fh
	MOV 38H, #0
	mov R1,#30h
retorno:
	mov A,@R1
	jz termina
	mov R0,A
	lcall wrLCDdata4
	mov A,#150
	lcall delay
	inc R1
	sjmp retorno
termina:	
	mov R0,#offCur
	lcall wrLCDcom4
	ljmp 2F0h
	
	
$INCLUDE(subrutinasLCD.inc)
	end
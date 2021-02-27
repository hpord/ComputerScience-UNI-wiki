;Mostrar los caracteres a, b, c,d,e,$,&,?....1,2,?
	org 8000h
repite:
	lcall inicioLCD	;Inicializacion del display LCD
	MOV 30H, #0E0h;
	MOV 31H, #0E2h
	MOV 32H, #0E4h
	mov 33H, #0E3h
	mov 34H, #'E'
	mov 35h, #0EEh
	mov 36h, #0F7h
	MOV 37H, #0;
	mov R1,#30h
retorno:
	mov A,@R1
	jz termina	;Z=1 SI A=0
	mov R0,A
	lcall wrLCDdata4;Enviar el dato al display LCD
	lcall sdelay	;UN SEGUNDO
	lcall sdelay	;UN SEGUNDO
	inc R1
	sjmp retorno
termina:	
	mov R0,#offCur	;Ocultar el cursor
	lcall wrLCDcom4
	sjmp repite
	
	
$INCLUDE(subrutinasLCD.inc)
	end
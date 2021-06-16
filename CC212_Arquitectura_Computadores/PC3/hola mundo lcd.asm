;Problema 1
	org 8000h
	lcall initLCD4
	MOV A,#1	;FILA 1
	MOV B,#0	;POSICION 0 DEL CURSOR
	lcall placeCur4
	lcall prtLCD4
	db "Hola Mundo.....",0
	MOV A,#2	;FILA 2
	MOV B,#0	;POSICION 0 DEL CURSOR
	lcall placeCur4	;localiza el cursor en los valores indicados
	lcall prtLCD4
	db "Como les va ?",0
	mov R0,#offcur ;oculta el cursor
	lcall wrLCDcom4;14 y 15 funciona juntas
	ljmp 2F0h
	
$INCLUDE(Sub_LCD.inc)
	end
	org 8000h
	lcall inicioLCD
; localiza el cursor sobre la fila 1, posición 0 e imprime el mensaje en el LCD
repite:
 	mov a, #1 	; fila 1
 	mov b, #0 	; posición 0
 	lcall placeCur4
 	lcall prtLCD4 	; visualiza mensaje en la primera fila
 	db "Hola mundo!.....",0
 	
 	mov a, #2 	; fila 2
 	mov b, #0 	; posición 0
 	lcall placeCur4
 	lcall prtLCD4 	; muestra mensaje
 	db "Como les va?.",0
 	mov R0,#offcur	; desaparece el cursor
 	lcall wrLCDcom4
 	lcall print	;Envia al terminal
 	db "Hola mundo!.....",0 ;visualiza mensaje
 	lcall print
 	db 0dh,0ah,"Como les va?.",0dh,0ah,0
	ljmp 2F0h
$INCLUDE(subrutinasLCD.inc)
	end
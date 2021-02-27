	org 8000h
	lcall inicioLCD
; localiza el cursor sobre la fila 1, posición 0 e imprime el mensaje
repite:
 	mov a, #1 ; fila 1
 	mov b, #0 ; posición 0
 	lcall placeCur4
 	lcall prtLCD4 ; visualiza mensaje
 	db "Arquitectura de",0
 	
 	mov a, #2 ; fila 2
 	mov b, #4 ; posición 4
 	lcall placeCur4
 	lcall prtLCD4 ; muestra mensaje
 	db "Computadores",0
 	
 	mov a, #1 ; fila 1
 	mov b, #14h ; posición 14h
 	lcall placeCur4
 	lcall prtLCD4 ; visualiza mensaje
 	db "Arquitectura de",0
 	
 	mov a, #2 ; fila 2
 	mov b, #18h ; posición 18h
 	lcall placeCur4
 	lcall prtLCD4 ; muestra mensaje
 	db "Computadores",0
 	
otravez:
	mov R6,#4
regresa:
 	mov R0,#onDsp
 	lcall wrLCDcom4
 	mov A,#250
 	lcall delay
 	mov A,#250
 	lcall delay
 	mov A,#250
 	lcall delay
 	mov R0,#offDsp
 	lcall wrLCDcom4
 	mov A,#250
 	lcall delay
 	mov A,#250
 	lcall delay
	djnz R6,regresa

	mov R0,#onDsp
 	lcall wrLCDcom4
 	mov A,#250
 	lcall delay
 	mov A,#250
 	lcall delay
 	mov A,#250
 	lcall delay
 	mov r0,#offcur
    	lcall wrlcdcom4
    	mov A,#1
    	lcall delay     ;
    	;Aqui empieza el desplazamiento
 	mov R7,#40
movimiento_iz:
	;mov A,#1
	;lcall dspshlf4
	mov R0,#shLfDsp
	lcall wrlcdcom4
	mov A,#250
	lcall delay
	djnz R7,movimiento_iz
	mov R7,#40
movimiento_der:
	;mov A,#1
	;lcall dspShRt4
	mov R0,#shRtDsp
	lcall wrlcdcom4
	mov A,#250
	lcall delay
	djnz R7,movimiento_der
	sjmp otravez
$INCLUDE(subrutinasLCD.inc)
	end
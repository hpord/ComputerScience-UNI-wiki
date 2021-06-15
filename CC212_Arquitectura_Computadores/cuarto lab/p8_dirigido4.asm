;Hacer un programa que muestre:
; MODULO
; ENTRENADOR TMC51
;Y que parpadee.
sdelay  equ 142h
	org 8000h
	lcall inicioLCD
	mov a, #1 ; fila 1
 	mov b, #0 ; posición 0
 	lcall placeCur4
 	lcall prtLCD4 ; visualiza mensaje
 	db "MODULO",0
 	
 	mov a, #2 ; fila 2
 	mov b, #0 ; posición 0
 	lcall placeCur4
 	lcall prtLCD4 ; muestra mensaje
 	db "ENTRENADOR TMC51",0
 	lcall sdelay
 repite:
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
	sjmp repite
$INCLUDE(subrutinasLCD.inc)
	end
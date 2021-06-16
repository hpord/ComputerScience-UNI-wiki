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
 	db "Helou",0
 	
 	mov a, #2 ; fila 2
 	mov b, #0 ; posición 0
 	lcall placeCur4
 	lcall prtLCD4 ; muestra mensaje
 	db "Naranjita nwn",0
 	lcall sdelay
 	lcall sdelay
 	mov r0,#offcur
    	lcall wrlcdcom4
    	mov A,#1
    	lcall delay     ;
;Aqui empieza el desplazamiento
otravez:
 	mov R7,#16
movimiento_der:
	mov R0,#shRtDsp
	lcall wrlcdcom4
	mov A,#250
	lcall delay
	djnz R7,movimiento_der
	lcall sdelay
	mov R7,#16
movimiento_iz:
	mov R0,#shLfDsp
	lcall wrlcdcom4
	mov A,#250
	lcall delay
	djnz R7,movimiento_iz
	lcall sdelay
	sjmp otravez
$INCLUDE(subrutinasLCD.inc)
	end
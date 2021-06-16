	org 8000h
repite:
	lcall inicioLCD
	mov r0,#offcur
    	lcall wrlcdcom4
    	mov A,#1
    	lcall delay
    	mov a,#1
    	mov b,#4
    	lcall placeCur4
    	mov A,#1
    	lcall delay
    	lcall prtLCD4
    	db "Espere...",0 
    	mov a,#2
    	mov b,#0
    	lcall placeCur4
    	mov A,#1
    	lcall delay
    	mov R7,#16
lazo:
	mov R0,#0FFh
	lcall wrLCDdata4
	mov A,#250
	lcall delay
	mov A,#250
	lcall delay
	djnz R7,lazo
	sjmp repite
	ljmp 2F0h
$INCLUDE(subrutinasLCD.inc)
	end

	
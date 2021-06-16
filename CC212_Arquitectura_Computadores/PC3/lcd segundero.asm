;4	
	org 8000h
	lcall inicioLCD
	lcall print
	db 0dh,0ah, "Segundero:",0dh,0ah,0
	mov A,#1
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Segundero:",0
	mov A,#2
	mov B,#11
	lcall placeCur4
	mov R0,#offCur
	lcall wrLCDcom4
denuevo:
	mov R7,#60
	mov R4,#0
otravez:
	mov A,R4
	lcall twoDigits_dec_ascii
	mov R0,30h
	lcall wrLCDdata4
	mov R0,#shLfCur
	lcall wrLCDcom4
	mov R0,#shLfCur
	lcall wrLCDcom4
	mov A,#100
	lcall delay
	inc R4
	djnz R7,otravez
	sjmp denuevo
$INCLUDE(subrutinasLCD.inc)
	end	
		
	
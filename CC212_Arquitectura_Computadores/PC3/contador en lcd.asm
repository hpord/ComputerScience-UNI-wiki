;5	
	org 8000h
	lcall inicioLCD
	lcall print
	db 0dh,0ah, "Contador:",0dh,0ah,0
	mov A,#1
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Contador:",0
	mov A,#2
	mov B,#11
	lcall placeCur4
	mov R0,#offCur
	lcall wrLCDcom4
denuevo:
	mov R7,#251
	mov R4,#0
otravez:
	mov A,R4
	lcall treeDigits_dec_ascii
	mov R0,30h
	lcall wrLCDdata4
	mov R0,31h
	lcall wrLCDdata4
	mov R0,32h
	lcall wrLCDdata4
	mov R0,#shLfCur
	lcall wrLCDcom4
	mov R0,#shLfCur
	lcall wrLCDcom4
	mov R0,#shLfCur
	lcall wrLCDcom4
	lcall posicion11_terminal
	mov A,30h
	lcall sndchr
	mov A,31h
	lcall sndchr
	mov A,32h
	lcall sndchr
	mov A,#0dh
	lcall sndchr
	mov A,#250
	lcall delay
	inc R4
	djnz R7,otravez
	sjmp denuevo
posicion11_terminal:
	mov R3,#12
sigue:
	mov A,#20h
	lcall sndchr
	djnz R3,sigue
	ret
$INCLUDE(subrutinasLCD.inc)
	end	
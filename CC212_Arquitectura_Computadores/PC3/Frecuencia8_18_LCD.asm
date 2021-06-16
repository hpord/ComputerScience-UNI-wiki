	org 8000
	
	mov TMOD,#20h
	setb TR0
menu:	
	lcall inicioLCD
	mov A,#1
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Frecuencia: 8hz",0
	mov R0,#offCur
	lcall wrLCDcom4
	mov A,#2
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Frecuencia: 18hz",0
	
	
	jnb P3.2,f8hz
	
	sjmp menu
	
f8hz:
	mov R0,#offDsp
	lcall wrLCDcom4
	lcall frecuencia8hz
	mov R0,#onDsp
	lcall wrLCDcom4
	ljmp f8hz

frecuencia8hz:
	mov R7,#255
loop1:
	jnb TF0,$
	clr TF0
	djnz R7,loop1
	ret		
	
	

$INCLUDE(subrutinasLCD.inc)
	end	
	
	org 8000h
	
	mov TMOD,#20h
	lcall print
	db 0dh,0ah,"Seleccione una frecuencia",0dh,0ah
	db " ",0dh,0ah
	db "P3.2)Frecuencia de 23hz",0dh,0ah    ;k=3
	db "P3.3)Frecuencia de 27hz",0dh,0ah, 0   ;k=2
menu:
	
	jnb P3.2,f23hz
	jnb P3.3,f27hz
	
	sjmp menu
	  
f23hz:  
        lcall inicioLCD
	mov A,#1
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Frecuencia: 23hz",0
	mov R0,#offCur
	lcall wrLCDcom4
	lcall frec23hz
        ljmp f23hz
frec23hz:    
	mov R7,#3	;La cantidad de overflows
	cpl p1.0
	setb TR0
	setb ET0
	setb EA
	ajmp menu
loop1:
	jnb TF0,$
	clr TF0
	djnz R7,loop1
	ret
	
f27hz: 
        lcall inicioLCD
	mov A,#1
	mov B,#0
	lcall placeCur4
	lcall prtLCD4
	db "Frecuencia: 27hz",0
	mov R0,#offCur
	lcall wrLCDcom4
	lcall frec27hz
        ljmp f27hz
 
frec27hz:    
	mov R7,#3	;La cantidad de overflows
	cpl p1.0
	setb TR0
	setb ET0
	setb EA
	ajmp menu
loop2:
	jnb TF0,$
	clr TF0
	djnz R7,loop2
	ret		
	
	

$INCLUDE(subrutinasLCD.inc)
	end
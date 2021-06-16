
	org 8000h
	mov TMOD,#20h
	mov A,#1
	mov dptr,#rutina_interrup_t0
	lcall setintvec
menu:
	lcall print
	db 0dh,0ah,"Menu de Frecuencias",0dh,0ah
	db "01)Frecuencia de 2hz",0dh,0ah
	db "02)Frecuencia de 12hz",0dh,0ah
	db "03)Frecuencia de 22hz",0dh,0ah
	db "04)Frecuencia de 32hz",0dh,0ah
	db "05)Salir",0dh,0ah
	db "Ingrese seleccion :",0ah,0
	lcall getbyt
	mov R6,A
	cjne A,#1,f12hz
f2hz:
	mov R7,#28	;La cantidad de overflows
	setb TR0
	setb ET0
	setb EA
	ajmp menu	;el menu se lanza de nuevo
f12hz:
	cjne A,#2,f22hz
	mov R7,#5	;de aca
	setb TR0
	setb ET0
	setb EA
	ajmp menu	;hasta aca esta generando 12 herz
f22hz:	
	cjne A,#3,f32hz
	mov R7,#3
	setb TR0
	setb ET0
	setb EA
	ajmp menu
f32hz:
	cjne A,#4,sale
	mov R7,#2
	setb TR0
	setb ET0
	setb EA
	ajmp menu
sale:
	clr EA
	clr TR0
	lcall print
	db 0dh, 0ah,"Hasta la proxima...",0dh,0ah,0
	ljmp 2F0h
	
rutina_interrup_t0:
	mov A,R6
	cjne A,#1,otro
frec2hz:
	dec R7
	cjne R7,#0,sale_interrupcion
	cpl P1.0
	mov R7,#28
	sjmp sale_interrupcion
otro:
	cjne A,#2,otro2
frec12hz:	;k=28
	dec R7 ;decremento k a 27 
	cjne R7,#0,sale_interrupcion ;cuando k=0 sale de la interrupcion
	cpl P1.0
	mov R7,#5
	sjmp sale_interrupcion
otro2:
	cjne A,#3,otro3
frec22hz:
	dec R7
	cjne R7,#0,sale_interrupcion
	cpl P1.0
	mov R7,#3
	sjmp sale_interrupcion
otro3:
	cjne A,#4,sale_interrupcion
frecc32hz:
	dec R7
	cjne R7,#0,sale_interrupcion
	cpl P1.0
	mov R7,#2
	sjmp sale_interrupcion
sale_interrupcion:
	reti
	end
setintvec equ 145h
print equ 136h
getbyt equ 11Eh

	org 8000h
	mov TMOD,#20h
	mov A,#1
	mov dptr,#rutina_interrup_t0
	lcall setintvec
menu:
	lcall print
	db 0dh,0ah,"Menu de Frecuencias",0dh,0ah
	db "01)Frecuencia de 13hz",0dh,0ah
	db "02)Frecuencia de 18hz",0dh,0ah
	db "03)Frecuencia de 23hz",0dh,0ah
	db "04)Salir",0dh,0ah
	db "Ingrese seleccion :",0ah,0
	lcall getbyt
	mov R6,A
	cjne A,#1,f18hz
f13hz:
	mov R7,#4	;La cantidad de overflows
	lcall print
	db 0dh, 0ah,"Frecuencia seleccionada 13 Hz",0dh,0ah,0
	setb TR0
	setb ET0
	setb EA
	ajmp menu	;el menu se lanza de nuevo
f18hz:
	cjne A,#2,f23hz
	mov R7,#3	;de aca
	lcall print
	db 0dh, 0ah,"Frecuencia seleccionada 18Hz",0dh,0ah,0
	setb TR0
	setb ET0
	setb EA
	ajmp menu	;hasta aca esta generando 18 herz
f23hz:	
	cjne A,#3,sale
	mov R7,#2  
	lcall print
	db 0dh, 0ah,"Frecuencia seleccionada 23 hz",0dh,0ah,0
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
frec13hz:
	dec R7
	cjne R7,#0,sale_interrupcion
	cpl P1.0
	mov R7,#4
	sjmp sale_interrupcion
otro:
	cjne A,#2,otro2
frec18hz:	;k=3
	dec R7 ;decremento k a 2 
	cjne R7,#0,sale_interrupcion ;cuando k=0 sale de la interrupcion
	cpl P1.0
	mov R7,#3
	sjmp sale_interrupcion
otro2:
	cjne A,#3,sale_interrupcion
frec23hz:
	dec R7
	cjne R7,#0,sale_interrupcion
	cpl P1.0
	mov R7,#2
	sjmp sale_interrupcion
sale_interrupcion:
	reti
	end
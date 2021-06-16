;Hacer un programa que utilizando dos botones conectados al pin P3.2 y P3.3
;interrumpa al TMC51 y en ese momento envíe al puerto serie mensajes desde donde
;ha sido interrumpido. El programa principal es hacer un led parpadeante por el puerto
;P1.0.
delay equ 118h
setintvec equ 145h
print equ 136h
getchr equ 121h
prthex equ 13Fh
sndchr	equ 148h
	org 8000h
	mov TMOD,#20h ;timer0 modo 1
	mov A,#1	;rutina de interrupcion
	mov dptr,#rutina_interrup_t0	;interrupcion del timer0
	lcall setintvec
	clr IT0
	clr IT1
	mov A,#0
	mov dptr,#RutinaInterr0 ;interrupcion exter0
	lcall setintvec
	mov A,#2
	mov dptr,#RutinaInterr1 ; interrupcion exter1
	lcall setintvec
	setb EX0
	setb EX1
	setb EA
	setb P3.2
	setb P3.3
f2hz:
	mov R7,#28	;La cantidad de overflows
	setb TR0
	setb ET0 ;interrupcion del temporizador
	setb EA ;interrupcion global
repite:
	lcall getchr
	cjne A,#3,continua;#3 es el codigo assci de control C, para otras teclas se busca su codigo assci.
	clr EX0
	clr EX1 ;clr deshabilita las interrupciones
	clr EA
	lcall print
	db 0dh,0ah,"Ctl-C ha sido presionado. Por tanto el programa termina",0dh,0ah,0
	ljmp 2F0h
continua:
	sjmp repite
rutina_interrup_t0:;aca se podria poner un contador exadecimal par 
;apoder visualizarlo en pantalla a la misma frecuencia
	push acc
	dec r7
	cjne r7,#0,sale_interrupcion
	cpl p1.0
	mov r7,#28
	mov A,R5
	inc R5
	lcall prthex
	mov A,#0dh
	lcall sndchr
	dec R4
	mov A,R4
	cjne A,#0,sale_interrupcion
	mov R4,#16
	mov R5,#0
	;dec R7 ;rutina de interrupcion hasta 0
	;cjne R7,#0,sale_interrupcion
	;cpl P1.0 
	;mov R7,#28
sale_interrupcion:
	pop acc	;se agrego para el nuevo codigo de ariba
	reti
	
RutinaInterr0:
	clr EX0
	mov A,#100
	lcall delay
	push acc
	lcall print
	db 0dh,0ah,"La interrupcion viene del boton P3.2",0dh,0ah
	db 0dh,0ah,"Si desea salir del programa presione ctl-C",0dh,0ah,0
	mov A,#200
	lcall delay
	pop acc
	setb EX0
	reti
RutinaInterr1:
	clr EX1
	mov A,#100
	lcall delay
	push acc
	lcall print
	db 0dh,0ah,"La interrupcion viene del boton P3.3, es P3.3 ok?",0dh,0ah,0
	mov A,#200
	lcall delay
	pop acc
	setb EX1
	reti	
	end
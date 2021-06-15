;Hacer un programa para el TMC51 que al presionar el botón conectado al pin P3.2
;interrumpa al TMC51 y en ese momento envié por el puerto serie dos cadenas: “curso:
;Arquitectura de Computadores” y en otra fila “Prof.: Martín Cruz”. El programa principal
;es un contador de 0 a F mostrado en el display de 7 segmentos que cuenta cada segundo.
display equ 11Bh
sdelay  equ 142h
setintvec equ 145h
print equ 136h
delay equ 118h
prthex equ 13Fh
sndchr equ 148h
getchr equ 121h
	org 8000h
	clr IT0
	mov A,#0
	mov dptr,#RutinaInterrExt0
	lcall setintvec
	setb EX0
	setb EA
	setb P3.2
repite:
	mov R5,#20
	lcall getchr
	cjne A,#3,noCtlC ;si ingresa Ctrl C sale del programa
	clr EX0
	clr EA
	;podemos imprimir si queremos :v
	ljmp 2F0h
noCtlC:
	sjmp repite
;	mov R3,#16
;	mov R5,#0
;otra_vez:
;	mov A,R5
;	lcall display
;	cpl A	;funciona para un display catodo comun
;	mov P1,A
;	mov A,R5
;	lcall prthex
;	mov A,#0dh
;	lcall sndchr
;	lcall sdelay
;	inc R5
;	djnz R3,otra_vez
;	sjmp repite
RutinaInterrExt0:
	push acc
	clr EX0
	mov A,#100
	lcall delay
	lcall print
	db 0dh,0ah,"Me estan interrumpiendo, voy a multiplicar dos numeros",0dh,0ah,0
	mov A,R5
	;mov A,#20
	mov B,#10
	mul AB
	mov 30h,A
	lcall print
	db 0dh,0ah,"El resultado de multiplicar es :",0ah,0
	mov A,30h
	lcall prthex
	lcall print
	db 0dh,0ah,0
	mov A,#200
	lcall delay
	setb EX0
	pop acc
	reti
	end
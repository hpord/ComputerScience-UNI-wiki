display equ 118h
sdelay  equ 142h
setintvec equ 145h
print equ 136h
delay equ 118h
	org 8000h
	clr IT0	;esto es para el boton p3.2 y para el p3.3 es IT1
	mov A,#0
	mov dptr,#RutinaInterrExt0
	lcall setintvec
	setb EX0
	setb EA
	setb p3.2
repite:
	mov R3,#16
	mov R2,#0
otra_vez:
	mov A,R2
	lcall display
	cpl A
	mov p1,A
	lcall sdelay
	inc R2
	djnz R3,otra_vez
	sjmp repite
RutinaInterrExt0:
	push acc
	clr EX0
	mov A,#100
	lcall delay
	lcall print
	db 0dh,0ah,"Curso: Arquitectura de Computadores",0dh,0ah
	db "Alumno: Hervias Danel",0dh,0ah,0
	mov A,#200
	lcall delay
	setb EX0
	pop acc
	reti
	end
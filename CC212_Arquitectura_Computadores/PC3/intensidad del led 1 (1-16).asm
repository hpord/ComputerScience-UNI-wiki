;Hacer un programa para el TMC51 que al ingresar valores de 0 a F modifique la
;intensidad del led en P1.0. Usar PWM.
ledFlag equ 20h	; Se pone a 1 si el LED está encendido
dCycle  equ 7Eh
dCycleC equ 7Fh
PWM     equ 90h	;Puerto P1.0
errorf  equ 3	;Flag de error en caso se ingrese un caracter distinto a 0..F
print   equ 136h
getchr  equ 121h
ascbin  equ 100h
setintvec equ 145h
	org 8000h
	mov dCycle,#0
	setb PWM	;Apagamos el LED
	lcall itim0
loop:
	lcall print
	db 0dh,0ah,"Ingresa nueva intensidad del LED(0...F)",0
	lcall getchr
	cjne A,#3,noCtlC
	clr TR0
	clr EA
	lcall print
	db 0dh,0ah,"Ha presionado Ctl-C. El programa termina.",0dh,0ah,0
	ljmp 2F0h
noCtlC:
	clr errorf
	lcall ascbin; Convertir codigo ASCII a binario (los primos 4 bits del nible del byte)
	;un nible son 4 bits, entonces un byte tiene 2 nibles
	jnb errorf,digitOK
	ajmp loop 
digitOK:
	setb TR0
	setb EA
	swap a	;intercambio entre nibles
	anl A,#0F0h
	mov dCycle,A
	cpl A
	mov dCycleC,A
	ajmp loop
	
itim0:
	mov TMOD,#22H	;Se usa el modo 2
	mov A,#1
	mov dptr,#rutinaInterrT0
	lcall setintvec
	mov TH0,dCycle
	setb ET0
	setb TR0
	ret
	
rutinaInterrT0:
	push acc
 	jb ledFlag, LedOff ; si el flag es 1, apaga el led
 	clr PWM ; sino enciende el motor
	mov TH0, dCycle ; prepara para la siguiente cuenta
 	setb ledFlag ; actualiza el estado del flag
 	pop acc
 	reti
 	
 Ledoff:
 	setb P1.0 ; apaga el LED
 	mov TH0, dCycleC ; prepara para la siguiente cuenta
 	clr ledFlag ; actualiza el estado del flag
 	pop acc
 	reti
	end
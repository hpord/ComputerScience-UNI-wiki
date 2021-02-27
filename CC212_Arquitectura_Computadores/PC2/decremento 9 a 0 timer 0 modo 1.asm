;Hacer un programa que decremente de 9 a 0 cada segundo. El tiempo de 1 segundo
;generarlo usando el timer 0 en modo 1. El programa que se repita indefinidamente.
;TIMER 0 en MODO 1
;Kx65536x(12/11.0592x10^6)s}=1seg
;k=14
display equ 11bh
sndchr	equ 148h
print	equ 136h
	org 8000h
	mov TMOD,#21h
	setb TR0
repite:
	mov R4,#10
	mov R2,#9
lazo:
	mov A,R2
	lcall display
	cpl A
	mov P1,A
	mov A,R2
	lcall decremento_digito_terminal
	lcall segundo
	;lcall sdelay
	dec R2
	djnz R4,lazo
	lcall print ;se usa para enviar mensaje cuando llega a 0 el contador
	db 0dh,0ah,"Ignition!!, Litoff!!",0dh,0ah,0
	sjmp repite
	ljmp 2F0h
segundo:
	mov R6,#14
loop:
	jnb TF0,$
	clr TF0
	djnz R6,loop
	ret
decremento_digito_terminal:;para mostrar en la terminal 
	add A,#30h
	lcall sndchr
	mov A,#0dh	; para resscribir los numeros sobre si mismos en la terminal
	lcall sndchr
	ret
	end
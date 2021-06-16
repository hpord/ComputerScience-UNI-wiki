;Hacer un programa que decremente de 9 a 0 cada segundo. El tiempo de 1 segundo
;generarlo usando el timer 0 en modo 0. El programa que se repita indefinidamente
;periodo = 1/1hz = 1s
;SemiPeriodo = 0.5s
;kx8192x(12/11.0592x10^6)=1s
;k=11.0592x10^6/12x8192
;k=112.5~ = 112.
display	equ 11bh
;sdelay	equ 142h
sndchr	equ 148h
print 	equ 136h
	org 8000h
	mov TMOD,#20h
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
	mov R6,#112
loop:
	jnb TF0,$
	clr TF0
	djnz R6,loop
	ret
decremento_digito_terminal:
	add A,#30h
	lcall sndchr
	mov A,#0dh
	lcall sndchr
	ret
	end
	
	
	
	
	
	
	
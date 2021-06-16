;Hacer un programa que genere una frecuencia de 15hertz en el pin P1.0 del Puerto 1.
;MODO 1 del timer0.
;periodo=1/15 Hz = 0.066seg
;semiPeriodo = 0.033seg
;(65536-j)x(12/11.0592x10^6)s=0.033s
;j=34816 --> j=8800h
;Yo necesito que le microcontrolador cuente desde 34816 hasta 65536

	org 8000h
	mov tmod,#01h
otra_vez:
	mov th0,#88h
	mov tl0,#0h
	setb tr0; inicio el temporizador TIMER0
	jnb TF0,$
	clr TF0
	cpl p1.0
	clr tr0
	sjmp otra_vez
	end
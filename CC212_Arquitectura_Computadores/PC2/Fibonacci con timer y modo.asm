;4)Hacer un programa que encuentre 
;la serie de Fibonacci para n=6. 
;Los números de esta
;serie enviarlo al terminal. 
;Considerar la serie desde n=1.
;n=1  1
;n=2  1  1
;n=3  1  1  2
;n=4  1  1  2  3
;n=5  1  1  2  3  5
;n=6  1  1  2  3  5  8
;generar el tiempo de 1s entre número y número
sdelay  equ 142h
sndchr  equ 148h
display equ 11Bh
	org 8000h
	mov TMOD,#21h    ;modo 2 timer 1 y modo 1 timer 0
	
	mov A,#1	;muestra 1 en el display (n=1)
	lcall display
	cpl A
	mov P1,A
	lcall timer_delay ; llama al delay de 1 segundo
	mov A,#1	; muestra 1 en el display  (n=2)
	lcall display
	cpl A
	mov P1,A
	lcall timer_delay ;llama al delay de 1 segundo
	
;A partir de aqui empieza el calculo
	mov R5,#1	; hace las veces de a
	mov R6,#1	; hace las veces de b
	mov R2,#3	; hace las veces de i
lazo:
	mov A,R5
	add A,R6	;add R5,R6(esta prohibido)
	mov R7,A	; hace las veces de c
	mov A,R6
	mov R5,A
	mov A,R7
	mov R6,A
	mov A,R7
	lcall display		;imprime c en el display
	cpl A
	mov P1,A
	lcall timer_delay	;llama al delay de 1 segundo
	inc R2
	mov A,R2
	cjne A,#5,lazo
	ljmp 2F0h	
	
timer_delay:
	mov TH0,#10h		; valor de recarga 4096 en decimal, 1000 en hexadecimal, 10h 00h
	mov TL0,#0		; 							 TH   TL
	mov R3,#0		; inicio de contador
	setb TR0		; inicio del timer 0 (TR0=1)
	
espera_desborde:	
	jnb TF0,$		; (jump no bit ) salta a la misma instruccion si no se ah desbordado, si se desborda es porque el flg se volvio 1
	inc R3			; incrementa el contador
	clr TF0			; limpia la bandera 
	mov TH0, #10h
	mov TL0, #00h
	cjne R3,#15,espera_desborde ; (compare and jump if not equal) compara el R3 con 15 y salta a espera_desborde si no es igual a 15
	clr TR0			; apaga el timer 0 (TR0=0)		
	ret			; retorna donde se quedó el lcall
	end

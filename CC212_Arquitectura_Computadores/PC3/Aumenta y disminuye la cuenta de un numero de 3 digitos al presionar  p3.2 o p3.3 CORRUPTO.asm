	org 8000h
	lcall inicioLCD
	mov a, #1 	; fila 1
 	mov b, #0 	; posición 0
 	lcall placeCur4
 	mov R0,#offCur ;desaparece el cursor
 	lcall wrLCDcom4
	clr IT0 ;Se activa la interrupción externa 0 en el nivel bajo del pulso.
	clr IT1 ;Se activa la interrupción externa 1 en el nivel bajo del pulso.
	mov A,#0
	mov dptr,#rutinaExt0
	lcall setintvec
	mov A,#2
	mov dptr,#rutinaExt1
	lcall setintvec
	setb EX0
	setb EX1
	setb EA ;Habilita las interrupciones en forma global
	setb P3.2
	setb P3.3
	mov R6,#0 ;Hace las veces de un contador
	mov A,R6
	sjmp $ ;Salto asi mismo
rutinaExt0:
	push acc
	clr EX0
	mov A,#100
	lcall delay
	mov A,R6
	subb A,#19
	jnc cambia_
	sjmp se_va
cambia_:
	mov R6,#0
	sjmp salta
se_va:
	inc R6
salta:
	mov A,R6
	lcall tres_digitos_decimales
	mov R0,30h
	lcall wrLCDdata4
	mov R0,31h
	lcall wrLCDdata4
	mov R0,32h
	lcall wrLCDdata4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov A,#100
	lcall delay
	setb EX0
	pop acc
	reti
rutinaExt1:
	push acc
	clr EX1
	mov A,#100
	lcall delay
	mov A,R6	
	subb A,#1
	jc cambia2
	sjmp no_cambia
cambia2:
	mov R6,#19
	sjmp salta2
no_cambia:
	dec R6
salta2:
	mov A,R6
	lcall tres_digitos_decimales
	mov R0,30h
	lcall wrLCDdata4
	mov R0,31h
	lcall wrLCDdata4
	mov R0,32h
	lcall wrLCDdata4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov A,#100
	lcall delay
	setb EX1
	pop acc
	reti
	
tres_digitos_decimales:
	mov B,#100
	div AB
	add A,#30h
	mov 30h,A
	mov A,B
	mov B,#10
	div AB
	add A,#30h
	mov 31h,A
	mov A,B
	add A,#30h
	mov 32h,A
	ret
$INCLUDE(subrutinasLCD.inc)
end
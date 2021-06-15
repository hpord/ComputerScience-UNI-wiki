;Hacer un contador decimal de 0 a 250 cada décima de segundo en el LCD.
sndchr  equ 148h
	org 8000h
	lcall inicioLCD
	mov a, #1 	; fila 1
 	mov b, #0 	; posición 0
 	lcall placeCur4
 	mov R7,#251
 	mov R3,#0
 	mov R0,#offCur ;desaparece el cursor
 	lcall wrLCDcom4
lazo:
 	mov A,R3
 	lcall tres_digitos_decimales
 	mov R0,30h
 	lcall wrLCDdata4
 	mov R0,31h
 	lcall wrLCDdata4
 	mov R0,32h
 	lcall wrLCDdata4
 	mov R0,#shLfCur	;desplaza el cursor a la izquierda
 	lcall wrLCDcom4
 	mov R0,#shLfCur	;desplaza el cursor a la izquierda
 	lcall wrLCDcom4
 	mov R0,#shLfCur	;desplaza el cursor a la izquierda
 	lcall wrLCDcom4
 	
 	mov A,30h
 	lcall sndchr
 	mov A,31h
 	lcall sndchr
 	mov A,32h
 	lcall sndchr 	
 	mov A,#0dh
 	lcall sndchr
 	
 	mov A,#100
 	lcall delay
 	inc R3
 	djnz R7,lazo
 	ljmp 2f0h
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
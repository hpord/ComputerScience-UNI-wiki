;2) Fibonacci para n=7 1 1 2 3 5 8 13
binasc equ 109h
org 8000h
lcall inicioLCD
mov a, #1 ; fila 1
mov b, #0 ; posición 0
lcall placeCur4
lcall prtLCD4
db "Serie Fibonacci :",0
mov a, #2 ; fila 2
mov b, #0 ; posición 0
lcall placeCur4
mov R7,#1
mov R3,#1
mov R5,#3
mov R0,#offCur ;desaparece el cursor
lcall wrLCDcom4

lazo1:
	mov A,R7
	lcall binasc
	mov 30h,R2
	mov A,R2
	mov R0,A
	lcall wrLCDdata4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4

lazo2:
	mov A,R3
	lcall binasc
	mov 30h,R2
	mov A,R2
	mov R0,A
	lcall wrLCDdata4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDdata4

lazo_3:
	mov A,R5
	add A,R6	
	mov R7,A	
	mov A,R6
	mov R5,A
	mov A,R7
	mov R6,A
	mov A,R7
	lcall dos_digitos_decimales
	mov R0,30h
	lcall wrLCDdata4
	mov R0,31h
	lcall wrLCDdata4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4
	mov R0,#shLfCur ;desplaza el cursor a la izquierda
	lcall wrLCDcom4	
	inc R2
	mov A,R2
	cjne A,#7,lazo_3
	ljmp 2F0h

dos_digitos_decimales:
	mov B,#10
	div AB
	add A,#30h
	mov 30h,A
	mov A,B
	add A,#30h
	mov 31h,A
	ret
$INCLUDE(subrutinasLCD.inc)
	end
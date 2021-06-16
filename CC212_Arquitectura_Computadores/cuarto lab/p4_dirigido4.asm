;_Hacer un programa que muestre en la primera fila el mensaje Segundero: y en la segunda
;fila un contador decimal de 0 a 59 cada décima de segundo en el LCD y lo envíe también
;al terminal.
sndchr  equ 148h
sdelay 	equ 142h
	org 8000h
	lcall inicioLCD
	mov a, #1 	; fila 1
 	mov b, #0 	; posición 0
 	lcall placeCur4
 	lcall prtLCD4
 	db "SEGUNDERO :",0
 	lcall print
 	db "SEGUNDERO :",0dh, 0ah,0
 	mov a, #2 	; fila 2
 	mov b, #11 	; posición 11
 	lcall placeCur4
 	mov R7,#60
 	mov R3,#0
 	mov R0,#offCur ;desaparece el cursor
 	lcall wrLCDcom4
lazo:
 	mov A,R3
 	lcall dos_digitos_decimales
 	mov R0,30h
 	lcall wrLCDdata4
 	mov R0,31h
 	lcall wrLCDdata4
 	mov R0,#shLfCur	;desplaza el cursor a la izquierda
 	lcall wrLCDcom4
 	mov R0,#shLfCur	;desplaza el cursor a la izquierda
 	lcall wrLCDcom4
 	lcall diez_espacios
 	mov A,30h
 	lcall sndchr
 	mov A,31h
 	lcall sndchr
 	mov A,#0dh
 	lcall sndchr
 	mov A,#100
 	lcall sdelay
 	inc R3
 	djnz R7,lazo
 	ljmp 2F0h
diez_espacios:
 	mov R5,#10
loop:
	mov A,#20h
	lcall sndchr
	djnz R5,loop
	ret
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
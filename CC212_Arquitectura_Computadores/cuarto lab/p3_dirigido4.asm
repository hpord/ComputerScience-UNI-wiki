;Modificar el programa anterior para que se muestre en la primera fila del display:
;CONTADOR: y en la segunda fila, en la posición 11 la cuenta del 0 al 9. Hacer lo mismo
;para que se visualice en el terminal.
binasc  equ 109h
sdelay  equ 142h
sndchr  equ 148h
	org 8000h
	lcall inicioLCD
	mov a, #1 	; fila 1
 	mov b, #0 	; posición 0
      	lcall placeCur4 ; como b=0, el cursor ira a la posicion 0
 	lcall prtLCD4    
 	db "CONTADOR :",0
 	lcall print
 	db "CONTADOR :",0dh, 0ah,0
 	
repite:
 	mov a, #2 	; fila 2
 	mov b, #11 	; posición 11
 	lcall placeCur4
 	mov R7,#10
 	mov R3,#0
 	mov R0,#offCur    ;desaparece el cursor
 	lcall wrLCDcom4   ; escribe una palabra comando al LCD
                          ; el comando debe ser localizado en R0
lazo:
 	mov A,R3
 	lcall binasc
 	mov 30h,R2
 	mov A,R2
 	mov R0,A
 	lcall wrLCDdata4
 	mov R0,#shLfCur	;desplaza el cursor a la izquierda
 	lcall wrLCDcom4
 	lcall once_espacios
 	mov A,30h
 	lcall sndchr
 	mov A,#0dh
 	lcall sndchr  ;envia un caracter contenido en el acumulador A
 	lcall sdelay  ;retardo de un segundo
  	inc R3
 	djnz R7,lazo
 	ljmp 2F0h
once_espacios:
	mov R5,#11
loop:
	mov A,#20h
	lcall sndchr
	djnz R5,loop
	ret
$INCLUDE(subrutinasLCD.inc)
	end
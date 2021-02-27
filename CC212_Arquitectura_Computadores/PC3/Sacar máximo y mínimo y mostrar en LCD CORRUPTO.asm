
org 8000h
lcall inicioLCD
	mov a, #1 ; fila 1
	mov b, #0 ; posición 0
	lcall placeCur4
	lcall prtLCD4 ; visualiza mensaje en la primera fila
	db "Mayor :",0
	mov a, #1 ; fila 1
	mov b, #11 ; posición 0
	lcall placeCur4
	mov R6,#255	;
	mov R2,#0	
	mov R5,#10	
	lcall lazo
	lcall wrLCDcom4
	mov a, #2 ; fila 2
	mov b, #0 ; posición 0
	lcall placeCur4
	lcall prtLCD4 ; muestra mensaje
	db "Menor :",0
	mov a, #2 ; fila 1
	mov b, #11 ; posición 0
	lcall wrLCDcom4
	mov R3,#0; R5 hace las veces de largest
	mov R7,#10
	mov R2,#0
	lcall wrLCDcom4
	lcall lazo_2
	
lazo:
	mov A,R1
	clr C
	lcall extraer_numero
	mov 30h,A
	subb A,R6 		;A<--A-R4, si A>R4, Carry(C)=0
	jc cambio			; salte si hay carry(resta negativa) carry=1

lazo_2:
	mov A,R2
	clr C
	lcall extraer_numero
	mov 30h,A	;A es current
	subb A,R3;A<--(A-R5)
	jc continua
	mov R3,30h
	
continua:
	inc R2
	djnz R7,lazo_2
	mov A,R3
	sjmp mostrar_2
	
regresa:
	inc R1
	djnz R5,lazo			;decrementa y salto si R5 no es 0
	sjmp mostrar			
	
cambio:
	mov R6,30h
	sjmp regresa
	
mostrar:
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
	ret
	
mostrar_2:
	mov A,R3
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
	ljmp 2F0h
	
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
	
extraer_numero:
	inc A
	movc A,@A+PC
	ret
	db 120,9,20,155,42,187,25,230,198,4
	ljmp 2F0h
$INCLUDE(subrutinasLCD.inc)
	end
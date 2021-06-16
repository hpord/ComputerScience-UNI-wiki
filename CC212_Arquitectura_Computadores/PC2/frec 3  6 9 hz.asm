;1)

getbyt  equ 11Eh
sndchr	equ 148H
print   equ 136h
	org 8000h
	clr 0CAh
	clr 0C9h
	mov 0C9h,#3
	lcall print
	db "Seleccione Frecuencia",0dh,0ah
	db "01) 3Hz",0dh,0ah
	db "02) 6Hz",0dh,0ah
	db "03) 9Hz",0dh,0ah
	db "04) Retorna al monitor",0dh,0ah
	db "Seleccionar opcion:",0dh,0ah,0;
	lcall getbyt
	mov 60h,A
	lcall selecciona_valor_menos_s ;RECAP2L
	mov 61h,A
	mov A,60h
	mov 0CAh,A	
	lcall selecciona_valor_mas_s	;RECAP2H
	mov 62h,A
	mov 0CBh,A
	
	setb 0CAh
	ljmp 2F0h
	
	

selecciona_valor_menos_s:
	inc A
	movc A,@A+PC
	ret
	db 0,0,0,0,0	
	ret
	
selecciona_valor_mas_s:
	inc A
	movc A,@A+PC
	ret
	db 0,10h,8h,0B0h,0
	ret
	end
		
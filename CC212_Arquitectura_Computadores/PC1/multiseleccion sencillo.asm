;Hacer un menú de tal forma que pueda seleccionar como “01” un programa de la pregunta
;3. Y como “02” seleccione un programa de la pregunta 4. Y como “03” seleccione un
;programa de la pregunta 5.
; Sugerencia: Usar la subrutina getbyt
sndchr	equ 148h
print	equ 136h
getbyt	equ 11Eh
	org 8000h
menu:
	lcall print
	db 0dh,0ah,"M  E  N  U",0dh,0ah
	db "01)Programma de la Pregunta 3",0dh,0ah
	db "02)Programma de la Pregunta 4",0dh,0ah
	db "03)Programma de la Pregunta 5",0dh,0ah
	db "04)Salir",0dh,0ah
	db "Seleccione opcion",0dh,0
	lcall getbyt
	cjne A,#1,otra_validacion
	sjmp opcion1
otra_validacion:
	cjne A,#2,sale
	sjmp opcion2
sale:
	cjne A,#3,sale1
	sjmp opcion3
sale1:
	cjne A,#4,sale2
	ljmp 2F0h
sale2:
	lcall print
	db 0dh,0ah,"Opcion invalida",0dh,0ah,0
	ljmp 2F0h
opcion1:
	lcall print
	db 0dh,0ah,"Programma de la Pregunta 3",0dh,0ah,0
	ljmp 2F0h
	;ljmp 8400  direccion de otro programa para poder ejecutarlo
opcion2:
	lcall print
	db 0dh,0ah,"Programad de la pregunta 4",0dh,0ah,0
	ljmp 2F0h
opcion3:
	lcall print
	db 0dh,0ah,"Programma de la Pregunta 5",0dh,0ah,0
	ljmp 2F0h
	end
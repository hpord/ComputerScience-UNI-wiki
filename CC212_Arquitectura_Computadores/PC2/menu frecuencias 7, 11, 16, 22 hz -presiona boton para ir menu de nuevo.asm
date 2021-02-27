sndchr	equ 148h
print	equ 136h
getbyt	equ 11Eh
	org 8000h
menu:
	lcall print
	db 0dh,0ah,"M  E  N  U",0dh,0ah
	db "01)Frecuencia 7hz",0dh,0ah
	db "02)Frecuencia 11hz",0dh,0ah
	db "03)Frecuencia 16hz",0dh,0ah
	db "04)Frecuencia 22hz",0dh,0ah
	db "05)Salir",0dh,0ah
	db "Presione el boton conectado a P3.2 para regresar al MENU",0dh,0ah
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
	sjmp opcion4
sale2:
	cjne A,#5,sale3
	sjmp opcion5
sale3:
	lcall print
	db 0dh,0ah,"Opcion invalida",0dh,0ah,0
	ljmp 2F0h
opcion1:
	mov tmod,#21h
loop1:
	mov th0,#24h
	mov tl0,#0h
	setb tr0
	jnb TF0,$
	clr TF0
	cpl p1.0
	clr tr0
	
	sjmp loop1
opcion2:
	mov tmod,#21h
loop2:
	mov th0,#5dh
	mov tl0,#0h
	setb tr0
	jnb TF0,$
	clr TF0
	cpl p1.0
	clr tr0
	sjmp Espera_cuenta
	sjmp loop2
opcion3:
	mov tmod,#21h
loop3:
	mov th0,#80h
	mov tl0,#0h
	setb tr0
	jnb TF0,$
	clr TF0
	cpl p1.0
	clr tr0
	sjmp Espera_cuenta
	sjmp loop3
opcion4:
	mov tmod,#21h
loop4:
	mov th0,#2Eh
	mov tl0,#0h
	setb tr0
	jnb TF0,$
	clr TF0
	cpl p1.0
	clr tr0
	sjmp Espera_cuenta
	sjmp loop4
opcion5:
	ljmp 2F0h
	end
regresa_menu_:
	ajmp regresa_menuEspera_cuenta:
	jnb P3.2,regresa_menu_
	jnb TF0,Espera_cuenta
	cpl P1.0
	clr TF0
	cjne A,#1,va_
	sjmp frec_10hz

regresa_menu_:
	ajmp regresa_menu
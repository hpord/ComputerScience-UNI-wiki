;Modo 1 del Timer0 para calculo de 10Hz de frecuencia en P1.0
print equ 136h
getbyt equ 11Eh
	org 8000h
regresa_menu:
	mov TMOD,#21h
	clr TR0
	setb P1.0
	lcall print
	db 0dh,0ah,"    M E N U    ",0dh,0ah
	db 0dh,0ah,"01)Frecuencia 10Hz",0dh,0ah
	db "02)Frecuencia 15Hz",0dh,0ah
	db "03)Frecuencia 20Hz",0dh,0ah
	db "04)Salir",0dh,0ah
	db "Presione el boton conectado a P3.2 para regresar al MENU",0dh,0ah
	db "Seleccione una opcion: ",0ah,0
	lcall getbyt
	cjne A,#1,pregunta
	sjmp frec_10hz
pregunta:
	cjne A,#2,decidir
	sjmp frec_15hz
decidir:
	cjne A,#3,sale
frec_20hz:
	mov TH0,#0A6h
	mov TL0,#0
	setb TR0
	sjmp Espera_cuenta
sale:
	clr TR0
	setb P1.0
	lcall print
	db 0dh,0ah,"Hasta pronto...",0dh,0ah,0
	ljmp 2F0h
frec_15hz:
	mov TH0,#88h
	mov TL0,#0
	setb TR0
	sjmp Espera_cuenta
frec_10hz:
	mov TH0,#4Ch
	mov TL0,#0
	setb TR0
Espera_cuenta:
	jnb P3.2,regresa_menu_
	jnb TF0,Espera_cuenta
	cpl P1.0
	clr TF0
	cjne A,#1,va_
	sjmp frec_10hz
regresa_menu_:
	ajmp regresa_menu
va_:
	cjne A,#2,va__
	sjmp frec_15hz
va__:
	sjmp frec_20hz
	end
	
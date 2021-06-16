;1)Hacer  un  programa para  el  TMC51 que  al  presionar  un  botón  
;conectado  al  pin  P3.2 encienda un led  conectado en P1.0 y  si  
;se  vuelve a  presionar  que lo  apague. Este led  se enciende 
;con la instrucciónclr P1.0.
setintvec equ	145h
delay	 equ	118h
	org 8000h
	clr IT0	;configuro para que se considere el nivel bajo
	mov A,#0;seleciono interrupcion externa 0
	mov dptr,#rutina_interrup_ext0
	lcall setintvec
	setb EX0;habilita la interrupcion externa 0
	setb EA	;habilita interrupciones globales
	setb P3.2
	setb P1.0	;inicialmente el led esta apagado
	sjmp $		;salto asi mismo
	;ljmp 2F0h
rutina_interrup_ext0:
	clr EX0		;deshabilito la interrupcion
	mov A,#100	;100 milisgundos
	lcall delay
	cpl P1.0
	mov A,#200	;200 milisegundos
	lcall delay
	setb EX0	;habilito la interrupcion
	reti
	end
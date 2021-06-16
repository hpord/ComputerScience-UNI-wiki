	bis.b #0x40,&P1DIR ; Se configura P1.3 como entrada (se pone a cero ) y P1.6(Led Verde) como salida (se ponse a 1).
	bis.b #0x08,&P1REN ; Habilita la resitencia si el pueto P1.3 esta configurado como entrada.
	mov.b #0x08,&P1OUT ; Hace pull-up en P1.3.
apagar bic.b #0x40,&P1OUT
	bit.b #0x08,&P1IN
	jnc loop
	jmp apagar
loop bit.b #0x08,&P1IN
	jc prender
	jmp loop
prender bis.b #0x40,&P1OUT
	bit.b #0x08,&P1IN
	jnc loop1
	jmp prender
loop1 bit.b #0x08,&P1IN
	jc apagar
	jmp loop1
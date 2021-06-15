           bis.b #0x41, &P1DIR
           mov.b #08h, &P1OUT
           bis.b #08h, &P1REN
	   mov.w #8, R5
regresa_1 bit.b #08h, &P1IN ;
           jc sin_presion
con_presion call #parp_red
	dec R5
	jnz regresa_1
regresa_2 bit.b #08h, &P1IN
           jc sin_pres_2;
con_pres_2 call #parp_green
	jmp regresa_2
sin_presion bis.b #0x41, &P1OUT
	jmp regresa_1
sin_pres_2 call #parpadeo_3
	jmp regresa_2


parp_red    bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	ret
parp_green bis.b #0x40, &P1OUT;
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bic.b #0x40, &P1OUT;
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	bis.b #0x01, &P1OUT;
	call #espera_1
	bic.b #0x01, &P1OUT
	call #espera_1
	ret
parpadeo_3 bis.b #0x01, &P1OUT;
	bic.b #0x40, &P1OUT;
	call #espera
	bic.b #0x01, &P1OUT
	bis.b #0x40, &P1OUT;
	call #espera
	ret
	espera mov.w #50500, R8
loop dec R8
	jnz loop
	ret
espera_1 mov.w #30000, R13
loop_1 dec R13
	jnz loop_1
	ret
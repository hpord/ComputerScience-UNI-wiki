SetupP1 mov.b #041h,&P1DIR ; P1.0 y P1.6 como salida
	mov.b #08h,&P1OUT ; P1.3 se pone a uno, sino cero //se pone como salida
	bis.b #08h,&P1REN
	mov.b #01h,&P1OUT
Mainloop bit.b #08h,&P1IN
	mov.b #49h,&P1OUT
	mov.b #48h,&P1OUT
	jc ON
OFF 	mov.b #004,R10
	call #parpadeo1
	jmp Mainloop ;
ON 	mov.b #08h,&P1OUT
	jmp Mainloop
parpadeo1 mov.b #08h,&P1OUT
	  call #espera
	  mov.b #48h,&P1OUT
	  call #espera
	  dec.b R10
	  jnz parpadeo2
	  ret

parpadeo2 mov.b #49h,&P1OUT
	  call #espera
	  mov.b #09h,&P1OUT
	  call #espera
	  dec.b R10
	  jnz parpadeo1
	  mov.b #004,R10
	  ret

espera mov.w #050000,R15 ;
L1 	dec.w R15 ;
	jnz L1 ;
	ret
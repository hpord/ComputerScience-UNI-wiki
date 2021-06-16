org 8000h
	
	
	lcall print
	db 0dh,0ah,"CONTADOR DE 59 HASTA 0",0dh,0ah,0
	mov A,#1
        mov B,#0
        lcall placeCur4
        lcall prtLCD4
        db "Contador: ",0
        mov A, #2
        mov B, #11
        lcall placeCur4
        mov R0, #offcur  ;Comando que oculta el cursor
        lcall wrLCDcom4

 menu:
	
	jnb P3.2,repite
	jnb P3.3,pausa
	
	sjmp menu
pausa:           ;PRESIONAR CON ALGO DE RETARDO PARA QUE RECONOZCA , PERO SI FUNCIONA
    jnb P3.2,reanuda
    ljmp pausa
    ret
  
repite:
 mov R5, #59
 mov R6, #60 ;llegara hasta 59 y en 60 se reinicia
 
loop:
 
   mov A, R5
   lcall threeDigits_dec_ascii
   mov R0, 30h
   lcall wrLCDdata4
   mov R0, 31h
   lcall wrLCDdata4
   mov R0, 32h
   lcall wrLCDdata4
   mov R0,#shLfCur  ;comando que desplaza el cursor a la izquierda
   lcall wrLCDcom4
   mov R0,#shLfCur  ;comando que desplaza el cursor a la izquierda
   lcall wrLCDcom4
   mov R0,#shLfCur  ;comando que desplaza el cursor a la izquierda
   lcall wrLCDcom4
   mov A, #11
   lcall positionNTerminal
   mov A, 30h
   lcall sndchr
   mov A, 31h
   lcall sndchr
   mov A, 32h
   lcall sndchr
   mov A, #0dh
   lcall sndchr
   lcall sdelay
   dec R5
   setb P3.3
   jnb P3.3,pausa
reanuda:
   djnz R6, loop
   sjmp repite
  
ljmp 2F0h
		
	
	
$INCLUDE(subrutinasLCD.inc)
	end

org 8000h
   mov tmod, #20h
   lcall inicioLCD
   ;mov a, #1
   ;mov dptr,#rutina_interrup_t0
  ; lcall setintvec
   lcall print
   db 0dh, 0ah, "INGRESE UN NUMERO ENTRE 0 Y 5 : ", 0ah,0
   lcall getbyt
   mov R6,A
   cjne A,#0, cero
   cjne A,#1, uno
   cjne A,#2, dos
   cjne A,#3, tres
   cjne A,#4, cuatro
   cjne A,#5, cinco
   ljmp 2F0h
   
cero:
  
    MOV A,#1
    MOV B,#0
    lcall placeCur4
    lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    ret
uno:
    lcall cero
    MOV A, #1
    MOV B, #3
    lcall placeCur4
    lcall extraer_numero
    mov 30h,A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    lcall extraer_numero
    mov 30h,A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    ret
dos:
    
    lcall uno
    MOV A,#1
    MOV B,#5
    lcall placeCur4
    lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    call extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    ret
  
tres:
    lcall tres
    MOV A,#1
    MOV B,#8
    lcall placeCur4
    lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
     lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    ret
    
cuatro:
    lcall tres
    MOV A,#2
    MOV B,#0
    lcall placeCur4
    lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
     lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    ret
    
cinco:
    lcall cuatro
    MOV A,#2
    MOV B,#4
    lcall placeCur4
    lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    lcall extraer_numero
    mov 30h, A
    MOV R0, 30h
    lcall prtLCD4
    lcall sndchr
    ret
      
extraer_numero:
	inc A
	movc A,@A+PC
	ret
	db 0,", ",1,", ", 8,", ",27,", ",64,", ",125
	ret

   $INCLUDE(subrutinasLCD.inc)
   end
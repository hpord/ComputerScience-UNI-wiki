sndchr equ 148h
print equ 136h
sdlay  equ 142h
display equ 11Bh
getbyt equ 11Eh
      org 8000h
      lcall print 
      db 0dh, 0ah, "Ingrese el numero ", 0ah, 0
      lcall getbyt
      cjne A, #0, continua
      ljmp 2f0h
continua:
   cjne  A, #1, sigue_calculando
   lcall print
   db 0dh, 0ah, "Serie de fino :", 0ah, 0
   mov A,#31h
   lcall sndchr
   mov A, #44
   lcall sndchr
   mov A,#1
   lcall display 
   cpl A
   mov P1,A
   ljmp 2f0h
sigue_calculando:
   clr C
   subb A,#2
   mov 30h, A
   lcall print
   db 0dh, 0ah, "Serie de fibo : ", 0ah, 0
   mov A, #31h
   lcall sndchr
   mov A, #44
   lcall sndchr
   mov A, #1
   lcall display
   cpl A
   mov P1, A
   lcall sdelay
   cpl A
   mov P1, A
   lcall sdelay   ;cada segundo
   mov A, #31h
   lcall sndchr
   mov A, #44
   lcall sndchr
   mov A,#1
   lcall display
   cpl A
   mov P1, A
   lcall sdelay
   mov R2, #1 ;r2 HACE LAS VECES DE A
   mov R3, #1 ;r3 hace las veces de B
   mov R5, 30h
   mov A, R5
   cjne A, A,#0, lazo
   ljmp 2f0h
lazo:
   mov a,r2
   mov a,r3
   mov r4, a
   mov a, r3
   mov r2, a
   mov a, r4
   mov r3, a
   mov a,r4
   mov b, #10
   div ab
   mov 35h,a
   mov 36h, b
   add a, #30h
   lcall sndchr
   mov a, 36h
   add a ,#30h
   lcall sndchr
   mov a,#44
   lcall sndchr
   mov a, #44
   lcall sndchr
   mov a,r4
   lcall display
   cpl a
   mov p1, a
   lcall sdelay  
   djnz r5, lazo
   ljmp 2f0h
   end
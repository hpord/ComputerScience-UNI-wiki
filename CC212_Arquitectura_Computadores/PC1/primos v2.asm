org 8000h
  lcall print
  db 0dh, 0ah, "Ingrese un numero : ",0ah, 0
  lcall getbyt
  mov 30h, A
  cjne A, #2, otroNumero
  sjmp SiPrimo
otroNumero:
  mov R2, #2 ; numero entre el cual es dividido
continua: 
  mov A, 30h
  mov B, r2
  div ab
  mov a,b
  cjne a, #0, sigue
  sjmp NoPrimo
sigue:
  inc r2
  mov a, r2
  cjne a, 30h, continua
  sjmp SiPrimo
NoPrimo:
   lcall print
   db 0dh, 0ah, "No es primo", 0dh, 0ah, 0
   mov a, #0c0h
   cpl a
   mov p1,a
   ljmp 2f0h
SiPrimo:
   lcall print 
   db  0dh, 0ah, "Es primo", 0dh, 0ah,0
   mov a, #73h
   mov p1, a
   ljmp 2f0h
   end
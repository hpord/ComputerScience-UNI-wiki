;factorial de 5
;enviar el resultado a terminal
print equ 136h
sndchr equ 148h
getbyt equ 11Eh
display equ 11Bh
   org 8000h 
   mov R3, #1
   mov R4, #1
   lcall print
   db 0dh, 0ah, "Ingrese a calcular del factorial: ",0ah, 0
   lcall getbyt ;5 faact
   mov 30h, A
   lcall display
   cpl A
   mov P1, A
   mov R5, 30h
lazo:
   mov A, R3
   mov B,R4
   mul AB
   mov R3, A
   inc R4
   djnz R5, lazo
   mov A, R3   ; resultado del factorial
   mov B,#100
   div AB     ;A <--4 B<--5
   mov 40h, A
   mov A, B
   mov A, #10
   div AB
   mov 41h, A
   mov 42H, B
   lcall print
   db 0dh, "El factorial es: ",0ah, 0
   mov A,40h
   add A,#30h    ; se convierte a ascii
   lcall sndchr  ; envia un caracter al terminal
   mov A, 41h
   add A,#30h
   lcall sndchr
   ;salto de linea
   mov A,#0dh
   lcall sndchr
   mov A, #0ah
   lcall sndchr
   ljmp 2F0h
   end
   
;112 overflows
display equ 118h
sndchr equ 148h
print equ 136h
    org 8000h
    mov tmod, #20h
    setb tr0
    
repite: 
   mov r4, #10
   mov r2, #9
   
 lazo:
    mov a, r2
    lcall display
    cpl a
    mov p1, a
    mov a, r2
    lcall decremento_digito_terminal
    lcall segundo   ; aqui se ha calculado el tiempo de 1 segundo para evitar usar sdelay
    dec r2
    djnz r4, lazo
    lcall print
    db 0dh, 0ah, "Ignicion ", 0dh, 0ah, 0
    sjmp repite
    ljmp 2f0h
 segundo:
    mov r6,#112
 loop:
    jnb tf0, $
    clr tf0
    djnz r6, loop
 decremento_digito_terminal:
    add A,#30h
    lcall sndchr
    mov a,#0dh
    lcall sndchr
    ret
    end
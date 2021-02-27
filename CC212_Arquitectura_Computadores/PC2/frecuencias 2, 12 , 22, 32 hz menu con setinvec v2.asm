;para una frecuencia de 2hz , usamos:
;periodo=0.5s, semip = 0.25
;k*8192*(12/11.0592*106)s = 0.04    k=4.5   k=5

org 8000
   mov tmod, #20h
   mov a, #1
   mov dptr,#rutina_interrup_t0
   lcall setintvec
   
menu:
   lcall print
   db 0dh, 0ah, "Menu de frecuencias", 0dh, 0ah
   db "01) 2hz",0dh, 0ah
   db "02)12 hz",0dh, 0ah
   db "03)22hz",0dh, 0ah
   db "04) 32hz ",0dh, 0ah
   db "05) salir ",0dh, 0ah
   db "Ingrese seleccion : ",0ah, 0
   lcall getbyt
   mov r6,a
   cjne a,#1, f12hz
f2hz:
    mov r7,#28     ;la cantidad de overflows
    setb tr0
    setb et0
    set ea
    sjmp menu
f12hz:
    cjne a, #2, f22hz
    mov r7, #5
    setb tr0
    setb et0
    set ea
    ajmp menu
f22hz:
    cjne a,#3, f32hz
    mov r7, #3
    setb tr0
    setb et0
    setb ea
    ajmp menu
f32:
    cjne a,#4, sale
    mov r7,#2
    setb tr0
    setb et0
    setb  ea
    ajmp menu
sale:
    clr ea
    clr  tr0
    lcall print 
    db 0dh, 0ah, "hasta la proxima ..", 0dh,0ah,0
    ljmp 2f0h
    
rutina_interrup_t0: 
    mov a,r6
    cjne a,#1,otro
frec2hz:
    dec r7
    cjne r7, #0, sale_interrupcion
    cpl p1.0
    mov r7,#28
    sjmp sale_interrupcion
otro:
    cjne a,#2,otro2
frec12hz:
    dec r7
    cjne r7,#0,sale_interrupcion
    cpl p1.0
    mov r7,#5
    sjmp sale_interrupcion
otro2:
    cjne a,#3,sale3
frec22hz:
    dec r7
    cjne r7,#0,sale_interrupcion
    cpl p1.0
    mov r7,#3
    
    sjmp sale_interrupcion
otro3:
    cjne a,#4, sale_interrupcion
frecc32hz:
    dec r7
    cjne r7,#0,sale_interrupcion
    cpl p1.0
    mov r7,#2
    sjmp sale_interrupcion
sale_interrupcion:
   reti
   end
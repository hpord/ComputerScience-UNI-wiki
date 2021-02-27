@se llena con valores de 0 a 99
.data
.balign 4
a:.skip 400   @es mi arreglo
.text
.global _start
_start:
    ldr r1,direccion
    mov r2,#10
loop:
    cmp r2,#110
    beq end
    add r3,r1,r2,LSL #2 /*r3<-- r1+(r2*4), 3000h 3004h 3008h 300Ch ...*/ 
    str r2,[r3]
    add r2,r2,#1   @incremento r2
    b loop  
end:
     sub r3,r3,#4
     ldr r2,[r3]
     sub r3,r3,#4
     ldr r4,[r3]
     add r1,r2,r4
     mov r0,r1
     mov r7, #1  @mediante el servicio 1 de sale del programa
     swi 0
direccion:
     .word a


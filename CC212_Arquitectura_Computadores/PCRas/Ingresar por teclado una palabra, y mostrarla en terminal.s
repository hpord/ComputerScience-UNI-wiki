@---p3.s---
@lectura desde el teclado
.text
.global _start
_start:
        mov r7,#3
        mov r0,#0
        mov r2,#11
        ldr r1,=mensaje
        swi 0
_write:
        mov r7,#4
        mov r0,#1
        ldr r1,=mensaje
        mov r2,#11
        swi 0
end:
        mov r7,#1
        swi 0
.data
mensaje:
        .ascii " "
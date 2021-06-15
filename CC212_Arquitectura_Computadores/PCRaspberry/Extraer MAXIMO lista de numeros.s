.org 0
.code 32
.text

_array : 
    .word 10,9,14,13,15
    .skip 512

_start : .global _start

    adr r0,_array
    ldr r5,=4
    ;ldr r3,=0
    ldr r1,[r0],#4
    mov r2,r1

loop : 
    ldr r1,[r0],#4
    cmp r2,r1
    blt loop1
    sub r5,r5,#1
    cmp r5,#0
    beq halt
    bgt loop
loop1:
    mov r2,r1
    sub r5,r5,#1
    cmp r5,#0
    beq halt
    bgt loop    

halt: b halt
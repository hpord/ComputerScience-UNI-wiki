@ ---- Added ----
@ bubblesort2.s
@
@ pi@RPi3:~ $ as -o bubblesort2.o bubblesort2.s
@ pi@RPi3:~ $ gcc -o bubblesort2 bubblesort2.o
@ pi@RPi3:~ $ ./bubblesort2; echo $?

.data

table:
  .word 9, -8, -7, 6, -5, 4, -3, 2, -1, 0, 127, 128
aft_table:

.balign 4
n:
  .word (aft_table - table) >>2
@ ---------------

@ ---- Added ----
.balign 4             @ Prt
frmt:                 @ Prt
  .asciz "%d  "       @ Prt

.balign 4
flags:                @ RDmp
  .word 0             @ RDmp
msg:                  @ RDmp
  .asciz "NZCV  2> 6= 8<\n"  @ RDmp
aft_msg:              @ RDmp
                      @ RDmp
l_msg:                @ RDmp
  .word (aft_msg - msg) - 1  @ RDmp
@ ---------------

.text
.global main
.global printf, putchar  @ Prt
main:
     push  {r4-r10, lr}
     ldr   r1, =n
     ldr   r1, [r1]       @ len(table) in r1
     bl    Print          @ Prt
@ ---------------

bubblesort:
      @ maybe r0, r1 for table and counter (rest is based on that)
      @ r8 = Buffer for Value
      @ r4 = Counter for loop1
      @ r5 = Register for Value
      @ r7 = Register for Value
      @ r1 = Size of Array
      @ r0 = Address of the 1. Element
      @ r10 = "swapped" register

loop:
     mov r10, #0
     sub r1, #1            @ Decrement Counter for loop

@ ---- Added ----

   ldr   r0, =table
   mov   r4, #1      @ i = 1   i could = 0, if instructions
                     @ cmp r4, r1   @ compare r4 and r1
                     @ add r4, #1   @ Increment counter for loop1
                     @ were reversed
@ ---------------

     loop1:

            ldr r5, [r0]
            ldr r7, [r0, #4]

            cmp r5, r7

                  movgt r8, r7
                  movgt r7, r5
                  movgt r5, r8
                  strgt r5, [r0]
                  strgt r7, [r0, #4]
                  movgt r10, #1

@ ---- Added ----
                  add   r0, #4   @ Index table to next position
@ ---------------

            cmp r4, r1   @ compare r4 and r1
            add r4, #1   @ Increment counter for loop1
            blt loop1    @ is r4 < r1 ? yes = go to loop1

@ ---- Added ----
     bl    Print         @ Prt
     bl    RDmp          @ RDmp
@ ---------------

     cmp r10, #1
     beq loop

@ ---- Added ----

exit:
   pop   {r4-r10, lr}
   mov   r0, #0         @ good return code
   bx    lr             @ Exit with gcc linker

@ ---------------

@ ---- Added ----

 Print:                  @ Prt, table to stdout
    push  {r0-r10, lr}   @ Prt
    mrs   r10, cpsr      @ Prt
    ldr   r2, =n         @ Prt
    ldr   r2, [r2]       @ Prt
    ldr   r3, =table     @ Prt
 lp:                     @ Prt
    ldr   r0, =frmt      @ Prt
    ldr   r1, [r3], #4   @ Prt
    push  {r0-r3}        @ Prt
    bl    printf         @ Prt
    pop   {r0-r3}        @ Prt
    subs  r2, #1         @ Prt
    bne   lp             @ Prt
    mov   r0, #0xa       @ Prt
    bl    putchar        @ Prt
    msr   cpsr_f, r10    @ Prt
    pop   {r0-r10, lr}   @ Prt
    mov   pc, lr         @ Prt
@ ---------------

@ ---- Added ----
RDmp:                   @ RDmp
   push   {r0-r10, lr}  @ RDmp
   mrs    r10, cpsr     @ RDmp
   push   {r8-r11}      @ RDmp
   push   {r4-r7}       @ RDmp
   push   {r0-r3}       @ RDmp
                        @ RDmp
   ldr    r1, =flags    @ RDmp
   mrs    r0, cpsr      @ RDmp
   str    r0, [r1]      @ RDmp
   b      seq           @ RDmp
                        @ RDmp
p_char:                 @ RDmp
   push   {r0-r4, lr}   @ RDmp
   bl     putchar       @ RDmp
   pop    {r0-r4, lr}   @ RDmp
   mov    pc, lr        @ RDmp
                        @ RDmp
register:               @ RDmp
   mov    r1, #0        @ RDmp
   push   {r0, lr}      @ RDmp
                        @ RDmp
nibble:                 @ RDmp
   mov    r2, r3        @ RDmp
   lsl    r2, r1        @ RDmp
   lsr    r2, #28       @ RDmp
   add    r2, #48       @ RDmp
   cmp    r2, #58       @ RDmp
   addge  r2, #39       @ RDmp
   mov    r0, r2        @ RDmp
   bl     p_char        @ RDmp
   add    r1, #4        @ RDmp
   cmp    r1, #32       @ RDmp
   blt    nibble        @ RDmp
   mov    r0, #32       @ RDmp
   bl     p_char        @ RDmp
   pop    {r0, lr}      @ RDmp
   mov    pc, lr        @ RDmp
                        @ RDmp
manage:                 @ RDmp
   push   {r0, lr}      @ RDmp
   mov    r3, r4        @ RDmp
   bl     register      @ RDmp
   mov    r3, r5        @ RDmp
   bl     register      @ RDmp
   mov    r3, r6        @ RDmp
   bl     register      @ RDmp
   mov    r3, r7        @ RDmp
   bl     register      @ RDmp
   pop    {r0, lr}      @ RDmp
   mov    pc, lr        @ RDmp
                        @ RDmp
seq:                    @ RDmp
   pop    {r4-r7}       @ RDmp
   bl     manage        @ RDmp
   mov    r0, #32       @ RDmp
   bl     p_char        @ RDmp
   pop    {r4-r7}       @ RDmp
   bl     manage        @ RDmp
   mov    r0, #0x0a     @ RDmp
   bl     p_char        @ RDmp
                        @ RDmp
   pop    {r4-r7}       @ RDmp
   bl     manage        @ RDmp
   mov    r0, #32       @ RDmp
   bl     p_char        @ RDmp
   ldr    r3, =flags    @ RDmp
   ldr    r3, [r3]      @ RDmp
   bl     register      @ RDmp
                        @ RDmp
   ldr    r2, = l_msg   @ RDmp
   ldr    r2, [r2]      @ RDmp
   ldr    r1, =msg      @ RDmp
w_msg:                  @ RDmp
   ldr    r0, [r1], #1  @ RDmp
   bl     p_char        @ RDmp
   subs   r2, #1        @ RDmp
   bgt    w_msg         @ RDmp
   msr    cpsr_f, r10   @ RDmp
   pop    {r0-r10, lr}  @ RDmp
   mov    pc, lr        @ RDmp
@ ---------------
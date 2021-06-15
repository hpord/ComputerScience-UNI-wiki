.syntax unified

.equ limit,10000
.equ limit4,40000

.align 4

number     .req r4
count      .req r5
numprimes  .req r6
primes_ptr .req r7

.section .bss
.lcomm primes_vector,limit4 @ sufficient for 10000 32-bit ints

.section .rodata
 .align 2
resstring:
 .asciz "%d\n"
.text
 .align 2
 .global main
 .type main, %function
main:
 stmfd sp!, {r4-r7, lr}

 ldr     primes_ptr, =primes_vector
 mov     numprimes, 1
 mov     number, 2
 str     number, [primes_ptr]

 ldr count, =limit
 mov number, 3                                 @ 2 is the first prime
loop:
 mov     r0, number
 ldr     r1, =primes_vector
 mov     r2, numprimes
 bl      prime_vector
 teq     r0, 1
 bne     nexti
 str     number, [primes_ptr, numprimes, lsl 2]
 add     numprimes, numprimes, 1
 subs count, count, 1
 beq printme
nexti:
 add number, number, 2
 b loop
 
printme:
 mov r1, number
 ldr r0, =resstring                            @ store address of start of string to r0
 bl printf

 mov r0, 0
 ldmfd sp!, {r4-r7, pc}
 mov r7, 1                                     @ set r7 to 1 - the syscall for exit
 swi 0                                         @ then invoke the syscall from linux
prime_vector.s


.syntax unified
.equ word, 4

@ this subroutine returns 1 if the passed number is prime; 0 if not
@
@ inputs
@   r0 - integer to test
@   r1 - pointer to vector of prime integers smaller than r0
@   r2 - length of vector passed in r1

@ outputs
@   r0 - prime boolean

number   .req r4
vptr     .req r5
tmp      .req r6
squared  .req r7
vsize    .req r8

.global prime_vector
.type prime_vector, %function
.text
.align 2

prime_vector:
 stmfd sp!, {r4-r8, lr}
 mov number, r0
 mov vptr, r1
 mov vsize, r2
nexti:
 ldr tmp, [vptr], word
 mul squared, tmp, tmp
 cmp squared, number    @ check if vector element squared is greater than test number
 movgt r0, 1              @ if so test numer is prime so leave
 bgt last
 mov r0, number
 mov r1, tmp
 bl divide             @ divide number by vector element - if no remainder
 teq r1, 0              @ it is not prime so leave
 moveq r0, 0
 beq last
 subs vsize, vsize, 1    @ check next element
 bgt nexti
 mov r0, 0
last:
 ldmfd sp!, {r4-r8, pc}
divide.s


.syntax unified
@ divide takes value in r0, divisor in r1 and returns dividend in r0 and modulus in r1 
 .global divide
 .type divide, %function
divide:
        stmfd   sp!, {lr}
@ see http://infocenter.arm.com/help/topic/com.arm.doc.ihi0043d/IHI0043D_rtabi.pdf
 bl __aeabi_uidivmod
 ldmfd   sp!, {pc}
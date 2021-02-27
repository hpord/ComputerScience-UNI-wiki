        .section .rodata
        .align 2
scanner:
        .string "%d"
        .align 2
printer:
        .string "The average of the numbers is: %d + %d/%d\n"
instructions:
        .string "Type numbers to average, seperated by newlines.\n"
        
        .data
        .align 2
        
        .text
        .align 2
        .arm
        
        .type avg, %function
avg:
        @ Pointer to array in r0, array size in r1
        push {lr}
        mov lr, #0
        mov r2, #0
.Lavg_top:       
        cmp r1, #0
        ble .Lavg_ret
        ldr r3, [r0], #4
        add r2, r2, r3
        sub r1, r1, #1
        add lr, lr, #1
        b .Lavg_top
.Lavg_ret:
        mov r1, lr
        mov r0, r2
        bl div
        pop {lr}
        bx lr

        .type div, %function
        @ int, int div(int n, int d)
        @ quotient in r0, remainder in r3
div:
        push {lr}
        mov r2, #0
div_top:
        subs r0, r0, r1
        bmi div_end
        add r2, r2, #1
        b div_top
div_end:
        add r0, r0, r1
        mov r3, r0
        mov r0, r2
        pop {lr}
        bx lr

        .globl main
        .type main, %function
main:
        ldr r0, =instructions
        bl printf
        mov r6, #50
        mov r5, #0
        mov r0, r6
        mov r0, r0, lsl #2
        bl malloc
        mov r4, r0
        @ pernament pointer to start of allocated memory
        @ don't touch
        mov r9, r0
scan_loop_top:
        ldr r0, =scanner
        push {r0}
        mov r1, sp
        bl __isoc99_scanf
        pop {r7}
        cmp r0, #1
        bne scan_loop_end
        str r7, [r4], #4
        add r5, r5, #1
        cmp r5, r6
        bge scan_realloc
        b scan_loop_top
scan_realloc:
        mov r8, r6
        mov r6, r6, lsl #1
        mov r1, r6
        mov r1, r1, lsl #2
        mov r0, r9
        bl realloc
        mov r9, r0
        mov r4, r9
        mov r8, r8, lsl #2
        add r4, r4, r8
        b scan_loop_top
scan_loop_end:
        mov r0, r9
        mov r1, r5
        bl avg
        mov r1, r0
        mov r2, r3
        mov r3, r5
        ldr r0, =printer
        bl printf
        mov r0, r9
        bl free
        mov r0, #0
        mov r7, #1
        swi #0
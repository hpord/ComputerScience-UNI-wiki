/* -- loop01.s */
.text
.global main
main:
    mov r1, #0       /* r1 ← 0 */
    mov r2, #1       /* r2 ← 1 */
loop: 
    cmp r2, #22      /* compare r2 and 22 */
    bgt end          /* branch if r2 > 22 to end */
    add r1, r1, r2   /* r1 ← r1 + r2 */
    add r2, r2, #1   /* r2 ← r2 + 1 */
    b loop
end:
    mov r0, r1       /* r0 ← r1 */
    bx lr


@Programa que sume 1+2++3...+22=253
.text
.global _start



_start:
	mov r1,#0
	mov r2,#1
loop:
	cmp r2,#22
	bgt end
	add r1,r1,r2	@r1=r1+r2
	add r2,r2,#1	@Incrementar el valor de r2
	b loop


end:
	mov r0,r1		
	mov r7, #1	@mediante  el servicio 1 sale del programa. servicio de Sycall
	SWI 0



.text
.global _start
_start:
    mov r1,#0
    mov r2,#1
loop:
    cmp r2,#22
    bgt end
    add r1,r1,r2  @r1=r1+r2
    add r2,r2,#1  @incrementar el valor de r2
    b loop
end:
     mov r0,r1
     mov r7, #1  @mediante el servicio 1 de sale del programa
     swi 0
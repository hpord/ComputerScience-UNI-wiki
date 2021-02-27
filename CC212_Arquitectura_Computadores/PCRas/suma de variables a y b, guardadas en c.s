//p6.s
//Suma de las variables a y b. c=a+b
.data
a: .word 33
b: .word 55
c: .word 0 @contendra la suma de a y b. Esto es a+b
.text
.global _start



_start:
	ldr r1,=a		//carga la direccion de a a r1
	ldr r1,[r1]		//carga el valor de a a r1
	ldr r2,=b		@carga la direccion de b a r2
	ldr r2,[r2]		@carga el valor de b a r2
	add r0, r1, r2 		/* r0 <- r1 + r2 */
	ldr r2,=c
	str r0,[r2]		@almaceno el valor de r0 en c
	mov r7, #1		@mediante  el servicio 1 sale del programa. servicio de Sycall
	SWI 0

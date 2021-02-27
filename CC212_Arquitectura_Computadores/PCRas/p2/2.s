.data
a: .word 0xEEBB88DD
b: .word 0xF8001162


.text
.global _start
_start:
	mov r7,#4	@servicio 4 del system call(API permite poder ingresar dese el 
			@teclado y visualizar en la pantalla)
	mov r0,#1	@file(stdout).salida a monitor
	ldr r1,=mensaje	@carga el registro con la direccion de la cadena
	mov r2,#33	@longitud del mensaje
	svc #0
calculo:
	ldr r1,=a
	ldr r1,[r1]
	ldr r2,=b
	ldr r2,[r2]
	cmp r1,r2
	bgt resultado
	mov r0,#2
	b end
resultado:
	mov r0,#1

end:
	mov r7,#1	@servicio 1 del system call quen indica salida del programa
	swi 0
.data
mensaje:
	.ascii "Calculo del menor de dos numeros\n"

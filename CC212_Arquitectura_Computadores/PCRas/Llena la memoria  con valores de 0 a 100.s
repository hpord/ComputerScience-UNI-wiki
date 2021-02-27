@Llenado de ciertas posiciones de memoria
@Se llenan con valores de 0 a 99
.data
.balign 4
a: .skip 400 @ Es mi arreglo
.direccion: .word
.text
.global _start



_start:
	ldr r1,direccion  @carga la direccion de "direccion" a r1
	mov r2,#0
loop:
	cmp r2,#100	@comparar
	beq end
	add r3,r1,r2,LSL #2 	/*r3<-- r1+(r2*4)*/
	str r2,[r3]	@almaceno
	add r2,r2,#1	@incremento en 1
	b loop		@termina el loop


end:
	sub r3,r3
	ldr r1,[r3]
	mov r0,r1		
	mov r7, #1	@mediante  el servicio 1 sale del programa. servicio de Sycall
	SWI 0

direccion: .word a



@se llena con valores de 0 a 99
.data
.balign 4
a:.skip 400   @es mi arreglo
.text
.global _start
_start:
    ldr r1,direccion
    mov r2,#0
loop:
    cmp r2,#100
    beq end
    add r3,r1,r2,LSL #2 /*r3<-- r1+(r2*4), 3000h 3004h 3008h 300Ch ...*/ 
    str r2,[r3]
    add r2,r2,#1   @incremento r2
    b loop  
end:
     sub r3,r3,#8
     ldr r1,[r3]
     mov r0,r1
     mov r7, #1  @mediante el servicio 1 de sale del programa
     swi 0
direccion:
     .word a


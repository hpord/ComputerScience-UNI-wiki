@programa que calcule el mayor valor de dos numeros 0xAABBCCDD y 0xFF0011BB
@si r0=1 entonces el primero valor es mayor que el segundo
@si r0=2 entonces el segundo valor es mayor que el primero
.data
a: .word 0xAABBCCDD
b: .word 0xFF0011BB
.text
.global _start
_start:
     ldr r1,=a  @carga la direccion de a a r1
     ldr r1,[r1] @carga el valor de a a r1
     ldr r2,=b   @carga la direccion de b a r2
     ldr r2,[r2] @carga el valor de b a r2
     cmp r1, r2 
     bgt resultado
     mov r0,#2
     b end
resultado:
     mov r0,#1
      
end:
     mov r7, #1  @mediante el servicio 1 de sale del programa
     swi 0
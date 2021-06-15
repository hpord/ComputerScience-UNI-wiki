.text
.global _start
_start: 
        
 	MOV R0,#23               @Numero que desea probar
	CMP R0,#01               @Comparando con 1
 	BEQ PRIME                @Si son iguales, se declara como primo
	CMP R0,#02               @Comparando con 2
 	BEQ PRIME                @Si son iguales se declara como primo
 	MOV R1,R0                @Copia el número en R1
 	MOV R2,#02               @Divisor inicial

UP:                     
 BL DIVISION              @Llama a la subrutina division
 CMP R8,#00               @Compara el resto con 0
 BEQ NOTPRIME             @Si son iguales entonces no es primo
 ADD R2,R2,#01            @Si no, incrementa el divisor y comprueba
 CMP R2,R1                @Comparar divisor con el numero de prueba
 BEQ PRIME                @Si todos los numeros son hechos significa que es primo
 B UP                     @Si no se repite hasta el final

NOTPRIME:
 
 LDR R3,=0x11111111       @Declarando al numero de prueba como no primo
 mov r7,#4	@servicio 4 del system call(API permite poder ingresar dese el 
			@teclado y visualizar en la pantalla)
 mov r0,#1	@file(stdout).salida a monitor
 ldr r1,=mensaje1	@carga el registro con la direccion de la cadena
 mov r2,#23	@longitud del mensaje
 svc #0
 B END                    @Finalizando el programa

PRIME: 
 LDR R3,=0xFFFFFFFF       @Declarando el numero de prueba como primo
 mov r7,#4	@servicio 4 del system call(API permite poder ingresar dese el 
			@teclado y visualizar en la pantalla)
 mov r0,#1	@file(stdout).salida a monitor
 ldr r1,=mensaje2	@carga el registro con la direccion de la cadena
 mov r2,#23	@longitud del mensaje
 svc #0
 B END

DIVISION:
	                  @Funcion para la operacion division
 MOV R8,R0                @Copia de el numero a evaluar de la funcion principal
 MOV R9,R2                @Copia del divisor desde la funcion principal

LOOP:                     
 SUB R8,R8,R9             @Restas sucesivas para la division
 ADD R10,R10,#01          @Contador para mantener el resultado de la division
 CMP R8,R9                @Compara el resultado distinto de cero
 BPL LOOP                 @Repite el bucle si todavia se necesita restar
 MOV PC,LR                @Retorna a la funcion principal
 
END:
  mov r7, #1   @servicio 1 de system call que indica salida del programa
  swi 0

.data
mensaje1:
	.ascii "El numero no es primo\n"

.data
mensaje2:
	.ascii "El numero si es primo\n"
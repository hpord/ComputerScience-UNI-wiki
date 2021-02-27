@p1.s
.text
.global _start
_start:
        mov r7,#4 ;@servicio 4 del sytem call(API QUE PERMITE INGRESAR DESDE TECLADO
                  ;@Y VISUALIZAR EN LA PANTALLA
        mov r0, #1  ;@file(stdout) Salida a monitor
        ldr r1, =mensaje; @carga el registro con la drección de la cadena
        mov r2, #38   ; @longitud del mensaje (hasta que posición se va a mostrar
        svc #0
end:
        mov r7, #1   ;@servicio 1 de system call que indica salida del programa
        swi 0        ;@detiene el prgrama

.data
mensaje:
        .ascii "Hola mundo!!!\n\tBienvenido al ARM"
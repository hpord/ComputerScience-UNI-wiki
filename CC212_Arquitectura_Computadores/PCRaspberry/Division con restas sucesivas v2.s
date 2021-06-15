 CMP             R2, #0
 CMP             R2, #0
 BEQ divide_end
@ compruebe si hay división entre cero!

 MOV      R0,#0     @borrar R0 para acumular el resultado
 MOV      R3,#1     @establecer el bit 0 en R3, que será
                    @desplazado a la izquierda y luego a la derecha
.text
.global _start

_start:
 CMP      R2,R1
 MOVLS    R2,R2,LSL#1
 MOVLS    R3,R3,LSL#1
 BLS      _start
 @desplazar R2 hacia la izquierda hasta que esté a punto de
 @ser más grande que R1
 @desplazar R3 a la izquierda en paralelo en orden
 @para marcar qué tan lejos tenemos que ir

next:
 CMP       R1,R2      
		      @conjunto de carry si R1> R2 (no pregunte por qué)
 SUBCS     R1,R1,R2   @restar R2 de R1 si esto fuera
                      @dar una respuesta positiva
 ADDCS     R0,R0,R3   @y agregue el bit actual en R3 a
                      @la respuesta acumulada en R0

 MOVS      R3,R3,LSR#1     @Desplazar R3 a la derecha en llevar bandera
 MOVCC     R2,R2,LSR#1     @y si el bit 0 de R3 era cero, también
                           @desplazar R2 a la derecha
 BCC       next            @Si el carry no está vacio, R3 ha cambiado
                           @de vuelta a donde comenzó, y nosotros
                           @podemos finalizar

.divide_end
 @MOV       R25, R24        @salida de la rutina
	mov r7,#1
        swi 0
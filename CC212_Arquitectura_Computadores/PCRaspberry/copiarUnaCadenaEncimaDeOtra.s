 	@AREA Copy, CODE, READONLY
 	ENTRY @marcar la primera instrucción para llamar

start 	LDR r1, =srcstr @ Puntero hacia la primera cadena
 	LDR r0, =dststr @ Puntero hacia la segunda cadena

strcopy @ copiar la primera cadena en segundo lugar
 	LDRB r2, [r1],#1 @ carga byte y actualiza la direccion
 	STRB r2, [r0],#1 @ almacena byte y actualiza la direccion
 	CMP r2, #0 @ comprobar si hay cero terminador
 	BNE strcopy @ seguir adelante si no
stop
 	SWI 0x11 @ Terminar

 	AREA Strings, DATA, READWRITE
srcstr 	DCB "First string - source",0
dststr 	DCB "Second string - destination",0
 
	END
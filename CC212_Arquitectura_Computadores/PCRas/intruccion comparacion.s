@Instrucciones de comparacion:cmp r1,r2
@Instrucciones de salto condicional: BEQ, salta si ambos registros son iguales
@Instrucciones de salto condicional: BGT, salta si R1 es mas grande que R2
@Instrucciones de salto condicional: BGE, salta si R1 es mayor o igual que R2
.text
.global _start



_start:
	mov r1,#66
	mov r2,#36
	cmp r1,r2
	@beq son_iguales
	bge son_iguales
es_menor:
	mov r0,#0
	b end
es_mayor:
	mov r0,#2
	b end
son_iguales:
	mov r0,#1

	
end:
	mov r7, #1		@mediante  el servicio 1 sale del programa. servicio de Sycall
	SWI 0

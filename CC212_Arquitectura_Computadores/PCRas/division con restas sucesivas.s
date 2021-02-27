 MOV R1, # 128		@ dividir R1
 MOV R2, # 4		@por R2
 MOV R0, # 0		@ inicializar contador
.subtract
 SUBS R1, R1, R2	@ restar R2 de
                        @ R1 y tienda 
               		@ resultado de nuevo en
                   	@ R1 configurando banderas
 ADD 	R0, R0, # 1	@ agregue 1 al contador,
                   	@ NO establecer banderas
 BHI	substract	@ ramificar al inicio de
                   	@ condición de bucle
                   	@ Superior, es decir, R1 es
                   	@ aún mayor que
                   	@ R2. Responda ahora en R0
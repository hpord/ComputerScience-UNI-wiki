 
.text
.global _start
_start:
      mov r0,#10
      mov r1,#96
      mov r2,#66
      cmp r1,r2        @comparo r1 con r2. significa tres cosas si r1<r2, r1>r2 o r1=r2
      ADDNE r0, r1, r0 @r0=r1+r0   r0:= r1 +r0 - r2 
      SUBNE r0, r0, r2 @r0=r1-r0   
son_iguales:
      @mov r0,#1
end:
     mov r7, #1  @mediante el servicio 1 de sale del programa
     swi 0
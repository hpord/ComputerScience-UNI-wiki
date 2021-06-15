org 8000h
   clr it0    ;configuro para que considere el nivel bajo
   mov a,#0   ;seleccion interrupcion externa 0
   mov dptr,#rutina_interrup_ext0
   lcall setintvec
   setb ex0     ;habilita la int. ext 0
   setb ea      ;hab. las int. globales
   setb p3.2
   setb p1.0      ;inicialmente el led estaba apagado
   sjmp $         ;salta a ais mismo
rutina_interrup_ext0:
   clr ex0      ;deshabilita la interrupcion
   mov a,#100   ;100 mils de retardo
   lcall delay
   cpl p1.0
   mov a,#200    ;200 mls de retardo
   lcall delay
   setb ex0      ;habilita la interrupcion
   reti
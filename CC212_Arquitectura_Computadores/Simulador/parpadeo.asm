org 0h
Inicio: 
  clr p1.0
  lcall retardo
  
  setb p1.0
  lcall retardo
  sjmp Inicio

retardo:
  mov r1, #5
 loop:
   djnz r1, loop
   ret
end
  
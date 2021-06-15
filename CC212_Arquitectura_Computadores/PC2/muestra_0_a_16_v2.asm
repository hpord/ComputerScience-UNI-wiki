sdelay equ 142h
delay equ 118h
getbyt equ 11eh
sndchr equ 148h
print equ 136h
prthex equ 13fh
binasc equ 109h
getchr equ 121h
ascbin equ 100h
setintvec equ 145h  
display equ 11bh  
       org 8000h
       clr it0
       mov a, #0
       mov dptr, #RutinaInterrExt0
       lcall setintvec
       setb ex0
       setb ea
       setb p3.2
repite:
      mov r3, #16
      mov r2, #0
otra_vez:
      mov a,r2
      lcall display
      cpl a
      mov p1,a
      lcall sdelay
      inc r2
      djnz r3,otra_vez
      sjmp repite
RutinaInterrExt0:
   push acc
   clr ex0
   mov a,#100
   lcall delay
   lcall print
   db 0dh, 0ah, "Interrumpcion en proceso",0dh, 0ah,0
   mov a,#200
   lcall delay
   setb ex0
   pop acc
   reti 
   end
   
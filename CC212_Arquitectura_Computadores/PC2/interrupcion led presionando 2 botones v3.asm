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
  mov tmod ,#20h
  mov a,#1
  mov dptr ,#rutina_interrup_t0
  lcall setintvec
  clr it0
  clr it1
  mov a,#0
  mov dptr,#RutinaInterr0
  lcall setintvec
  mov a,#2
  mov deptr,#RutinaInterr1
  lcall setintvec
  setb ex0
  setb ex1
  setb ea
  setb p3.2
  setb p3.3
f2hz:
  mov r7,#28  ; la cantida de overflows
  setb tr0
  setb et0
  mov r4, #16
  mov r5, #0
repite:
 lcall getchr
 cjne a,#3, continua
 clr ex0
 clr ex1
 clr ea
 lcall print
 db 0dh, 0ah, "Ctl-C ha sido presionado, bye", 0dh, 0ah, 0
 ljmp 2f0h
continua:
 sjmp repite:
rutina_interrup_t0:
  push acc
  dec r7
  cjne r7, #0,sale_interrupcion
  cpl p1.0
  mov r7,#28
  mov a,r5
  lcall prthex
  mov a,#0dh
  lcall sndchr
  inc r5
  dec r4
  mov a,r4
  cjne a,#0, sale_interrupcion
  mov r4, #16
  mov r5, #0
sale_interrupcion:
  pop acc
  reti
RutinaInterr0:
  clr ex0
  mov a,#100
  lcall delay
  push acc
  lcall print
  db 0dh, 0ah, "La imterrupcion viene del boton p3.2", 0dh, 0ah
  db 0dh, 0ah, "Si desea salir del programa presione ctl-c",0dh, 0ah,0
  mov a,#200
  lcall delay
  pop acc
  setb ex0
  reti
RutinaInterr1:
  clr ex1
  mov a,#100
  lcall delay
  push acc
  lcall print 
  db 0dh, 0ah,"La interrupcion viene del boton p3.3, es p3.3 ok?", 0dh, 0ah,0
  mov a,#200
  lcall delay
  pop acc
  setb ex1
  reti end
  end
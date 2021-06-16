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
   mov a,#0
   mov dptr ,#RutinaInterrExt0
   lcall setintvec
   setb ex0
   setb ea
   setb p3.2
repite:
	mov r5,#20
	lcall getchr
	cjne a,#3,noCtlC  ;Si ingresa ctr C sale del programa
	clr ex0
	clr ea
	lcall print 
	db 0dh, 0ah," Hasta pronto ",0dh, 0ah, 0
	ljmp 2f0h
noCtlC:
    sjmp repite
RutinaInterrExt0:
     pop acc
     clr ex0
     mov a,#100
     lcall delay
     lcall print
     db 0dh, 0ah, "Me estas tocando :v ,voy a multiplicar dos numeros", 0dh, 0ah, 0
     mov a, r5
     mov b, #10
     mul ab
     mov 30h,a
     lcall print
     db 0dh, 0ah, "El resultado es.. ",0ah, 0
     mov a,30h
     lcall prthex
     lcall print
     db 0dh, 0ah,0
     mov a,#200
     lcall delay
     setb ex0
     pop acc
     reti
     end
           
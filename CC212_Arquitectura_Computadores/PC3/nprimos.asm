binasc equ 109h
sdelay equ 142h
sndchr equ 148h 
getbyt equ 11Eh 
      org 8000h  
repite:
        lcall inicioLCD
 	mov a, #1 	
 	mov b, #0 	
 	lcall placeCur4  
 	mov R3,#2
 	mov R0,#offCur    
 	lcall wrLCDcom4 ;lee contenido del registro 0
repite2:
        mov a, #1 	
 	mov b, #0 	
 	lcall placeCur4 	
primos:
        mov A,R3
 	lcall dos_digitos_decimales
 	mov R0,30h 	
 	lcall wrLCDdata4
 	mov R0,31h
 	lcall wrLCDdata4
 	mov A,#100
 	lcall sdelay
constante:
        inc R3
        mov R1,#2 	
primos_1:
        mov A,R3
        mov B,R1
        div AB
        mov A,B
        cjne A,#0,siprimo
        sjmp noprimo
noprimo:
        cjne R3,#40,constante
        sjmp salir
siprimo:
        inc R1
        mov A,R1
        mov 30h,R3
        cjne A, 30h, primos_1
        sjmp repite2
        ;div AB
        ;mov A,B
        ;cjne A,#1,primos_1
        ;sjmp repite2
                 	
dos_digitos_decimales:
	mov B,#10
	div AB
	add A,#30h
	mov 30h,A
	mov A,B
	add A,#30h
	mov 31h,A
	ret 
salir:
        ljmp 2F0h	                          
$INCLUDE(subrutinasLCD.inc)
	end
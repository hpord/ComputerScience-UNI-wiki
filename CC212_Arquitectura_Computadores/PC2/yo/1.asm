setintvec equ 145h
delay 	 equ 118h
sdelay   equ 142h
crlf	 equ 115h
display  equ 11Bh
print	 equ 136h
	org 8000h
	         ;Habilita la interrupcion externa 0
	clr IT0 ;fijamos la interrupcion externa sensible en el nivel bajo
	mov a,#0
	mov dptr,#ISR0
	lcall setintvec
	setb EX0
	setb P3.2
                        ;habilita la interrupcion externa 1
	
	clr IT1		;fijamos la interrupcion externa sensible en el nivel bajo
	mov a,#2
	mov dptr,#ISR1
	lcall setintvec
	setb EX1
	setb EA
	setb P3.3
		
repite1: 
	setb P1.0
	mov A,#200
	lcall delay
	clr P1.0
	mov A,#200
	lcall delay 
	sjmp repite1
	
ISR0:
	clr EX0
	push acc
	mov R5,#10
	mov R7,#0
	lcall aumento
	lcall crlf
	pop acc
	setb EX0
	reti
	
aumento:
	mov A,R7
	lcall display
	cpl A
	mov P1,A
	lcall sdelay
	inc R7
	djnz R5,aumento
	sjmp again

again:
	mov R5,#10
	mov R7,#0
	lcall aumento
	ret
	
ISR1:
	clr EX1
	push acc
	lcall decremento
	lcall crlf
	pop acc
	setb EX1
	reti
	
decremento:
	mov R7,A
	lcall display
	cpl A
	mov P1,A
	lcall sdelay
	dec R7
	djnz R5,decremento
	sjmp again2
again2:
         mov R5, #10
         mov R7, #0
         lcall decremento
         ret
	end
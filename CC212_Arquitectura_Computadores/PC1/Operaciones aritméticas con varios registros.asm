;3
display equ 11Bh
	org 8000h
	mov A,#20         ;T
	mov B,#10	  ;U
	mul AB		; TXU
	mov 40h,A
	mov A,#30	;V
	mov B,#15        ;W
	div AB		;V/W
	mov 41h,A
	mov R2,#200	;X	
	mov R3,#2	;Y
	mov R4,#5 	;Z
	mov R0,40h
	mov R1,41h
	mov A,R0
	add A,R1
	subb A,R2
	add A,R3
	add A,R4					
	mov 30h,A
	lcall display
	cpl A
	mov P1,A
	ljmp 2F0h
	end	
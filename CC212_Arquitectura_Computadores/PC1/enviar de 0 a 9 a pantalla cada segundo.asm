;Hacer un programa que envíe por el puerto serie dígitos decimales de 0 a 9 cada segundo
display equ 11Bh
sndchr	equ 148h
print	equ 136h
	org 8000h
	mov TMOD,#21h
repite:
	mov R4,#10
	mov R2,#0
lazo:
	mov A,R2
	lcall display
	cpl A
	mov P1,A
	mov A,R2
	lcall digito_al_terminal
	lcall segundo
	inc R2		;inc : incremento
	djnz R4,lazo
	sjmp repite
segundo:
	mov R6,#14
loop:
	jnb TF0,$
	clr TF0
	djnz R6,loop
	ret
digito_al_terminal:;para mostrar en la terminal 
	add A,#30h
	lcall sndchr
	mov A,#0dh	; para resscribir los numeros sobre si mismos en la terminal
	lcall sndchr
	ret
	end
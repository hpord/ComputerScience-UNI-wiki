	org 8000h
	lcall inicioLCD

; Primero fijamos la direccióne CGRAM, luego descargas los
; patrones del font.  caracters 0 y 1 son definidos
; sucesivamente.  caracter 0 es una Carita feliz, y caracter
; 1 es una Flor. Para una fila blanca del font, el
; patron de bits 20h es enviado.

    mov   a, #0     ; selecciona caracter de dirección 0
    mov   b, #0     ; selecciona fila 0 del font de dirección 0
    lcall setCGRAM4
    lcall prtLCD4
    db    20h, 11h, 20h, 04h, 20h, 11h, 0Eh, 20h	; Carita feliz
    db	  20h, 0Eh, 1Fh, 0Eh, 04h, 1Fh, 04h, 04h,0	; flor

; mueve cursor a la linea 1
    mov   a, #1               ; linea 1
    mov   b, #0               ; posicion 0
    lcall placeCur4
; imprime mensaje.  desde que 0 implica fin de la cadena,
; se usa caracter 8. Note que los caracters 0..7
; son los mismos que los caracteres 8..Fh.
    lcall prtLCD4             ; imprime mensaje
    db    " Carita feliz: ", 8, 0
; mueve cursor a la linea 2
    mov   a, #2               ; linea 2
    mov   b, #0               ; posicion 0
    lcall placeCur4
    lcall prtLCD4             ; imprime mensaje
    db    " Flor: ", 1, 0
    mov R0,#offCur
    lcall wrLCDcom4
    ljmp 2F0h
;=======================================================================
;esta rutina establece la dirección RAM del generador de caracteres. El
; carácter [0..7] se coloca en el acumulador. Las filas de las fuentes
; se colocan en el registro b. las instrucciones 40h a 7Fh
; seleccionan las direcciones CGRAM 0 a 3Fh (0 a 63 decimal).
; Se asume la fuente de caracteres 5x7, es decir, cada caracter
; contiene una matriz de 40 puntos dispuestos en 8 filas de
; 5 puntos cada uno. Las 7 filas son para los caracteres y la 8ª
; fila para el cursor de subrayado. La dirección CGRAM 0 corresponde
; a la primera fila (fuente) del carácter 0, la dirección 7 corresponde
; a la 8ª (última) fila de carácter 0, y la dirección 3Fh
; corresponde a la 8ª fila del caracter 7.
;
; Entrada: el acumulador indica el código de caracteres [0..7]
;y el registro B acumula la fila del font [0..7]
; Salida: ninguno
;========================================================================
setCGRAM4:
         push  b
         mov   b, #8
         mul   ab           ; multiplica numero de caracter por 8
         pop   b            ; b acumula numero de fila
         add   a, b         ; a acumula la dirección del CGRAM
         add   a, #40h      ; convierte a una instrucción
         mov   r0, a        ; carga instrucción
         lcall wrLCDcom4    ; envia comando
         ret
;=======================================================================
$INCLUDE(subrutinasLCD.inc)
end
.model small
.stack 100h
.data

prompt db 13, 10, 'First number:','$'
prompt db 13,10, 'Second number:', '$'
result db 13, 10, 'Sum','$'
 
;Variables


num1 db ?
num2 db ?
sum db ?
 
.code
main proc

    mov ax,@data           ;get data segment address
    mov ds,ax              ;initialize ds

;Display Prompt

    mov ah,9    ;print string function
    mov dx,offset prompt;ds:dx points to string
    int 21h
 
; Numbers from the user
    mov ah,1    ;input function
    int 21h
    mov bl,al   ;save the value from input
    mov num1,al

    mov ah,9
    lea dx, prompt  ;print prompt
    int 21h

    mov ah,2    ;input second function
    int 21h
    mov bh,al   ;save the value from second input
    mov num2,al

;Addition

        mov ax,num1         ;move num1 into ax
        add ax,num2         ;add first and second numbers together
        mov sum,ax           ;move the total sum of numbers in sum

;Print Sum
    mov ah,9
    lea dx, result       ; print result
    int 21h

    mov ah,2
    mov dl,bl
    int 21h

        mov dl,'+'           ;display + sign
    int 21h

    mov dl,bh
    int 21h

        mov dl,'='           ;display = sign
    int 21h

    mov dl,bh
    int 21h

    mov ah,4ch
    int 21h

  main endp

end main

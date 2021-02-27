/ *  - printf02 . s * / 
.data
 
/ * Primer mensaje * / 
. BAlinee 4 
mensaje1 :  . asciz "Hey, escribe un número:"
 
/ * Segundo mensaje * / 
. BAlinee 4 
mensaje2 :  . asciz "% d por 5 es% d \ n"
 
/ * Patrón de formato para scanf * / 
. BAlinee 4 
scan_pattern :  . asciz "% d"
 
/ * Donde scanf almacenará el número leído * / 
. BAlinee 4 
number_read :  . palabra  0
 
. BAlinee 4 
de retorno :  . palabra  0
 
. BAlinee 4 
return2 :  . palabra  0
 
.texto
 
/*
función mult_by_5
* / 
mult_by_5 :  
    ldr r1 , address_of_return2        / * r1 ← & address_of_return * / 
    str lr ,  [ r1 ]                      / *  * r1 ← lr * /
 
    agregue r0 , r0 , r0 ,  LSL # 2            / * r0 ← r0 +  4 * r0 * /
 
    lr LDR , address_of_return2        / * lr ← y address_of_return * / 
    LDR LR ,  [ LR ]                      / * lr ← * LR * / 
    BX LR                             / * regreso de principal utilizando lr * / 
address_of_return2 :  . palabra retorno2
 
.global main
main : 
    ldr r1 , address_of_return         / * r1 ← & address_of_return * / 
    str lr ,  [ r1 ]                      / *  * r1 ← lr * /
 
    ldr r0 , address_of_message1       / * r0 ← & message1 * / 
    bl printf                         / *  call to printf * /
 
    ldr r0 , address_of_scan_pattern   / * r0 ← & scan_pattern * / 
    ldr r1 , address_of_number_read    / * r1 ← & number_read * / 
    bl scanf                          / *  call to scanf * /
 
    ldr r0 , address_of_number_read    / * r0 ← & number_read * / 
    ldr r0 ,  [ r0 ]                      / * r0 ← * r0 * / 
    bl mult_by_5
 
    mov r2 , r0                        / * r2 ← r0 * / 
    ldr r1 , address_of_number_read    / * r1 ← & number_read * / 
    ldr r1 ,  [ r1 ]                      / * r1 ← * r1 * / 
    ldr r0 , address_of_message2       / * r0 ← & message2 * / 
    bl printf                         / *  llame a printf * /
 
    lr LDR , address_of_return         / * lr ← y address_of_return * / 
    LDR LR ,  [ LR ]                      / * lr ← * LR * / 
    BX LR                             / * regreso de principal utilizando lr * / 
address_of_message1 :  . palabra mensaje1
address_of_message2 :  . mensaje de palabra2
address_of_scan_pattern :  . word scan_pattern
address_of_number_read :  . word number_read
address_of_return :  . palabra retorno
 
/ * Externo * / 
. mundial printf
 . scanf global
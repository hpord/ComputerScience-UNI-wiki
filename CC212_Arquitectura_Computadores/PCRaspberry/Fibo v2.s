fibo:   push	{lr}  @ salvaguarda lr
	sub	sp, #12	@ hago espacio para v. locales
 	cmp	r0, #2 	@ if n<2
	movlo	r0, #1	@ return 1
	blo	fib1	
	
	sub	r0, #1 @ else		 
	str	r0, [sp] @ salvo n-1 en [sp]
	bl	fibo	@fibonacci(n-1)
	str 	r0, [sp, #4] @ salvo valor devuelto por fib.(n-1)
	ldr	r0, [sp]  @ recupero de la pila n-1 
	sub 	r0, #1	@ calculo n-2
	bl	fibo @ fibonacci(n-2)
	ldr	r1, [sp, #4] @ recupero salida de fib.(n-1)
	add	r0, r1	@ lo sumo a fib.(n-1)
	
fib1: 	add	sp, #12 @ libero espacio de v. locales
	pop	{lr}	@ recupero registros (sólo lr)
	bx	lr	@ salgo de la función
 

 
  

 
 
 
 
    
 

  

  
 
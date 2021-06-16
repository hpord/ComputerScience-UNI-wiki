;-------------------------------------------------------------------------------
; MSP430 Assembler Code Template for use with TI Code Composer Studio
;
;
;-------------------------------------------------------------------------------
            .cdecls C,LIST,"msp430.h"       ; Include device header file
            
;-------------------------------------------------------------------------------
            .def    RESET                   ; Export program entry-point to
                                            ; make it known to linker.
;-------------------------------------------------------------------------------
            .text                           ; Assemble into program memory.
            .retain                         ; Override ELF conditional linking
                                            ; and retain current section.
            .retainrefs                     ; And retain any sections that have
                                            ; references to current section.

;-------------------------------------------------------------------------------
RESET       mov.w   #__STACK_END,SP         ; Initialize stackpointer
StopWDT     mov.w   #WDTPW|WDTHOLD,&WDTCTL  ; Stop watchdog timer


;-------------------------------------------------------------------------------
; Main loop here
;===================================PREGUNTA 1=====================================
;Encendido del LED rojo
;			bis.b #0x01,&P1DIR	;configuro P1.0 como salida.Se hace un or logico
;			bis.b #0x01,&P1OUT	;Envio un 1 al pin P1.0 como salida
;							;para encender el LED rojo
;loop:		jmp loop
;==================================================================================
;===================================PREGUNTA 2=====================================
;Encendido del LED verde
;El led verde se encuentra en P1.6
;Queremos q el pin p1.6 sea una salida no debo tocar el PIN P1.0
;			bis.b #0x40,&P1DIR ;tmb se peude escribirr en binario
;			bis.b #0x40,&P1OUT	;#40h = #01000000b esto representa el P1.6
;								;ya q va desde p1.0 hasta p1.7
;loop:		jmp loop
;==================================================================================
;===================================PREGUNTA 3=====================================
;Modificar el programa anterior para encender solamente el LED ROJO y
;solamente el LED VERDE usando la instrucción mov.b.
;			mov.b #41h,&P1DIR	;41h = 01000001b
;			mov.b #41h,&P1OUT
;otra_v		jmp otra_v
;==================================================================================
;===================================PREGUNTA 4=====================================
;Hacer un programa para encender 2 leds al mismo tiempo (el LED ROJO y VERDE).
;			bis.b #01000001b,&P1DIR
;			mov.b #01000001b,&P1OUT
;otra_v		jmp otra_v
;==================================================================================
;===================================PREGUNTA 5=====================================
;Hacer un programa para hacer parpadear el LED ROJO
;			bis.b #0x01,&P1DIR	;configuro el bit P1.0 como salida
;			bis.b #0x01,&P1OUT	;enciendo LED
;repite:		inv.b &P1OUT		;inv saca el complemento del registro P1OUT si es 1 lo vuelve 0 si es 0 lo vuelve 1
;wait:		mov.w #65000,R5
;lazo:		dec R5
;			jnz lazo
;			jmp repite
;==================================================================================
;			mov.b #0x01,&P1DIR
;			mov.b #0x01,&P1OUT
;repite:		inv.b &P1OUT		;inv saca el complemento del registro P1OUT si es 1 lo vuelve 0 si es 0 lo vuelve 1
;wait:		mov.w #65000,R5
;lazo:		dec R5
;			jnz lazo
;			jmp repite
;==================================================================================
;===================================PREGUNTA 6=====================================
;Hacer un programa para hacer parpadear el LED VERDE.
;			mov.b #0x40,&P1DIR
;			mov.b #0x40,&P1OUT
;repite:		inv.b &P1OUT		;inv saca el complemento del registro P1OUT si es 1 lo vuelve 0 si es 0 lo vuelve 1
;wait:		mov.w #65000,R5
;lazo:		dec R5
;			jnz lazo
;			jmp repite
;==================================================================================
;===================================PREGUNTA 7=====================================
;Hacer un programa para hacer parpadear el LED ROJO y el LED VERDE.
;			mov.b #01000001b,&P1DIR
;			mov.b #01000001b,&P1OUT
;repite:		inv.b &P1OUT		;inv saca el complemento del registro P1OUT si es 1 lo vuelve 0 si es 0 lo vuelve 1
;wait:		mov.w #65000,R5
;lazo:		dec R5
;			jnz lazo
;			jmp repite
;==================================================================================
;===================================PREGUNTA 8=====================================
;			mov.b #0x41,&P1DIR
;			mov.b #0x41,&P1OUT
;repite: 	inv.b &P1OUT
;			call #wait
;			jmp repite
;
;wait:		mov.w #65000,R5
;lazo:		dec R5
;			jnz lazo
;			ret
;==============OTRA FORMA==========================================================
;			bis.b #0x41,&P1DIR
;repite		bis.b #0x41,&P1OUT	;enciendo LED rojo y verde
;			call #wait
;			bic.b #0x41,&P1OUT
;			call #wait
;			jmp repite
;wait		mov.w #65000,R5
;lazo		dec R5
;			jnz lazo
;			ret
;==================================================================================
;===================================PREGUNTA 9=====================================
;			bis.b #0x41,&P1DIR	;configuro el bit P1.0 y el bit P1.6 como salida
;repite		bis.b #0x01,&P1OUT
;			bic.b #0x40,&P1OUT	;limpia el bit 0x40
;			call #wait
;			bis.b #0x40,&P1OUT
;			bic.b #0x01,&P1OUT
;			call #wait
;			jmp repite
;
;wait		mov.w #65000,R5
;lazo		dec R5
;			jnz lazo
;			ret

;==================================================================================
;===================================PREGUNTA 10=====================================
;Programa que lee una entrada(botón) y de acuerdo al estado modifica la salida del LED
;ROJO.
;			bis.b #0x01,&P1DIR
;			mov.b #8h,&P1OUT	;se fija en 1 el pin P1.3
;			bis.b #8h,&P1REN	;se fija PULL UP en el pin P1.3
;repite		bit.b #00001000b, &P1IN	;se ve el estado del pin P1.3
;			jc ON
;OFF		bic.b #0x01,&P1OUT
;			jmp repite
;ON			bis.b #0x01,&P1OUT
;			jmp repite
;===================================================================================
;===================================PREGUNTA 11=====================================
;Realice un programa que cuando se presione un botón encienda solamente el LED
;VERDE y cuando no lo presione que encienda solamente el LED ROJO.
;			bis.b #0x01,&P1DIR
;			bis.b #0x40,&P1DIR
;			mov.b #8h,&P1OUT	;se fija en 1 el pin P1.3
;			bis.b #8h,&P1REN	;se fija PULL UP en el pin P1.3
;repite		bit.b #00001000b, &P1IN	;se ve el estado del pin P1.3
;			jc ON
;OFF			bic.b #0x01,&P1OUT
;			bis.b #0x40,&P1OUT
;			jmp repite
;ON			bis.b #0x01,&P1OUT
;			bic.b #0x40,&P1OUT
;			jmp repite
;===================================================================================
;===================================PREGUNTA 12=====================================
;Realice un programa que al presionar un botón inicie el parpadeo del LED ROJO y
;encienda el LED VERDE. Y si no presiona que no se encienda nada.
;			bis.b #0x01,&P1DIR
;			bis.b #0x40,&P1DIR
;			mov.b #8h,&P1OUT	;se fija en 1 el pin P1.3
;			bis.b #8h,&P1REN	;se fija PULL UP en el pin P1.3
;repite		bit.b #00001000b, &P1IN	;se ve el estado del pin P1.3
;			jc ON
;OFF			mov.b #0x40,&P1DIR
;			call #repite1
;			jmp repite
;ON			bic.b #0x01,&P1OUT
;			bic.b #0x40,&P1OUT
;			jmp repite
;
;repite1:	inv.b &P1OUT		;inv saca el complemento del registro P1OUT si es 1 lo vuelve 0 si es 0 lo vuelve 1
;wait:		mov.w #65000,R5
;lazo:		dec R5
;			jnz lazo
;			ret
;===============================Codigo del profe====================================
			bis.b #0x41,&P1DIR
			mov.b #8h,&P1OUT
			bis.b #8h,&P1REN
repite		bit.b #00001000b,&P1IN
			jc ON
OFF			call #blink
			jmp repite
ON			bic.b #0x41,&P1OUT
			jmp repite

blink 		bis.b #0x41,&P1OUT
			call #wait
			bic.b #0x01,&P1OUT
			call #wait
			ret
wait		mov.w #65000,R5
lazo		dec R5
			jnz lazo
			ret

;===================================================================================
;-------------------------------------------------------------------------------


;-------------------------------------------------------------------------------
; Stack Pointer definition
;-------------------------------------------------------------------------------
            .global __STACK_END
            .sect   .stack
            
;-------------------------------------------------------------------------------
; Interrupt Vectors
;-------------------------------------------------------------------------------
            .sect   ".reset"                ; MSP430 RESET Vector
            .short  RESET
            

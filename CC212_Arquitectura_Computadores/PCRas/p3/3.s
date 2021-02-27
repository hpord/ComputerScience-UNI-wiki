.text
.global _start

_start:
mov r1,#5
mov r2,#25
mov r3,#0
loop:
cmp r1,r2
bgt end
sub r2,r2,r1 @r2=r2-r1
add r3,r3,#1
b loop
end:
mov r0,r3
mov r7,#1
swi 0

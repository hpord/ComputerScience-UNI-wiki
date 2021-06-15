all:3
3:3.o
	ld -o $@ $+
3.o:3.s
	as -o $@ $<
clean:
	rm -vf 3 *.o


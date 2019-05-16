all: atf atf2 cbl amb

atf: atf_main.o atf.o
	gcc -o atf atf_main.o atf.o
atf_main.o: atf_main.c atf.h
atf.o: atf.c atf.h

atf2: atf_main.o atf2.o
	gcc -o atf2 atf_main.o atf2.o
atf2.o: atf2.c atf2.h

cbl: cbl_main.o cbl.o
	gcc -o cbl cbl_main.o cbl.o
cbl.o: cbl.c cbl.h

amb: amb_main.o amb.o
	gcc -o amb amb_main.o amb.o
amb.o: amb.c amb.h

clean:
	rm -f atf atf2 cbl amb *.o

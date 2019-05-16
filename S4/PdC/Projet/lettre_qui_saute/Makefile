OPTION=-ansi -pedantic -Wall

.PHONY: clean jeu.test

jeu: jeu.c atf.o gestionpile.h gestionpile.o
	gcc $(OPTION) -o jeu atf.o gestionpile.o jeu.c

jeu.test: jeu
	./jeu dure doux

clean:
	- rm jeu *.o

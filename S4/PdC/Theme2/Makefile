all: mcu_test mcu_wc mcu_ww mcu_wl mcu_rev mcu_uniq mcu_xxd

mcu_test: mcu_affiche_entier.o mcu_fatal.o mcu_readl.o mcu_test.c
mcu_affiche_entier.o: mcu_affiche_entier.c mcu_affiche_entier.h
mcu_fatal.o: mcu_fatal.c mcu_fatal.h
mcu_readl.o: mcu_readl.c mcu_readl.h

mcu_wc: mcu_wc.o mcu_affiche_entier.o
mcu_wc.o: mcu_wc.c mcu_affiche_entier.h

mcu_ww: mcu_ww.o mcu_affiche_entier.o
mcu_ww.o: mcu_wc.c mcu_affiche_entier.h

mcu_wl: mcu_wl.o mcu_readl.o
mcu_wl.o: mcu_wl.c mcu_readl.h mcu_macros.h

mcu_rev: mcu_rev.o mcu_readl.o
mcu_rev.o: mcu_rev.c mcu_readl.h mcu_macros.h

mcu_uniq: mcu_uniq.o mcu_readl.o
mcu_uniq.o: mcu_uniq.c mcu_readl.h mcu_macros.h

mcu_xxd: mcu_xxd.o mcu_readl.o
mcu_xxd.o: mcu_xxd.c mcu_readl.h mcu_macros.h

clean:
	rm -f mcu_test mcu_wc mcu_ww mcu_wl mcu_rev mcu_uniq mcu_xxd *.o

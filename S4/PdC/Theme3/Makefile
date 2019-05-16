all: tab quicksort prixNobel quicksort_generique msort

tab: tab.o
tab.o: tab.c macro.h

quicksort: quicksort_int.o
	gcc -o quicksort quicksort_int.o
quicksort_int.o: quicksort_int.c macro.h

prixNobel: prixNobel.o
prixNobel.o: prixNobel.c macro_prix.h

quicksort_generique: quicksort_generique_main.o quicksort_generique.o
	gcc -o quicksort_generique quicksort_generique_main.o quicksort_generique.o
quicksort_generique_main.o: quicksort_generique_main.c macro.h
quicksort_generique.o: quicksort_generique.c quicksort_generique.h

msort: msort.o quicksort_generique.o mcu_readl.o
msort.o: msort.c quicksort_generique.h mcu_readl.h macro_tri.h
mcu_readl.o: mcu_readl.c mcu_readl.h mcu_macros.h

clean:
	rm -f tab quicksort prixNobel quicksort_generique msort *.o

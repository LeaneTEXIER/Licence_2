#include <stdio.h>
#include "macro_tri.h"
#include "mcu_readl.h"
#include "quicksort_generique.h"

void printfile(int* tab, int size){
  int i, j, l;
  i = 0;
  for (j=0; j<size; j++){
    while (l=*(tab+i)){
      putchar(l);
      i++;
    }
    putchar('\n');
    i = 0;
  }
}

void msort(void){
  int tab[NMAXLINE][NMAXCHAR];
  int i;
  i = 0;
  while (readl(tab[i])!=EOF){
    quicksort(&tab[0], i, sizeof(tab[0]), comparstr);
    i++;
  }
  printfile(*tab, i);
}

int main(void){
  msort();
  return 0;
}

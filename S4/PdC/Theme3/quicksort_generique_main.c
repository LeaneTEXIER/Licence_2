#include <stdio.h>
#include <stdlib.h>
#include "macro.h"
#include "quicksort_generique.h"

void tab_alea (int* tab){
  int i;
  for (i=0; i<TABSIZE; i++){
    tab[i]=rand();
  }
}

int main(){
  int i;
  int tab[TABSIZE];
  tab_alea(tab);
  quicksort(&tab[0], TABSIZE, sizeof(int), compar);
  for (i=0; i<TABSIZE; i++){
    printf("%i\n", tab[i]);
  }
  return 0;
}

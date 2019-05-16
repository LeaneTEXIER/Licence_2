#include <stdio.h>
#include <stdlib.h>
#include "macro.h"

void tab_alea (int* tab){
  int i;
  for (i=0; i<TABSIZE; i++){
    tab[i]=rand();
  }
}

int main(void){
  int i;
  int tab[TABSIZE];
  tab_alea(tab);
  for (i=0; i<TABSIZE; i++){
    printf("%i\n", tab[i]);
  }
  return 0;
}

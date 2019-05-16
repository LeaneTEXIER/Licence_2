#include <stdio.h>
#include <stdlib.h>
#include "macro.h"

void tab_alea (int* tab){
  int i;
  for (i=0; i<TABSIZE; i++){
    tab[i]=rand();
  }
}

int partition(int *tab, int left, int right){
  int pivot, i, j, tmp;
  pivot = left;
  i = left + 1;
  j = right;
  while (i<=j){
    if (tab[i]>tab[pivot]){
      tmp = tab[i];
      tab[i] = tab[j];
      tab[j] = tmp;
      j--;
    }
    else{
      tmp = tab[i];
      tab[i] = tab[pivot];
      tab[pivot] = tmp;
      i++;
      pivot++;
    }
  }
  return pivot;
}

void quicksort_int_aux(int *tab,unsigned int first,unsigned int last){
  int p;
  if (first+'0'<last+'0'){
    p=partition(tab, first, last);
    quicksort_int_aux(tab, first, p-1);
    quicksort_int_aux(tab, p+1, last);
  }
}


void quicksort_int(int *tab, unsigned int nelem) {
  quicksort_int_aux(tab, 0, nelem-1);
}

int main(void){
  int i;
  int tab[TABSIZE];
  tab_alea(tab);
  quicksort_int(tab, TABSIZE);
  for (i=0; i<TABSIZE; i++){
    printf("%i\n", tab[i]);
  }
  return 0;
}

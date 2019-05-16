#include <stdio.h>
#include "cbl.h"

int main(void){
  cbl_init();
  void * tab[42];
  void * tab2[42];
  int i, j;
  int test;
  void * adr;
  i = 0;
  /* Allocation de blocs tant que possible*/
  while ((adr = cbl_newbloc())!=NULL){
    /* Garder 42 adresses*/
    if (i<42){
      tab[i] = adr;
      i++;
    }
  }
  /* Libération de ces 42 blocs*/
  for (i=0; i<42; i++){
    cbl_freebloc(tab[i]);
  }
  /* Allocation de blocs tant que possible*/
  i = 0;
  while ((adr = cbl_newbloc())!=NULL){
    tab2[i] = adr;
    i++;
  }
  /*Vérification que cela à allouer 42 blocs*/
  printf ("42 blocs alloués: %s\n",i==42 ? "true" : "false");
  /* Vérification que les adresses de ces 42 blocs correspondent aux blocs libérés*/
  for (i=0; i<42; i++){
    test = 0;
    j = 0;
    while (!test && j<42){
      if (tab[i]==tab2[j]){
        test = 1;
      }
      j++;
    }
    if (!test){
      printf ("Adresses différentes\n");
    }
  }
  printf("Tout a été vérifié\n");
  return 0;
}

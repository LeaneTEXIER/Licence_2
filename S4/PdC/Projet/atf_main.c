#include <stdio.h>
#include "atf2.h"

int main(void){
  atf_init();
  void * tab[42];
  void * tab2[42];
  int i;
  void * adr;
  i = 0;
  /* Allocation de blocs tant que possible*/
  while ((adr = atf_newbloc())!=NULL){
    /* Garder 42 adresses*/
    if (i<42){
      tab[i] = adr;
      i++;
    }
  }
  /* Libération de ces 42 blocs*/
  for (i=0; i<42; i++){
    atf_freebloc(tab[i]);
  }
  /* Allocation de blocs tant que possible*/
  i = 0;
  while ((adr = atf_newbloc())!=NULL){
    tab2[i] = adr;
    i++;
  }
  /*Vérification que cela à allouer 42 blocs*/
  printf ("42 blocs alloués: %s\n",i==42 ? "true" : "false");
  /* Vérification que les adresses de ces 42 blocs correspondent aux blocs libérés*/
  for (i=0; i<42; i++){
    if (tab[i]!=tab2[i]){
      printf ("Adresses différentes\n");
    }
  }
  printf("Tout a été vérifié\n");
  return 0;
}

#include <stdio.h>
#include "amb.h"

int main(void){
  amb_init();
  void * tab[42];
  void * tab2[42];
  int i, j;
  int test;
  void * adr;
  i = 0;
  /* Liste de taille pour les blocs */
  int list[10];
  list[0] = 2;  list[1] = 4;  list[2] = 3;  list[3] = 5;  list[4] = 2;  list[5] = 1;  list[6] = 3;  list[7] = 6;  list[8] = 1;  list[9] = 2;
  int n;
  n = 0;
  /* Allocation de blocs tant que possible*/
  while ((adr = amb_newbloc(list[n%10]))!=NULL){
    n++;
    /* Garder 42 adresses*/
    if (i<42){
      tab[i] = adr;
      i++;
    }
  }
  /* Libération de ces 42 blocs*/
  for (i=0; i<42; i++){
    amb_freebloc(tab[i]);
  }
  /* Allocation de blocs tant que possible*/
  i = 0;
  n = 0;
  while ((adr = amb_newbloc(list[n%10]))!=NULL){
    n++;
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

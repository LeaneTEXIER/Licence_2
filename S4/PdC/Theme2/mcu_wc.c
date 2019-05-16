#include <stdio.h>
#include "mcu_affiche_entier.h"

int main (int argc, char const *argv[]){
  int i;
  int c;
  i=0;
  while ((c=getchar())!=EOF){
    i++;
  }
  affiche_entier(i);
  putchar('\n');
  return 0;
}

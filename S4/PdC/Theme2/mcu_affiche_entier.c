#include "mcu_affiche_entier.h"
#include <stdio.h>

void affiche_entier(int i){
  if (i>9){
    affiche_entier(i/10);
  }
  putchar((i%10)+'0');
}

/*int main(int argc, char const *argv[]) {
  int i;
  i = 18;
  affiche_entier(i);
}*/

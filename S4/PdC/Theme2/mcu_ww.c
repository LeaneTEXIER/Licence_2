#include <stdio.h>
#include "mcu_affiche_entier.h"

int estLettreOuChiffre(char c){
  if ((c<'0') || (c>'9' && c<'A') || (c>'Z' && c<'a') || (c>'z')){
    return 0;
  }
  else{
    return 1;
  }
}

int main (int argc, char const *argv[]){
  int i;
  char c;
  i=0;
  c=getchar();
  while (!estLettreOuChiffre(c) && c!=EOF){
    c=getchar();
  }
  while (c!=EOF){
    if (!estLettreOuChiffre(c)){
      i++;
      c=getchar();
      while (!estLettreOuChiffre(c) && c!=EOF){
        c=getchar();
      }
    }
    else{
      c=getchar();
    }
  }
  affiche_entier(i);
  putchar('\n');
  return 0;
}

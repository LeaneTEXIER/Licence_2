#include <stdio.h>
#include "mcu_readl.h"
#include "mcu_macros.h"

int main (int argc, char const *argv[]){
  int line[MAXLINE];
  int tab_car[16];
  int offset,i,j,k,l;
  offset=0;
  i=readl(line);
  k=0;
  while (i!=EOF){
    j=0;
    /* Remplir le tableau de caractères de taille 16*/
    while (j<16 && i!=EOF){
      if (line[k]){
        tab_car[j++]=line[k++];
      }
      else{
        tab_car[j++]='\n';
        i=readl(line);
        k=0;
      }
    }
    /*Afficher l'offset */
    printf("%7.7X:", offset);
    offset+=16;
    /*Afficher le code hexa des cara, complété par des espaces si tab_car a moins de 16 cara*/
    for (l=0; l<j; l++){
      if (l%2==0){
        putchar(' ');
      }
      printf("%2.2X", tab_car[l]);
    }
    /* Complete si tab_car a moins de 16 cara*/
    while (l<16){
      if (l%2==0){
        putchar(' ');
      }
      printf("  ");
      l++;
    }
    /*Afficher les cara de tab_car*/
    putchar(' ');
    for (l=0; l<j; l++){
      if (tab_car[l]!='\n'){
        putchar(tab_car[l]);
      }
      else{
        putchar('.');
      }
    }
    putchar('\n');
  }
  return 0;
}

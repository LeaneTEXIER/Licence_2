#include <stdio.h>
#include "mcu_readl.h"
#include "mcu_macros.h"

int main (int argc, char const *argv[]){
  int line[MAXLINE];
  int line2[MAXLINE];
  int i;
  int j;
  int k;
  /*Lecture et écriture de la premiere ligne */
  i=readl(line);
  j=0;
  while (line[j]){
    putchar(line[j++]);
  }
  putchar ('\n');
  /*Lecture des lignes suivantes jusqu'à EOF et écriture si différente de celle d'avant*/
  k=readl(line2);
  while (k!=EOF){
    /* Si les 2 lignes sont de taille diff, afficher car lignes diff */
    if (i!=k){
      j = 0;
      while (line2[j]){
        putchar(line2[j++]);
      }
      putchar ('\n');
    }
    else{
      j=0;
      /* Comparaison de chaque caractère des 2 lines */
      while (j<=i && line[j]==line2[j]){
        j++;
      }
      j--;
      /* Si les 2 lignes sont differentes, afficher */
      if (j!=i){
        j=0;
        while (line2[j]){
          putchar(line2[j++]);
        }
        putchar ('\n');
      }
    }
    /*line est line2 et line2 est la ligne suivante*/
    i=k;
    j=0;
    while (line2[j]){
      line[j]=line2[j];
      j++;
    }
    k=readl(line2);
  }
  return 0;
}

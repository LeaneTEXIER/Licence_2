#include <stdio.h>
#include "mcu_readl.h"
#include "mcu_macros.h"

int main (int argc, char const *argv[]){
  int i;
  int line[MAXLINE];
  int cmp;
  i=readl(line);
  cmp=0;
  while (i!=EOF){
    i=readl(line);
    cmp++;
  }
  printf("%d",cmp);
  putchar('\n');
  return 0;
}

#include <stdio.h>
#include "mcu_readl.h"
#include "mcu_macros.h"

int main (int argc, char const *argv[]){
  int i;
  int line[MAXLINE];
  int j;
  i=readl(line);
  while (i!=EOF){
    for (j=i; j>=0; j--){
      putchar(line[j]);
    }
    putchar('\n');
    i=readl(line);
  }
  return 0;
}

#include "mcu_readl.h"
#include <stdio.h>
#include <stdlib.h>
#include "mcu_macros.h"

int
readl (int line[])
{
  int c;
  int i;
  i = 0;
  c = getchar ();
  if (c == EOF){
      return EOF;
  }
  while ((c != '\n') && (i < MAXLINE)){
      line[i] = c;
      i++;
      c = getchar ();
    }
  if (i == MAXLINE){
      exit (1);
    }
  line[i] = 0;
  i--;
  return i;
}

/*int main (int argc, char const *argv[])
{
  int line[52];
  int j,i;
  j = 0;
  i = readl (line);
  while (line[j])
    putchar (line[j++]);
  return i;
}*/

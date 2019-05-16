#include "mcu_fatal.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void fatal(int assert, const char message[], int status){
  int i;
  if (assert!=0){
    for(i=0; i<strlen(message); i++){
      putc(message[i], stderr);
    }
    exit(status);
  }
}

/*int
main(int argc, char const *argv[]) {
  fatal(1==1,"1==1 is true\n",2);
  return 0;
}*/

#include <stdio.h>
#include "atf2.h"
#include <math.h>

static char membloc[NBLOCS][ATF_BLOCSIZE];
static unsigned char memstatus_b[NBLOCS_B];


void atf_init(){
  int i;
  for (i=0; i<NBLOCS_B; i++){
    memstatus_b[i]=0;
  }
}


void * atf_newbloc(){
  int i, j, k, l;
  for (i=0; i<NBLOCS_B; i++){
    l = 7;
    if (memstatus_b[i]<255){
      for (j=1; j<=128; j=j*2){
        if ((memstatus_b[i]&j)==0){
          memstatus_b[i] += j;
          k = 8*(i+1)-l-1;
          return &membloc[k][0];
        }
        l -= 1;
      }
    }
  }
  return NULL;
}


int atf_freebloc(void *bloc){
  int i,j,k;
  int test;
  test =  0;
  i = 0;
  while (!test & i<NBLOCS){
    if (&membloc[i][0]==bloc){
      test = 1;
    }
    else{
      i++;
    }
  }
  if (test){
    j = 1;
    for (k=1; k<=i%8; k++){
      j = j * 2;
    }
    if ((memstatus_b[i/8]&j)==j){
        memstatus_b[i/8] -= j;
        return 0;
      }
    }
  return 1;
}

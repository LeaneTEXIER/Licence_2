#include <stdio.h>
#include "atf.h"

static char membloc[NBLOCS][ATF_BLOCSIZE];
static char memstatus[NBLOCS];

void atf_init(){
  int i;
  for (i=0; i<NBLOCS; i++){
    memstatus[i]=0;
  }
}

void * atf_newbloc(){
  int i;
  for (i=0; i<NBLOCS; i++){
    if (memstatus[i]==0){
      memstatus[i]=1;
      return &membloc[i][0];
    }
  }
  return NULL;
}


int atf_freebloc(void *bloc){
  int i;
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
  if (test && memstatus[i]!=0){
    memstatus[i]=0;
    return 0;
  }
  else{
    return 1;
  }
}

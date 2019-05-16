#include <stdio.h>
#include "cbl.h"

static int first_free_blocs;

typedef struct{
  int NBLOCS_FREE;
  int CBL_NEXT;
}BLOCS_FREE_S;

typedef union{
  BLOCS_FREE_S  bfree;
  char alloues[CBL_BLOCSIZE];
}bloc_t;

static bloc_t membloc[NBLOCS];

int cbl_init(){
  int i;
  membloc[0].bfree.NBLOCS_FREE = NBLOCS;
  membloc[0].bfree.CBL_NEXT = BLOC_END;
  first_free_blocs = 0;
  for (i=1; i<NBLOCS; i++){
    membloc[i].bfree.NBLOCS_FREE = 0;
  }
}

void * cbl_newbloc(){
  void * adr;
  if (first_free_blocs==BLOC_END){
    return NULL;
  }
  int BL_FREE = membloc[first_free_blocs].bfree.NBLOCS_FREE;
  membloc[first_free_blocs].bfree.NBLOCS_FREE = -1;
  if (BL_FREE!=1){
    membloc[first_free_blocs+1].bfree.NBLOCS_FREE = BL_FREE-1;
    membloc[first_free_blocs+1].bfree.CBL_NEXT = membloc[first_free_blocs].bfree.CBL_NEXT;
    adr = &(membloc[first_free_blocs].alloues);
    first_free_blocs++;
  }
  else{
    adr = &(membloc[first_free_blocs].alloues);
    first_free_blocs = membloc[first_free_blocs].bfree.CBL_NEXT;
  }
  return adr;
}

int cbl_freebloc(void *bloc){
  int i;
  int test;
  test =  0;
  i = 0;
  while (!test & i<NBLOCS){
    if (&membloc[i].alloues==bloc){
      test = 1;
    }
    else{
      i++;
    }
  }
  if (!test || (membloc[i].bfree.NBLOCS_FREE != -1)){
    return 1;
  }
  else{
    membloc[i].bfree.NBLOCS_FREE = 1;
    membloc[i].bfree.CBL_NEXT = first_free_blocs;
    first_free_blocs = i;
    return 0;
  }
}

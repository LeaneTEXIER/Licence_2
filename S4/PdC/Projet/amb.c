#include <stdio.h>
#include "amb.h"

static int first_free_blocs;

typedef struct{
  int NBLOCS_FREE;
  int AMB_NEXT;
}BLOCS_FREE_S;

typedef union{
  BLOCS_FREE_S  bfree; /* Pour premier bloc d'une série de blocs libres */
  char b_alloues[AMB_BLOCSIZE]; /* Pour bloc alloué */
  unsigned int size_n; /* Pour le "bloc 0" d'une série de blocs alloués */
}bloc_t;

static bloc_t membloc[NBLOCS];

int amb_init(){
  int i;
  membloc[0].bfree.NBLOCS_FREE = NBLOCS;
  membloc[0].bfree.AMB_NEXT = BLOC_END;
  first_free_blocs = 0;
  for (i=1; i<NBLOCS; i++){
    membloc[i].size_n = 0;
  }
}


void * amb_newbloc(unsigned int nbloc){
  void * adr;
  int i,j,n,n_prev, nbloc_int;
  if (first_free_blocs==BLOC_END){
    return NULL;
  }
  n_prev = -1;
  n = first_free_blocs;
  i = membloc[first_free_blocs].bfree.AMB_NEXT;
  j = membloc[first_free_blocs].bfree.NBLOCS_FREE;
  while ((i!=-1) && (j<nbloc)){
    n_prev = n;
    n = i;
    i = membloc[i].bfree.AMB_NEXT;
    j = membloc[i].bfree.NBLOCS_FREE;
  }
  nbloc_int = (int) nbloc;
  if (j<nbloc_int){
    return NULL;
  }
  adr = &membloc[n];
  membloc[n].size_n = nbloc;
  if (j==nbloc+1){ //Prend exactement la taille
    if (n_prev==-1){
      first_free_blocs = i;
    }
    else{
      membloc[n_prev].bfree.AMB_NEXT = i;
    }
  }
  else{ //if (j>nbloc)
    if (n_prev==-1){
      first_free_blocs = first_free_blocs+nbloc+1;
      membloc[first_free_blocs].bfree.AMB_NEXT = i;
      membloc[first_free_blocs].bfree.NBLOCS_FREE = j-nbloc-1;
    }
    else{
      membloc[n_prev].bfree.AMB_NEXT = n+nbloc+1;
      membloc[n+nbloc+1].bfree.AMB_NEXT = i;
      membloc[n+nbloc+1].bfree.NBLOCS_FREE = j-nbloc-1;
    }
  }
  return adr;
}


int amb_freebloc(void *bloc){
  int i, prev, next;
  int test;
  test =  0;
  i = 0;
  while (!test & i<NBLOCS){
    if (&membloc[i].b_alloues==bloc){
      test = 1;
    }
    else{
      i++;
    }
  }
  if (!test || (membloc[i].size_n==0)){
    return 1;
  }
  prev = -1;
  next = first_free_blocs;
  while ((next!=-1) && (next<i)){
    prev = next;
    next = membloc[prev].bfree.AMB_NEXT;
  }
  if ((next != -1) && (membloc[i].size_n + 1 + i == next)){
    membloc[i].bfree.NBLOCS_FREE = membloc[i].size_n + 1 + membloc[next].bfree.NBLOCS_FREE;
    membloc[i].bfree.AMB_NEXT = membloc[next].bfree.AMB_NEXT;
  }
  if ((prev == -1)){
    first_free_blocs = i;
  }
  else if (membloc[prev].bfree.NBLOCS_FREE + prev == i){
    membloc[prev].bfree.NBLOCS_FREE += membloc[i].size_n+1;
  }
  if (((next==-1) && (prev==-1)) || ((next==-1) && (membloc[prev].bfree.NBLOCS_FREE + prev != i)) || ((prev==-1) && (membloc[i].size_n + 1 + i != next))){
    membloc[i].bfree.AMB_NEXT = next;
    membloc[i].bfree.NBLOCS_FREE = membloc[i].size_n+1;
    if ((next==-1) && (membloc[prev].bfree.NBLOCS_FREE + prev != i)){
      membloc[prev].bfree.AMB_NEXT = i;
    }
  }
  return 0;
}

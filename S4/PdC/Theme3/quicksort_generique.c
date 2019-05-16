#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compar (const void * nb1, const void * nb2){
  if (*(int *) nb1 == *(int *) nb2){
    return 0;
  }
  else if (*(int *) nb1 > *(int *) nb2){
    return 1;
  }
  else{
    return -1;
  }
}

int comparstr (const void * ch1, const void * ch2){
  if (*(char *)ch1 && *(char *)ch2){
    if (*(char *)ch1 == *(char *)ch2){
      return comparstr(ch1+1, ch2+1);
    }
    else if (*(char *)ch1 > *(char *)ch2){
      return 1;
    }
    else{
      return -1;
    }
  }
  else{
    if (*(char *)ch1){
      return 1;
    }
    else if (*(char *)ch2){
      return -1;
    }
    else{
      return 0;
    }
  }
}

int partition(void* base, int start, int nelem, int size, int(*compar)(const void *, const void *)){
  int ind_pivot, i, j;
  ind_pivot = start;
  i = start + 1;
  j = nelem;
  while (i<=j){
    if (compar((base + size * ind_pivot), (base + size * i))==-1){
      void *const tmp = malloc(size);
      memcpy (tmp, (base + size * i), size);
      memcpy ((base + size * i), (base + size * j), size);
      memcpy((base + size * j), tmp, size);
      free(tmp);
      j--;
    }
    else{
      void *const tmp = malloc(size);
      memcpy (tmp, (base + size * i), size);
      memcpy ((base + size * i), (base + size * ind_pivot), size);
      memcpy ((base + size * ind_pivot), tmp, size);
      free(tmp);
      i++;
      ind_pivot++;
    }
  }
  return ind_pivot;
}

void quicksort_aux(void* base, int start, int nelem, int size, int(*compar)(const void *a, const void *b)){
  if (nelem>start){
    int pivot = partition(base, start, nelem, size, compar);
    quicksort_aux(base, start, pivot-1, size, compar);
    quicksort_aux(base, pivot+1, nelem, size, compar);
  }
}

void quicksort(void* base, int nelem, int size, int(*compar)(const void *a, const void *b)){
  quicksort_aux(base, 0, nelem-1, size, compar);
}

#include "gestionpile.h"
#include <stdio.h>
#include <stdlib.h>
#include "atf.h"

void 
vider
(Pile_t *pile)
{
  if (!(*pile))
     return ;
  vider(&((*pile)->next)) ;
  atf_freebloc(*pile) ;
  *pile = NULL ;
  return ;
}

void 
empiler
(int element, Pile_t *pile)
{
   Pile_t tmp ;
   tmp = (Pile_t) atf_newbloc() ;
   if (tmp==NULL)
   {
	perror("Impossible d'allouer suffisament de blocs\n") ;
        exit(ALLOCATIONIMPOSSIBLE);
   }
   tmp->mot = element ;

   tmp->next = *pile ;
   *pile = tmp ; 
   return ;
}

int 
depiler
(Pile_t *pile)
{ 
  int res ;
  Pile_t tmp ;
  if (!(*pile))
     return PILEVIDE ; /* la pile est vide */
  tmp = *pile ;
  *pile = tmp-> next ;
  res = tmp-> mot ;
  atf_freebloc(tmp) ;
  return res ;
}

int 
estVide
(Pile_t pile)
{
  return (pile==NULL) ;
}

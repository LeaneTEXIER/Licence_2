#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "gestionpile.h"
#include "dico4lettres.h"
#include "atf.h"

#if ATF_BLOCSIZE < 16
#error "Taille de blocs dans atf.h insuffisante pour ce programme"
#endif

#define PARCOURU 1
#define NONPARCOURU 0

typedef int MatriceAdjacence_t[TAILLE_DICO][TAILLE_DICO] ;


/* Cette proc\'edure prend en argument deux cha\^\i{}nes de caract\`eres
   Elle renvoit 1==1 si les cha\^\i{}nes ne diff\`erent que par un caract\`ere et 0==1 sinon */

int
estSuccesseur
(char a[taille_mot], char b[taille_mot])
{

  int i,diff ;

  diff = 0 ;
  for(i=0;i<taille_mot;i++)
    if(a[i]-b[i]!=0)
      diff++ ;

  if (diff==1)
    return 1==1 ;

  return 0==1 ;
}

void
CreeMatriceAdjacence
(MatriceAdjacence_t mat)
{

  int i,j ;

  /* on parcours tous les mots du dictionnaires */
  for(i=0; i<TAILLE_DICO;i++)
  {
    /* Pour chaque mots, on compare avec tous les autres mots pour savoir si ce
       sont des successeurs. */
     mat[i][i]=0 ; /* on exclut le mot lui-m\^eme */
    for(j=i+1; j<TAILLE_DICO;j++) /* la matrice d'adjacence est sym\'etrique */
      mat[j][i]=mat[i][j]=estSuccesseur(dico[i],dico[j]) ;
   }
   return ;
}

/* une fonction d'affichage -------------------------------------------------------- */

void
AffichePileInverse
(Pile_t pile)
{
  if(!pile)
     return ;
  AffichePileInverse(pile->next) ;
  printf("%s -> ",dico[pile->mot]) ;
  return ;
}

/* la fonction de parcours -------------------------------------------------------- */

int ConvertionMotIndice(char *mot1) {

  int i,gauche,droite,stop ;

  /* La recherche proprement dit */
  gauche = 1 ;
  droite = TAILLE_DICO ;
  do{
      i = (droite + gauche)/2 ;
      stop =strcmp(dico[i],mot1)  ;
      if (stop == 0)
	return i ;
      else if (stop<0)
        gauche = i +1 ;
      else droite = i -1 ;
  } while ( gauche <= droite) ;

  return -1 ;
}

/* la fonction chemin prend en argument
  l'indice du premier mot
  l'indice du second mot
 la matrice d'incidence du graphe associe au dictionnaire */

int
Chemin
(int sommet, int sommetdestination, MatriceAdjacence_t mat, Pile_t *parcours, int *dejaparcouru)
{
  int i ;
  if (sommet==sommetdestination)
    return 1 ; /* on est arriv\'e */

  for(i=0;i<TAILLE_DICO;i++)
    if (mat[sommet][i]==1 && dejaparcouru[i]==NONPARCOURU)
    {
       empiler(i,parcours) ;
       dejaparcouru[i] = PARCOURU ;
       if(Chemin(i,sommetdestination,mat,parcours,dejaparcouru)==1)
       	     return 1 ; /* le chemin est bon, c'est fini */
       else  depiler(parcours) ; /* non c'\'etait pas la bonne direction */
    }

  return 0 ;
}


/* pour utiliser la fonction qsort de la librairie standard ---------------*/
int
mycompar
(const void *p1, const void *p2)
{
char **str1, **str2 ;
str1 = (char **) p1 ;
str2 = (char **) p2 ;
return strcmp(*str1,*str2) ;
}


/* -------------------------------------------------------------------------- */

int
main
(int argc, char **argv)
{
  int dejaparcouru[TAILLE_DICO] ;
  MatriceAdjacence_t MatriceAdjacence ;
  int i,j ;
  Pile_t parcours ;
  atf_init();
  if(argc!=3)
  {
	printf("Usage~: %s mot1 mot2\n",argv[0]);
	printf(" mot1 and mot2 in dico4lettre.h\n") ;
	return -1 ;
  }

  /* On va utiliser de la recherche dichotomique plus tard
     il nous faut donc trier notre tableau dico */
  /* TriBulle() ; */
  qsort((void *) dico,TAILLE_DICO,sizeof(char *), mycompar) ;

  for(i=0;i<TAILLE_DICO-1;i++)
     if(!strcmp(dico[i],dico[i+1]))
	printf("%s\n",dico[i]) ;

  CreeMatriceAdjacence(MatriceAdjacence) ;
  /* on construit un tableau des sommets d\'ej\`a parcouru */
  for(i=0;i<TAILLE_DICO;i++)
    dejaparcouru[i] = NONPARCOURU ;

  if ((i = ConvertionMotIndice(argv[1]))==-1){
    printf("Le mot %s n'est pas dans le dictionnaire\n",argv[1]) ;
    exit(1);
  }

  if ((j = ConvertionMotIndice(argv[2]))==-1){
    printf("Le mot %s n'est pas dans le dictionnaire\n",argv[2]) ;
    exit(1);
  }

  /* initialisation de la pile */
  parcours = NULL ;
  empiler(i,&parcours) ;
  dejaparcouru[i] = PARCOURU ;
  switch(Chemin(i,j,MatriceAdjacence,&parcours,dejaparcouru)){
  case 1 :
    {
    printf("Le chemin existe\n");
    AffichePileInverse(parcours) ;
    printf("\n") ;
    break ;
    }
  case 0 :
    printf("\n ;-( ces mots ne peuvent etre lies\n"); break ;
  default : printf("\n Je ne comprend pas ce qui se passe\n") ; break;
  }

  return 0 ;
}

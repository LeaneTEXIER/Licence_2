#define PILEVIDE -1
#define ALLOCATIONIMPOSSIBLE -2

/* Les fonctions de manipulation de la pile */

struct File
{
  int mot ; /* la position dans le tableau tri\'e */
  struct File * next ;
} ;

/* D\'efinition d'une pile */

struct Pile
{
  int mot ; /* la position dans le tableau tri\'e */
  struct Pile * next ;
  /* struct File * chemin ; */
}  ;

typedef struct Pile *Pile_t ;

/* fonctions de manipulation de file */

void vider (Pile_t *) ;
void empiler (int , Pile_t *) ;
int depiler (Pile_t *) ;
int estVide (Pile_t ) ;

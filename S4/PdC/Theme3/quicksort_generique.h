extern void quicksort(void* base, int nelem, int size, int(*compar)(const void *a, const void *b));
/* Tri generique avec :
base une référence sur le premier élément du tableau à trier ;
nelem le nombre d’éléments du tableau à trier ;
size la taille, en octets, d’un élément du tableau ;
compar un pointeur sur la fonction de comparaison.
*/

extern int comparstr(const void * ch1, const void * ch2);
/* Compare 2 chaines de caractères */

extern int compar (const void * nb1, const void * nb2);
/* Compare 2 entiers */

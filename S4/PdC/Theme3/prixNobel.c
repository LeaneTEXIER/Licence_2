#include <stdio.h>
#include <string.h>
#include "macro_prix.h"

enum domaine_e{LITERATURE, PHYSICS, CHEMISTRY, PEACE, PHYSIOLOGY_OR_MEDICINE};
typedef enum domaine_e domaine;

enum genre_e{MALE, FEMALE};
typedef enum genre_e genre;

struct Nomine_s{int date; /*Année obtention du prix*/
                domaine dom;
                char name[sizeName];
                int j,m,a; /* Date de naissance */
                char country[sizeCountry];
                genre g;
             };

struct Nomine_s tab[MAXTAB];

void read_espace(){
  char c;
  do{
    c=getchar();
  }while (c!='"');
}

void read_chaine(char tab[], int taille){
  int i;
  char c;
  i=0;
  c=getchar();
  do{
    if (c!='"'){
      tab[i++]=c;
    }
    c=getchar();
  }while (c!='"');
  tab[i]='\0';
}


int read_entier(){
  int c;
  int resultat;
  resultat=0;
  c=getchar();
  if (c==EOF){
    return 0;
  }
  else if (c==34){
    c=getchar();
  }
  do{
    resultat = (resultat*10)+(c-'0');
    c=getchar();
  }while ((c!=' ') && (c!='-') && (c!='"') && (c!=9));
  return resultat;
}

int construireTableaux(struct Nomine_s *tab){
  int i,j;
  char tmp[32];
  char nom[sizeName];
  char pays[sizeCountry];
  char c;
  i = 0;
  while (1){
    j = read_entier();
    if (j==0){
      return i;
    }
    tab[i].date = j;
    read_chaine(tmp, 22);
    if (!strcmp(tmp,"Physics")){
      tab[i].dom = PHYSICS;
    }
    else if (!strcmp(tmp,"Chemistry")){
      tab[i].dom = CHEMISTRY;
    }
    else if (!strcmp(tmp,"Physiology or Medicine")){
      tab[i].dom = PHYSIOLOGY_OR_MEDICINE;
    }
    else if (!strcmp(tmp,"Literature")){
      tab[i].dom = LITERATURE;
    }
    else if (!strcmp(tmp,"Peace")){
      tab[i].dom = PEACE;
    }
    read_espace();
    read_chaine(nom, sizeName);
    j = 0;
    while (nom[j]){
      tab[i].name[j] = nom[j++];
    }
    getchar();
    tab[i].a = read_entier();
    tab[i].m = read_entier();
    tab[i].j = read_entier();
    read_espace();
    read_chaine(pays, sizeCountry);
    j = 0;
    while (pays[j]){
      tab[i].country[j] = pays[j++];
    }
    read_espace();
    read_chaine(tmp, 6);
    if (!strcmp(tmp, "male")){
      tab[i].g = MALE;
    }
    else if (!strcmp(tmp, "female")){
      tab[i].g = FEMALE;
    }
    i++;
    getchar();
  }
}

int CompareNomineParAgeDObtention(struct Nomine_s s1, struct Nomine_s s2){
  int date1, a1, age1, date2, a2, age2;
  date1 = s1.date;
  a1 = s1.a;
  date2 = s2.date;
  a2 = s2.a;
  age1 = date1-a1;
  age2 = date2-a2;
  if (age1>age2){
    return 1;
  }
  else if (age1<age2){
    return -1;
  }
  else{
    return 0;
  }
}

int main(int argc, char *argv[]){
  int taille,i,j;
  i = 0;
  struct Nomine_s tab[MAXTAB];
  taille = construireTableaux(tab);
  while (tab[i].j!=0){
    printf("Date du prix: %i\n", tab[i].date );
    char * domaines[] = {"LITERATURE", "PHYSICS", "CHEMISTRY", "PEACE", "PHYSIOLOGY_OR_MEDICINE"};
    printf("Domaine: %s\n", domaines[tab[i].dom]);
    printf("Nom et prenom: ");
    j = 1;
    while (tab[i].name[j]){
      printf("%c", tab[i].name[j++]);
    }
    printf("\n");
    printf("Jour de naissance: %i\n", tab[i].j);
    printf("Mois de naissance: %i\n", tab[i].m);
    printf("Annee de naissance: %i\n", tab[i].a);
    printf("Pays d'origine: ");
    j = 1;
    while (tab[i].name[j]){
      printf("%c", tab[i].country[j++]);
    }
    printf("\n");
    char * sexe[] = {"MALE", "FEMALE"};
    printf("Sexe: %s\n", sexe[tab[i].g]);
    printf("\n");
    i++;
  }
  /*printf("%i\n",CompareNomineParAgeDObtention(tab[0], tab[1]));
  printf("%i\n",CompareNomineParAgeDObtention(tab[780], tab[781]));
  printf("%i\n",CompareNomineParAgeDObtention(tab[5], tab[6]));*/
  return taille;
}

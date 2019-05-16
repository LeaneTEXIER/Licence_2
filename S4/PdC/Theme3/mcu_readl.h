extern int readl(int line[]);
/* Lit une ligne sur l'entr\'ee standard gr\^ace \`a getchar (cf. man).
   Cette ligne doit comporter moins de MAXLINE caract\`eres.

   Le r\'esultat est retourn\'e dans line (passage de param\`etre
   par r\'ef\'erence).
   Un \0 est \'ecrit en fin de la cha\^\i{}ne.

   Ainsi, le tableau line doit \^etre de taille au moins MAXLINE+1.

   Retourne le nombre de caract\`eres lu, non compris le \0 final.
   Retourne EOF si la fin de fichier est atteinte.

   Termine le programme sur une erreur si rencontre une ligne de plus
   de MAXLINE caract\`eres et retourne 1 gr\^ace \`a la fonction exit
   (cf. man). */

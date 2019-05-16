<?php
/*Léane Texier*/
header("Content-Type: text/plain;charset=UTF-8");
require_once("lib/fonctionsLivre.php");    // inclusion de fichier

/* Test question 1.1
 */
 /*
$ligneOK = " nom_de_prop : machin chose ";
$ligneKO = " nom_de_prop  machin chose ";
echo '|'.propertyName($ligneOK).'|';
echo "\n";
echo '|'.propertyValue($ligneOK).'|';
echo "\n";
echo '|'.propertyValue($ligneKO).'|';
*/

/* Test question 1.2
 */
 /*
$file = fopen('data/exempleLivre.txt','r');
$livre = readBook($file);
print_r($livre);
*/

/* Test question 1.3.1
  */
 /*
print_r(elementBuilder('titre','h2','La marque du diable'));
*/

/* Test question 1.3.2
  */
  /*
print_r(authorsToHTML("Marini - Desberg"));
*/

/* Test question 1.3.3
  */
/*
print_r(coverToHTML('scorpion.jpg'));
*/

/* Test question 1.3.4
  */
/*
print_r(propertyToHTML('titre','La marque du diable'));
echo "\n";
print_r(propertyToHTML('auteurs','Marini - Desberg'));
echo "\n";
print_r(propertyToHTML('couverture','scorpion.jpg'));
echo "\n";
print_r(propertyToHTML('année','2000'));
echo "\n";
print_r(propertyToHTML('catégorie','bandes-dessinées'));
*/

/* Test question 1.3.5
  */
/*
$book = fopen('data/exempleLivre.txt','r');
$article = bookToHTML(readBook($book));
print_r($article);
*/


/* Test question 2.2
*/
$file = fopen('data/livres.txt','r');
print_r(libraryToHTML($file));
  ?>

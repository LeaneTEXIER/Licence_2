<?php
/*Léane Texier*/
require("fonctionsLivre.php");

/*Exercice1 */
function compareAbs($i,$j){
  return abs($i)-abs($j);
}

function comparerChainesParLongueur($s1,$s2){
  return strlen($s1)-strlen($s2);
}

function comparerChainesParLongueurPlus($s1,$s2){
  $comp=strlen($s1)-strlen($s2);
  if ($comp!==0){
    return $comp;
  }
  else{
    return -strcmp($s1,$s2);
  }
}

/*Exercice2 */
function loadBiblio($file){
  $tab=array();
  $i=0;
  while (($book=readBook($file))!=='FALSE'){
    $tab[$i]=$book;
    $i++;
  }
  return $tab;
}

function biblioToHTML($liste, $sort="none"){
  $htmlBooks="";
  if ($sort=='titles'){
    usort($liste,'compareBooksTitle');
  }
  if ($sort=='categories'){
    usort($liste,'compareBooksCategorie');
  }
  if ($sort=='none' || $sort=='titles' || $sort=='categories'){
    for ($i=0; $i<sizeof($liste); $i++){
      $htmlBooks.=bookToHTML($liste[$i]);
    }
  }
  else{
    throw new Exception("Tri invalide, mettre titles ou none ou rien");
  }
  return $htmlBooks;
}

function compareBooksTitle($book1, $book2){
  return strcmp($book1['titre'],$book2['titre']);
}

function compareBooksCategorie($book1,$book2){
  $comp=strcmp($book1['catégorie'],$book2['catégorie']);
  if ($comp===0){
    return compareBooksAnnee($book1,$book2);
  }
  else{
    return $comp;
  }
}

function compareBooksAnnee($book1,$book2){
  $comp=$book1['année']-$book2['année'];
  if ($comp===0){
    return compareBooksTitle($book1,$book2);
  }
  else{
    return $comp;
  }
}

?>

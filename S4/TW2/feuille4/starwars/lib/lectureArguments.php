<?php
/* Léane Texier */
 $civilite = $_GET['civilite'];
 $adhesion = $_GET['adhesion'];
 $nom = $_GET['nom'];
 $prenom = $_GET['prenom'];
 $voie = $_GET['voie'];
 $commune = $_GET['commune'];
 $compl = $_GET['compl'];
 $cp = $_GET['cp'];
 $fig = $_GET['fig'];

 function page_erreur(){
   require("starWars.php");
   exit();
 }

 /* verification de l'adhésion */
  $adhesionAllow=array_fill_keys(array('dejaMembre','oui','non'),TRUE);
  if (! isset($adhesion)){
    $error='Adhésion invalide';
    page_erreur();
  }
  else if (! isset($adhesionAllow[$adhesion])){
    $error='Adhésion invalide';
    page_erreur();
  }

  /* verification de la civilité */
  $civiliteAllow=array_fill_keys(array('Mr','Mme'),TRUE);
  if (! isset($civilite)){
    $error='Civilité invalide';
    page_erreur();
  }
  else if (! isset($civiliteAllow[$civilite])){
    $error='Civilité invalide';
    page_erreur();
  }

  /* verification des noms des figurines */
  $figAllow=array_fill_keys(array("Maître Yoda","Luke Skywalker","Anakin Skywalker","Dark Vador","Obi-Wan Kenobi","Han Solo","Princesse Leia","Padmée Amidala","Empereur Palpatine",
   "C3PO","Chewbacca","Rey","Finn","Poe Dameron","Kylo Ren"),TRUE);
  if (! isset($fig)){
    $error='Figurine invalide';
    page_erreur();
  }
  foreach ($fig as $figure) {
    if (! isset($figAllow[$figure])){
      $error='Figurine invalide';
      page_erreur();
    }
  }

  /* verification de la validité du code postal */
  $codepo = filter_input(INPUT_GET, 'cp', FILTER_VALIDATE_INT);
  if ($codepo === NULL || $codepo === FALSE || strlen($cp)!==5){
    $error='Code postal invalide';
    page_erreur();
  }

  /* verification que les autres champs obligatoires sont non vides */
  if (strlen($nom)===0){
    $error='Nom vide';
    page_erreur();
  }

  if (strlen($prenom)===0){
    $error='Prénom vide';
    page_erreur();
  }

  if (strlen($voie)===0){
    $error='Numéro et voie vide';
    page_erreur();
  }

  if (strlen($commune)===0){
    $error='Ville vide';
    page_erreur();
  }



?>

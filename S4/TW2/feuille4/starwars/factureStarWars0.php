<?php
/* Léane Texier */
require_once('lib/Facture.class.php');
require_once('lib/lectureArguments0.php');

$facture=new Facture($nom, $prenom, $civilite, $voie, $complAd, $cp ,$commune);

foreach ($fig as $figurine){
  $facture->ajouterFigurine($figurine);
}

if ($adhesion==='oui'){
  $facture->ajouterAdhesion();
}

if ($adhesion==='dejaMembre'){
  $facture->setAdherent();
}

?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Facture du club des fans de Star Wars</title>
 <link rel="stylesheet" type="text/css" href="factureStarWars.css" />
 <style type="text/css">

 </style>
</head>
<body>
  <?php
    echo $facture->toHTML();
  ?>
</body>
<html>

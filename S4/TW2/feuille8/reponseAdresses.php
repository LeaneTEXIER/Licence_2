<?php
    /*Léane Texier*/
    require_once("lib/fonctions.php");
    function page_erreur(){
      require_once("page_erreur.html");
      exit();
    }
    /* Vérifie que les 2 codes sont définis en get */
    if (!isset($_GET['cCommune']) || !isset($_GET['cCommune'])){
      page_erreur();
    }
    /* Vérifie la taille des 2 codes */
    if (strlen($_GET['cCommune'])!=5 || strlen($_GET['cVoie'])!=4){
      page_erreur();
    }
    /* Verifie que les codes sont composés que de chiffres et lettres majuscules */
    for ($i=0; $i<5; $i++){
      if (!ctype_upper($_GET['cCommune'][$i]) && !ctype_digit($_GET['cCommune'][$i])){
        page_erreur();
      }
    }
    for ($i=0; $i<4; $i++){
      if (!ctype_upper($_GET['cVoie'][$i]) && !ctype_digit($_GET['cVoie'][$i])){
        page_erreur();
      }
    }
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Reponses adresses</title>
</head>
<body>
  <?php
    /* Retourne la liste */
    return (listeAdresses($_GET['cCommune'],$_GET['cVoie']));
  ?>
</body>
</html>

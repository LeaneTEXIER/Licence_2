<?php
    /*Léane Texier*/
    require_once("lib/fonctions.php");
    function page_erreur(){
      require_once("page_erreur.html");
      exit();
    }
    /* Vérifie que le code commune est en get */
    if (!isset($_GET['cCommune'])){
      page_erreur();
    }
    /* Vérifie la taille du code */
    if (strlen($_GET['cCommune'])!=5){
      page_erreur();
    }
    /* Verifie que le code est composés que de chiffres et lettres majuscules */
    for ($i=0; $i<5; $i++){
      if (!ctype_upper($_GET['cCommune'][$i]) && !ctype_digit($_GET['cCommune'][$i])){
        page_erreur();
      }
    }
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Formulaire adresses</title>
</head>
<body>
 <?php
    return (formVoies($_GET['cCommune'],"reponseAdresses.php"));
  ?>
</body>
</html>

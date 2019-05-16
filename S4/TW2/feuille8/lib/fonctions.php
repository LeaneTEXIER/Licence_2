<?php
  /* TEXIER Léane */
  function formVoies($cc, $url){
    require("connexion.php");
    $stnt = $connexion->prepare(
      "select code_voie, nom_voie
      from voies
      where code_commune = '".$cc."'"
    );
    $stnt->execute();
    $stnt->setFetchMode(PDO::FETCH_ASSOC);
    $ligne = $stnt->fetch();
    echo "<form action=\"".$url."\" id=\"formulaire\" method=\"get\">";
    echo "<select id=\"voie\" name=\"cVoie\">";
    while ($ligne){
      echo "<option value = \"{$ligne['code_voie']}\">{$ligne['nom_voie']}</option>";
      $ligne = $stnt->fetch();
    }
    echo "</select>";
    echo "<input type=\"hidden\" id=\"commune\" name=\"cCommune\" value=\"".$cc."\"/>";
    echo "<button name=\"valid\" type=\"submit\">Chercher</button>";
    echo "</form>";
  }



  /* Renvois la liste de toutes les adresses disponibles dans la voie cv de la commune cc */
  function listeAdresses($cc, $cv){
    require("connexion.php");
    $stnt = $connexion->prepare(
      "select numero
      from adresses
      where code_commune = '".$cc."' and code_voie = '".$cv."'"
    );
    $stnt->execute();
    $stnt->setFetchMode(PDO::FETCH_ASSOC);
    $ligne = $stnt->fetch();
    echo "<ul>";
    while ($ligne){
      echo "<li>{$ligne['numero']}</li>";
      $ligne = $stnt->fetch();
    }
    echo "</ul>";
  }
?>

<?php
/* Léane Texier */
function tab($parsed_json){
  echo "<table id='TableauStations'>";
  /* En tete du table */
  echo "<thead>";
  echo "<tr id='titres'>";
  echo "<th> Station </th>";
  echo "<th> Commune </th>";
  echo "<th> Nb Vélos dispo </th>";
  echo "<th> Nb places dispo </th>";
  echo "</tr>";
  echo "</thead>";
  /*Informations de chaque station */
  echo "<tbody>";
  for ($i=0; $i<sizeof($parsed_json['records']); $i++){
    /* Coordonnées */
    $coord = $parsed_json['records'][$i]['geometry']['coordinates'];
    $lon = $coord[0];
    $lat = $coord[1];
    /* Infos pour le tableau */
    $info = $parsed_json['records'][$i]['fields'];
    $nom = $info['nom'];
    $nom_sta = nom($nom);
    $commune = $info['commune'];
    $nbVel = $info['nbVelosDispo'];
    $nbPla = $info['nbPlacesDispo'];
    /* Ligne du tableau */
    echo "<tr data-lat='".$lat."' data-lon='".$lon."'>";
    echo "<td class='nom'><a href=\"infos.php?lat=".$lat."&lng=".$lon."\">".$nom_sta."</a></td>";
    echo "<td class='commune'>".$commune."</td>";
    echo "<td class='velos'>".$nbVel."</td>";
    echo "<td class='places'>".$nbPla."</td>";
    echo "</tr>";
  }
  echo "</tbody>";
  echo "</table>";
}


/* Nom de la station sans numéro et cb */
function nom($nom){
  $espace = strpos($nom, " ");
  $cb = strpos($nom, "(CB)");
  if ($cb===false){
    return (substr($nom, $espace));
  }
  else{
    return (substr($nom, $espace, $cb-3));
  }
}


function infos_comp($parsed_json){
  /* Récupération des données */
  $info = $parsed_json['records'][0]['fields'];
  $nom = $info['nom'];
  $nom_sta = nom($nom);
  $commune = $info['commune'];
  $adresse = $info['adresse'];
  $numero = numero($nom);
  $cb = $info['type'];
  /* Ecriture des données */
  echo "<p id='station'>".$numero.": ".$nom_sta."</p>";
  echo "<p id='adresse'>".$adresse."</p>";
  echo "<p id='commune'>".$commune."</p>";
  if ($cb=== 'AVEC TPE'){
    echo "<p id='cb'>Borne acceptant les cartes bancaires </p>";
  }
  else{
    echo "<p id='cb'>Borne n'acceptant pas les cartes bancaires </p>";
  }
}


/* Numéro de la station */
function numero($nom){
  $espace = strpos($nom, " ");
  return (substr($nom, 0, $espace));
}


function infos_carte($parsed_json){
  /* Coordonnées */
  $coord = $parsed_json['records'][0]['geometry']['coordinates'];
  $lon = $coord[0];
  $lat = $coord[1];
  /* Nombre de places et velos dispos */
  $info = $parsed_json['records'][0]['fields'];
  $nbVel = $info['nbVelosDispo'];
  $nbPla = $info['nbPlacesDispo'];
  echo "<p class='lat'>".$lat."</p>";
  echo "<p class='lng'>".$lon."</p>";
  echo "<p class='velos'>".$nbVel."</p>";
  echo "<p class='places'>".$nbPla."</p>";
}
?>

<?php
/* Texier Léane */
$configContext = array(
        'http' => array(
                'proxy' => 'tcp://cache.univ-lille1.fr:3128',
                'request_fulluri' => true
        )
);
stream_context_set_default($configContext);
require_once("lib/data.php");
function page_erreur(){
  require("page_erreur.html");
  exit();
}
$enSer = "EN SERVICE";
if ($_POST['crit']=="communes"){
  if (($_POST['nomSC'])==null){
    page_erreur();
  }
  $crit = 'le nom de commune';
  $fp = fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&refine.etat=".$enSer."&refine.commune=".strtoupper($_POST['nomSC']), "r");
}
else if ($_POST['crit']=="stations"){
  if (($_POST['nomSC'])==null){
    page_erreur();
  }
  $crit = 'le nom de station';
  $fp = fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&refine.etat=".$enSer."&q=nom:".$_POST['nomSC'], "r");
}

else if ($_POST['crit']=="velosD"){
  if (($_POST['disponibilite'])==null){
    page_erreur();
  }
  $crit = 'le nombre de vélos disponibles';
  $fp = fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&refine.etat=".$enSer."&q=nbVelosDispo>".$_POST['disponibilite'], "r");
}
else if ($_POST['crit']=="placesD"){
  if (($_POST['disponibilite'])==null){
    page_erreur();
  }
  $crit = 'le nombre de places disponibles';
  $fp = fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&&refine.etat=".$enSer."q=nbPlacesDispo>".$_POST['disponibilite'], "r");
}
else if ($_POST['crit']=="distance"){
  if (($_POST['lat'])==null || ($_POST['lng'])==null || ($_POST['dist'])==null){
    page_erreur();
  }
  $crit = 'une distance';
  $fp = fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&refine.etat=".$enSer."&geofilter.distance=".$_POST['lat'].",".$_POST['lng'].",".$_POST['dist'], "r");
}
else{
  page_erreur();
}

$inter = fgets($fp);
$parsed_json = json_decode($inter,true);
if ($parsed_json['nhits']==0){
  page_erreur();
}

?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Stations V'liVe séléctionné suivant un critère</title>
        <meta charset="UTF-8" />
        <script type="text/javascript" src="lib/vlive.js"></script>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
        <script src="lib/scriptCarte.js"></script>
        <link rel="stylesheet" href="vliVe.css" />
    </head>
    <body>
        <header>
            <?php
              echo "<h1>Stations V'liVe séléctionnées suivant ".$crit."</h1>";
            ?>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
            <p> Un clic sur le nom d'une station ou sur le marqueur correspondant à une station, vous donnera de plus amples informations sur la station. </p>
        </header>
	      <div id='carte'>
        </div>
	      <div id='tableau'>
          <?php
            printf (tab($parsed_json));
           ?>
        </div>
        <div id="credits">
          <a href="credits.html">Crédits</a>
        </div>
    </body>
  </html>

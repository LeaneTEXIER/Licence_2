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

  $lat = $_GET['lat'];
  $lng = $_GET['lng'];

  if (!isset($lat) || !isset($lng) || !is_numeric($lat) || !is_numeric($lng)){
    page_erreur();
  }

  $enSer = "EN SERVICE";
  $fp=fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&refine.etat=".$enSer."&geofilter.distance=".$lat.",".$lng.",0", "r");
  $inter = fgets($fp);
  $parsed_json = json_decode($inter,true);
  if ($parsed_json['nhits']==0){
    page_erreur();
  }
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Informations sur la station</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
        <script src="lib/ScriptCarteInfosComp.js"></script>
        <link rel="stylesheet" href="vliVe.css" />
    </head>
    <body>
        <header>
            <h1>Informations sur la station</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
        </header>
        <div id="Infos_complementaires">
          <?php
            printf (infos_comp($parsed_json));
          ?>
        </div>
        <div id="carteInfos">
        </div>
        <div id="Infos_Carte">
          <?php
            printf (infos_carte($parsed_json));
          ?>
        </div>
        <div id="credits">
          <a href="credits.html">Crédits</a>
        </div>
    </body>
  </html>

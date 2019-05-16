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
$enSer = "EN SERVICE";
$fp = fopen("compress.zlib://https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&timezone=Europe/Paris&rows=250&refine.etat=".$enSer, "r");
$inter = fgets($fp);
$parsed_json = json_decode($inter,true);
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Station V'liVe</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
        <script src="lib/scriptCarte.js"></script>
        <link rel="stylesheet" href="vliVe.css" />
    </head>
    <body>
        <header>
            <h1>Station V'liVe</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
            <p> Un clic sur le nom d'une station ou sur le marqueur correspondant à une station, vous donnera de plus amples informations sur la station. </p>
        </header>
        <div id="LienFormulaire">
          <a href="formulaireStation.html">Trier par...</a>
        </div>
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

<!DOCTYPE html>
<!--Léane Texier-->
<?php
  require_once("lib/fonctionsSVG.php");
  function page_erreur(){
    require("page_erreur.html");
    exit();
  }
  /* Tests pour savoir si toutes les variables obligatoires sont definies
  et sont des valeurs numériques */
  if (!isset($_GET['cx']) || !isset($_GET['cy']) || !isset($_GET['r'])  ||
  !is_numeric($_GET['cx']) || !is_numeric($_GET['cy']) || !is_numeric($_GET['r'])){
    page_erreur();
  }
  $cx = $_GET['cx'];
  $cy = $_GET['cy'];
  $r = $_GET['r'];
  /*Test pour savoir si angle est défini et définir sa valeur*/
  if (isset($_GET['angle'])){
    if (!is_numeric($_GET['angle'])){
      page_erreur();
    }
    $a= $_GET['angle'];
  }
  else{
    $a=0;
  }
  /* Test pour savoir si la figure demandée est valable*/
  if ((!isset($_GET['fig'])) || (! in_array ($_GET['fig'], array("cercle","carre","triangle")))){
    page_erreur();
  }
  $fig = $_GET['fig'];
?>
<html xmlns="http://www.w3.org/1999/xhtml" lang="fr" xml:lang="fr">
    <head>
        <meta charset="UTF-8" />
        <title>Test SVG</title>
        <style>
            * {
                font-family : sans-serif;
            }
            svg {
                width : 400px;
                height: 400px;
                border : solid 1pt black;
            }
            #dessin * {
                fill-opacity : 0.7;
            }
            svg rect {
                fill : lightblue;
                stroke : black;
            }
            svg circle {
                fill : red;
            }
            svg polygon {
                fill : black;
            }
            line.axe {
                stroke : grey;
                stroke-width : 1;
            }
            line.marque {
                stroke : grey;
                stroke-width : 1;
            }
            svg text {
                text-anchor : middle;
                font-size:7pt;

            }
        </style>
    </head>
    <body>
        <h1>Test SVG</h1>
        <svg viewbox="-320,-320,640,640" preserveAspectRatio="xMedYMed meet" xmlns="http://www.w3.org/2000/svg">
            <!-- axes et graduations -->
            <line class ="axe" id="axeX" x1="0" y1="0" x2="300" y2="0"/>
            <line class="axe" id="axey" x1="0" y1="0" x2="0" y2="300"/>
            <g transform="translate(100,0)">
                <line class="marque" x1="0" y1="0" x2="0" y2="-3" />:
                <text x="0" y="-4" fill="blue">100</text>
            </g>
            <g transform="translate(0,100) rotate (-90)">
                <line class="marque" x1="0" y1="0" x2="0" y2="-3" />:
                <text x="0" y="-4" fill="blue">100</text>
            </g>
            <g transform="translate(200,0)">
                <line class="marque" x1="0" y1="0" x2="0" y2="-3" />:
                <text x="0" y="-4" fill="blue">200</text>
            </g>
            <g transform="translate(0,200) rotate (-90)">
                <line class="marque" x1="0" y1="0" x2="0" y2="-3" />:
                <text x="0" y="-4" fill="blue">200</text>
            </g>
            <g transform="translate(300,0)">
                <line class="marque" x1="0" y1="0" x2="0" y2="-3" />:
                <text x="0" y="-4" fill="blue">300</text>
            </g>
            <g transform="translate(0,300) rotate (-90)">
                <line class="marque" x1="0" y1="0" x2="0" y2="-3" />:
                <text x="0" y="-4" fill="blue">300</text>
            </g>
            <!-- dessin   -->
            <g id="dessin">
              <?php
                if ($fig==='cercle'){
                  echo cercle($cx, $cy, $r);
                }
                else if ($fig==='carre'){
                  echo carre($cx,$cy,$r,$a);
                }
                else{
                  echo triangleInscrit($cx,$cy,$r,$a);
                }
              ?>
            </g>
        </svg>
    </body>
</html>

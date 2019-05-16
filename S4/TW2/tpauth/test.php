<?php
/*Léane Texier */
require_once('lib/Identite.class.php');
require('lib/auth.php');
$prenom = $_SESSION['ident']->getPrenom();
$nom = $_SESSION['ident']->getNom();
echo "Bienvenue ".$prenom." ".$nom."!";
require('logout.php');
 ?>

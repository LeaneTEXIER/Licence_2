<?php
/*Léane Texier */
require_once("biblio.php");
session_start();
try{
  controleAuthentification();
}catch(Exception $e){
  require_once('formuLogin.php');
  exit();
}
 ?>

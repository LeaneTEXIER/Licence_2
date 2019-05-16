<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $login = $_GET['login'];
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(abonnements($login));
 ?>

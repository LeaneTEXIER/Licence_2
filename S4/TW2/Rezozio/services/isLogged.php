<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  session_start();
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(isLogged());
?>

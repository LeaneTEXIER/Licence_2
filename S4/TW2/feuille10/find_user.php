<?php
  require_once("lib/biblio.php");
  session_start();
  $sujet = $_GET['interest'];
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(searchByInterest($sujet));
 ?>

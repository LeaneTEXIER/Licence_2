<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $follower = $_GET['follower'];
  $membre_suivi = $_GET['membre_suivi'];
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(AboDesabo($follower, $membre_suivi));
 ?>

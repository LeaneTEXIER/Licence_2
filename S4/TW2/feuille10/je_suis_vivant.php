<?php
  require_once('lib/auth.php');
  $ident = $_SESSION['ident'];
  require_once ("lib/biblio.php");
  $login = $ident->getLogin();
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(vivant($login));
?>

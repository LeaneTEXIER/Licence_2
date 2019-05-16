<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  session_start();
  $ident = $_SESSION['ident'];
  if (isset($ident)){
    $login = $ident->getLogin();
    $source = $_POST['source'];
    header("Content Type: application/json; charset=utf-8");
    echo json_encode(postMessage($source, $login));
  }
?>

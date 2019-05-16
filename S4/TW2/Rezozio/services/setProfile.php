<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  session_start();
  $ident = $_SESSION['ident'];
  if (isset($ident)){
    $login = $ident->getLogin();
    $name = $_POST['name'];
    $password = $_POST['password'];
    $description = $_POST['description'];
    header("Content Type: application/json; charset=utf-8");
    echo json_encode(setProfile($login, $name, $password, $description));
  }
 ?>

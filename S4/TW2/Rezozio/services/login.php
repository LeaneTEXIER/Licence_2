<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  if (isset($_SESSION['ident'])){
    exit();
  }
  session_start();
  $login = $_POST['login'];
  $password = $_POST['password'];
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(login($login, $password));
?>

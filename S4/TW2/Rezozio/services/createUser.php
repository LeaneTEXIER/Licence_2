<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $ident = $_POST['ident'];
  $password = $_POST['password'];
  $name = $_POST['name'];
  header("Content Type: application/json; charset=utf-8");
  echo json_encode(createUser($ident, $password, $name));
 ?>

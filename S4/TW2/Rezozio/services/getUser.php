<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $user = $_GET['user'];
  $type = $_GET['type'];
  header("Content Type: application/json; charset=utf-8");
  if (isset($type)){
    echo json_encode(getUser($user, $type));
  }
  else{
    echo json_encode(getUser($user));
  }
 ?>

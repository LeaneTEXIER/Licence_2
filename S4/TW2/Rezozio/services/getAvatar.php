<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $user = $_GET['user'];
  $size = $_GET['size'];
  if (isset($size)){
    getAvatar($user, $size);
  }
  else{
    getAvatar($user);
  }
?>

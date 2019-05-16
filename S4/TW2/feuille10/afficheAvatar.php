<?php
  require_once('lib/fonctionsAvatar.php');
  require_once('lib/auth.php');
  $ident = $_SESSION['ident'];
  $login = $ident->getLogin();
  afficheAvatar($login);
?>

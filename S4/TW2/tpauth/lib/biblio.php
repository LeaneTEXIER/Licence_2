<?php
/*Léane Texier */
function authentifier($login,$password){
  $file = fopen('lib/password.txt', 'r');
  $line=fgets($file);
  while ($line!==FALSE) {
    list($log, $pass, $nom, $prenom) = explode(";",$line);
    if ($log==$login && $pass==$password){
      return new Identite($login, $nom, $prenom);
    }
    $line=fgets($file);
  }
  return null;
}

function controleAuthentification(){
  if (isset($_SESSION['ident'])){
    return;
  }
  else if (isset($_REQUEST['login']) && isset($_REQUEST['password'])){
    $identity = authentifier($_REQUEST['login'], $_REQUEST['password']);
    if ($identity != null){
      $_SESSION['ident'] = $identity;
      return;
    }
  }
  throw new Exception("Authentification incorrecte");
  return;
}
 ?>

<?php
function __autoload($className){
  include 'lib/'.$className .'.class.php';
}

//require_once('lib/Identite.class.php');

/* Renvoie un tableau de 4 chaînes contenant les prochain
     login, password, nom et prenom
   puisés dans le fichier $file
  Renvoie null en fin de fichier ou si la prochaine ligne n'a pas le bon format
*/
function getUser($file)
{
 $ligne = fgets($file);
 if (! $ligne)
   return null;
 $tab = explode(";",$ligne);
 if (count($tab) != 4)
  return null;
 return $tab;
}

function randomSalt(){
  $salt = '$2a$10$';
  $caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  for ($i=0; $i<22; $i++){
    $salt .= $caracteres[rand()%strlen($caracteres)];
  }
  return $salt;
}

function addUser($login, $password, $nom, $prenom){
  require_once("lib/connexion.php");
  $passwordHache = crypt($_POST['password'],$salt);
  $stnt = $connexion->prepare(
    "insert into passwordfeuille10
    values(:login, :password, :nom, :prenom)"
  );
  $stnt->bindValue(':login',$login);
  $stnt->bindValue(':password',crypt($password,randomSalt()));
  $stnt->bindValue(':nom',$nom);
  $stnt->bindValue(':prenom',$prenom);
  return $stnt->execute();
}

function infoPersonne($login){
  require_once("lib/connexion.php");
  $stnt = $connexion->prepare(
    "select * from passwordfeuille10 where login=:login"
  );
  $stnt->bindValue(':login',$login);
  $stnt->execute();
  return $stnt->fetch();
}

/*
  Si login et password sont corrects, alors
  le résultat est une instance d'Identite décrivant cet utilisateur
  Sinon le résultat vaut null
*/
function authentifie($login, $password)
{
 $info = infoPersonne($login);
 if (!$info){
   return null;
 }
 if (crypt($password, $info['password'])!=$info['password']){
   return null;
 }
 return new Identite($login,$info['nom'],$info['prenom']);
}

/*
 Verifie l'authentification
 La fonction se termine normalement
 - Si l'état de la session indique que l'authentification a déjà eu lieu
 - Si des paramètres login/password corrects ont été fournis
 Après exécution correcte,  $_SESSION['ident'] contient l'identité de l'utilisateur
 Dans tous les autres cas, une exception est déclenchée
*/
function controleAuthentification()
{
  if (isset($_SESSION['ident'])){
    return;
  }
  $login = inputFilterString('login');
  $password = inputFilterString('password');
  $ident = authentifie($login,$password);
  if (! $ident)
   { $_SESSION['echec']=TRUE;
     throw new Exception('login/password incorrects');
   }
  $_SESSION['ident'] = $ident;  //ou serialize($ident);
  unset($_SESSION['echec']); // au cas où c'était positionné
  return;
}

function inputFilterString($name, $requis=TRUE){
  $v = filter_input(INPUT_POST, $name, FILTER_SANITIZE_STRING);
  if ( $requis && $v == NULL )
    throw new Exception("argument $name est requis");
 return $v;
}

function updateUser($login, $password, $nom, $prenom){
  require_once("lib/connexion.php");
  if ($password){
    $stnt = $connexion->prepare(
      "update passwordfeuille10
       set password =:password
       where login=:login"
    );
    $passwordHache = crypt($password,randomSalt());
    $stnt->bindValue(':login',$login);
    $stnt->bindValue(':password',$passwordHache);
    $stnt->execute();
    echo "<p>Mot de passe changé avec succès</p>";
  }
  if ($nom){
    $stnt = $connexion->prepare(
      "update passwordfeuille10
       set nom =:nom
       where login=:login"
    );
    $stnt->bindValue(':login',$login);
    $stnt->bindValue(':nom',$nom);
    $stnt->execute();
    echo "<p>Nom changé avec succès</p>";
  }
  if ($prenom){
    $stnt = $connexion->prepare(
      "update passwordfeuille10
       set prenom =:prenom
       where login=:login"
    );
    $stnt->bindValue(':login',$login);
    $stnt->bindValue(':prenom',$prenom);
    $stnt->execute();
    echo "<p>Prénom changé avec succès</p>";
  }
}

function ajoutInterets($interest,$login){
  require_once("lib/connexion.php");
  $centres = explode(",", $interest);
  for ($i=0; $i<count($centres); $i++){
    $stnt = $connexion->prepare(
      "insert into interets
       values(:login, :sujet)"
    );
    $stnt->bindValue(':login',$login);
    $stnt->bindValue(':sujet',$centres[$i]);
    $stnt->execute();
  }
}

function searchByInterest($sujet){
  require_once("lib/connexion.php");
  if (!isset($_GET['interest'])){
    $stnt = $connexion->prepare(
      "select login, nom, prenom
       from passwordfeuille10"
    );
  }
  else{
    $stnt = $connexion->prepare(
      "select passwordfeuille10.login, nom, prenom
       from passwordfeuille10, interets
       where passwordfeuille10.login = interets.login and sujet='".$_GET['interest']."'"
    );
  }
  $stnt->execute();
  $stnt->setFetchMode(PDO::FETCH_ASSOC);
  $ligne = $stnt->fetch();
  $users = array();
  while($ligne){
    $tab = [];
    $tab['login'] = $ligne['login'];
    $tab['nom'] = $ligne['nom'];
    $tab['prenom'] = $ligne['prenom'];
    array_push($users, $tab);
    $ligne = $stnt->fetch();
  }
  return $users;
}


function vivant($login){
  require_once("lib/connexion.php");
  // Supprimer ceux dont le timestamp date de plus de 30 secondes
  $stnt = $connexion->prepare(
    "delete from still_alive
     where stamp<now() - interval '30 seconds'"
  );
  $stnt->execute();
  //Supprimer l'utilisateur connecté
  $stnt = $connexion->prepare(
    "delete from still_alive
     values(:login)"
  );
  $stnt->bindValue(':login',$login);
  $stnt->execute();
  //Rajouter à nouveau l'utilisateur connecté avec le timestamp acuel
  $stnt = $connexion->prepare(
    "insert into still_alive
     values(:login)"
  );
  $stnt->bindValue(':login',$login);
  $stnt->execute();
  //Récupérer tous les logins restants
  $stnt = $connexion->prepare(
    "select login
    from still_alive"
  );
  $stnt->execute();
  $stnt->setFetchMode(PDO::FETCH_ASSOC);
  $ligne = $stnt->fetch();
  //Les mettre dans un tableau
  $log_vivants = array();
  while($ligne){
    $tab = [];
    $tab['login'] = $ligne['login'];
    array_push($log_vivants, $tab);
    $ligne = $stnt->fetch();
  }
  return $log_vivants;
}

?>

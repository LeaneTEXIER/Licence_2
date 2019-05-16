<?php
    require_once('lib/auth.php');
    $ident = $_SESSION['ident'];
    $login = $ident->getLogin();
    $password = $_POST['password'];
    $nom = $_POST['nom'];
    $prenom = $_POST['prenom'];
    require_once("lib/biblio.php");
    updateUser($login, $password, $nom, $prenom)
?>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
      <head>
        <meta charset="UTF-8"/>
        <title>Changement informations</title>
      </head>
      <body>
        <a href="index.php">Accueil</a>
        <a href="myAccount.php">Mon compte</a>
        <a href="afficheAvatar.php">Avatar</a>
        <a href="logout.php">Se déconnecter</a>
      </body>
    </html>

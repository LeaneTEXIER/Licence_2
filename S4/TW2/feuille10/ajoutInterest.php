<?php
    require_once('lib/auth.php');
    $ident = $_SESSION['ident'];
    $login = $ident->getLogin();
    require_once("lib/biblio.php");
    ajoutInterets($_POST['interest'],$login);
?>
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
      <head>
        <meta charset="UTF-8"/>
        <title>Ajout Centres d'interets</title>
      </head>
      <body>
        <p>Centre(s) d'intérêt(s) ajouté(s) avec succes</p>
        <a href="index.php">Accueil</a>
        <a href="myAccount.php">Mon compte</a>
        <a href="afficheAvatar.php">Avatar</a>
        <a href="logout.php">Se déconnecter</a>
      </body>
    </html>

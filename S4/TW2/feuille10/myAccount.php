<?php
  require_once('lib/auth.php');
  $ident = $_SESSION['ident'];
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
  <head>
    <meta charset="UTF-8"/>
    <title>Mon compte</title>
  </head>
<body>
  <h1> Mon compte </h1>
  <form name="password" method="POST" action="changeInformations.php">
   <fieldset>
    <label for="password">Nouveau mot de passe :</label><input type="password" name="password" id="password"/><br/>
    <label for="nom">Nouveau nom :</label><input type="text" name="nom" id="nom"/><br/>
    <label for="prenom">Nouveau prénom :</label><input type="text" name="prenom" id="prenom"/><br/>
    <button type="submit" name="valid">Valider</button>
   </fieldset>
  </form>
  <form name="interets" method="POST" action="ajoutInterest.php">
   <fieldset>
    <label for="interest">Centres d'intérêts(séparés par des virgules) :</label>
    <input type="text" name="interest" id="interest" required="required" /><br/>
    <button type="submit" name="valid">Valider</button>
   </fieldset>
  </form>
  <form name="avatar" method="POSt"  enctype="multipart/form-data" action="avatar.php" >
    <fieldset>
     <label for="avatar">Photo pour avatar :</label>
     <input type="file" name="avatar" required="required"/><br/>
     <button type="submit" name="valid">Valider</button>
    </fieldset>
  </form>
  <a href="index.php">Accueil</a>
  <a href="afficheAvatar.php">Avatar</a>
  <a href="logout.php">Se déconnecter</a>
</body>
</html>

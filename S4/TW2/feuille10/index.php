<?php
require_once('lib/auth.php');
$ident = $_SESSION['ident'];
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
  <head>
    <meta charset="UTF-8"/>
    <title>Page à accès contrôlé</title>
    <script src="libJs/requetes.js"></script>
  </head>
<body>
<h1>
<?php echo "Bienvenue ". $ident->getPrenom() . " " .$ident->getNom();
?>
</h1>
<form name="interets" method="post" action="">
 <fieldset>
  <label for="interest">Centre d'intérêt :</label>
  <input type="text" name="interest" id="interest" required="required" /><br/>
  <button type="button" onclick="requete_users()">Valider</button>
</fieldset>
</form>
<div id="resultsInterest"></div>
<div id="usersConnect"></div>
<a href="myAccount.php">Mon compte</a>
<a href="afficheAvatar.php">Avatar</a>
<a href="logout.php">Se déconnecter</a>
</body>
</html>

<?php
  require_once("lib/Identite.class.php");
  session_start();
  if (!isset($_SESSION['ident'])){
    header('Location: index.php');
    exit();
  }
  else{
    $ident = $_SESSION['ident'];
    $login = $ident->getLogin();
  }
 ?>
<!DOCTYPE html>
<!-- TEXIER Léane -->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
  <head>
    <meta charset="UTF-8"/>
    <title>Mise à jour</title>
    <script src="js/requetesMAJ.js"></script>
    <link rel="stylesheet" href="rezozioCSS.css" />
  </head>
<body>
  <div id="Accueil">
    <a href="index.php">Accueil</a>
  </div>
  <div id="MonCompte">
    <a href="pageMembre.php?login=<?php echo $login ?>">Mon Compte</a>
  </div>
  <h1> Mise à jour de mon profil</h1>
  <div id="MessageInformation"></div>
  <div id="FormulaireInformations">
    <form name="maj" id="maj" method="post" action="services/setProfile.php">
     <fieldset>
      <legend>Mise à jour de mes informations :</legend>
      <label for="name">Nouveau nom :</label>
      <input type="text" name="name" id="name" maxlength="25"/><br/>
      <label for="password">Nouveau mot de passe :</label>
      <input type="password" name="password" id="password"/><br/>
      <label for="description">Nouvelle description :</label>
      <textarea type="text" name="description" id="description" maxlength="2048" rows="10" cols="48"></textarea>
      <button name="valid" value="ok" type="submit">Valider</button>
     </fieldset>
    </form>
  </div>
  <div id="formulaireAvatar">
    <form name="avatarMAJ" id="avatarMAJ" method="post" enctype="multipart/form-data" action="services/uploadAvatar.php">
     <fieldset>
      <legend>Mise à jour de mon avatar :</legend>
      <label for="avatar">Nouvelle photo pour avatar (Formats acceptés: .jpeg, .jpg, .png, .gif, .bmp; Taille maximale: 2 Mo):</label>
      <input type="file" name="avatar" id="avatar"/><br/>
      <button name="valid" value="ok" type="submit">Valider</button>
     </fieldset>
    </form>
  </div>
  <div id="Credits">
    <a href="credits.php">Credits</a>
  </div>
</body>
</html>

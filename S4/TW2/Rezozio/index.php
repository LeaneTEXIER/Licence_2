<!DOCTYPE html>
<!-- TEXIER Léane -->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
  <head>
    <meta charset="UTF-8"/>
    <title>Rezozio</title>
    <script src="js/requetes.js"></script>
    <link rel="stylesheet" href="rezozioCSS.css" />
  </head>
<body>
  <div id="Buttons">
    <div id="Connexion"></div>
    <div id="Inscription"></div>
    <div id="MonCompte"></div>
    <div id="MessageInformation"></div>
  </div>
  <h1>Rezozio </h1>
  <div id="recherche">
    <form name="recherche_user" method="post" action="#">
     <fieldset>
      <legend>Recherche de messages :</legend>
      <label for="recherche_user">Nom ou login de la personne cherchée :</label>
      <input type="text" name="recherche_user" id="recherche_user" required="required" /><br/>
      <button type="button" onclick="requete_FindUsers()">Valider</button>
    </fieldset>
    </form>
    <div id="reponsesRecherche"></div>
  </div>
  <div id="postMessage"></div>
  <div id="Messages">
    <div id="ListeMessagesAcc"></div>
    <div id="ButtonMessages"></div>
  </div>
  <div id="Credits">
    <a href="credits.php">Credits</a>
  </div>
</body>
</html>

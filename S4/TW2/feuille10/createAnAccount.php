<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
  <head>
    <meta charset="UTF-8"/>
    <title>Create an account</title>
  </head>
  <body>
    <form method="POST" action="newAccount.php">
     <fieldset>
      <label for="login">Login :</label>
      <input type="text" name="login" id="login" required="required" />
      <label for="password">Mot de passe :</label>
      <input type="password" name="password" id="password" required="required" />
      <label for="nom">Nom :</label>
      <input type="text" name="nom" id="nom" required="required" />
      <label for="prenom">Prenom :</label>
      <input type="text" name="prenom" id="prenom" required="required" />
      <button type="submit" name="valid">OK</button>
     </fieldset>
    </form>
    <a href="index.php">Se connecter</a>
  </body>
</html>

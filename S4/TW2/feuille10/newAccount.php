<?php
    require_once("lib/biblio.php");
    $ligne = addUser($_POST['login'], $_POST['password'], $_POST['nom'], $_POST['prenom']);
?>
 <!DOCTYPE html>
 <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
   <head>
     <meta charset="UTF-8"/>
     <title>Nouveau compte</title>
   </head>
   <body>
     <?php
      if($ligne != 0){
        echo "<p>Compte créer avec succès</p>";
        echo "<a href=\"index.php\">Se connecter</a>";
      }
      else{
        echo "<p>Login déjà utilisé</p>";
        echo "<a href=\"createAnAccount.php\">Creer un compte</a>";
        echo "<a href=\"index.php\">Se connecter</a>";
      }
    ?>
   </body>
 </html>

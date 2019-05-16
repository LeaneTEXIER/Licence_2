<!DOCTYPE html>
<!--Léane Texier-->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Equipe sélectionnée</title>
</head>
<body>
  <?php
	require("connexion.php");
	$stnt = $connexion->prepare(
		"update etape set arrivee='".$_POST['time']."' where dossard=".$_POST['num']
	);
	$stnt->execute();
	$stnt->setFetchMode(PDO::FETCH_ASSOC);
  $ligne = $stnt->rowCount();
  if ($ligne==0){
    echo("Erreur: Numéro de dossard inconnu ou heure invalide");
  }
  require('question13.html');
  exit();
  ?>
</body>
</html>

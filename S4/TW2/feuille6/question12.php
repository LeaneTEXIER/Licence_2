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
		"select directeur, couleur, coureurs.nom
    from coureurs, equipes
    where equipe ='".$_POST['equipeName']."' and equipes.nom='".$_POST['equipeName']."'"
	);
	$stnt->execute();
	$stnt->setFetchMode(PDO::FETCH_ASSOC);
  $ligne = $stnt->fetch();
  if (!$ligne){
    echo("Erreur: Nom d'équipe inconnue");
    exit();
  }
  echo "<div id='InfosEquipes'>";
  echo "<h3> Nom du directeur : </h3><p>".$ligne['directeur']."</p>";
  echo "<h3> Couleur de l'équipe : </h3><p>".$ligne['couleur']."</p>";
  echo "</div>";
  echo "<div id='ListeCoureurs'><ul>";
  echo "<h3> Nom des coureurs: </h3>";
  while ($ligne){
		echo "<li>{$ligne['nom']}</li>";
    $ligne = $stnt->fetch();
	}
  echo "</ul></div>";
  ?>
</body>
</html>

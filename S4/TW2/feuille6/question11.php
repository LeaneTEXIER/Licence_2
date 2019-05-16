<!DOCTYPE html>
<!--Léane Texier-->
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Liste des coureurs</title>
 <style>
  table{
    border-collapse: collapse;
    text-align: center;
  }

  td, th{
    border: 2px solid black;
  }
</style>
</head>
<body>
  <?php
	require("connexion.php");
	$stnt = $connexion->prepare(
		"select coureurs.nom as prenom, equipes.nom, directeur
		from coureurs, equipes
		where equipe=equipes.nom"
	);
	$stnt->execute();
	$stnt->setFetchMode(PDO::FETCH_ASSOC);
	echo "<table>";
  echo "<thead><tr><th>Prenom</th><th>Nom d'équipe</th><th>Directeur</th></tr></thead>";
  echo "<tbody>";
	while ($ligne = $stnt->fetch()){
		echo "<tr><td>{$ligne['prenom']}</td>".
		     "<td>{$ligne['nom']}</td>".
		     "<td>{$ligne['directeur']}</td></tr>";
	}
  echo "</tbody>";
	echo "</table>";
  ?>
</body>
</html>

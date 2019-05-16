<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Séance 1b PHP - Exercice 3</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
    </head>
    <body>
        <header>
            <h1>Séance 1b PHP - Exercice 3</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
        </header>
	<section>
		<h2>Question 1</h2>
		<?php
			$chaine = "L'hiver il fait froid + Et il neige+ Donc il faut bien se couvrir +Pour ne pas être malade." ;
			$chaineCoup = explode("+", $chaine);
			for ($i=0; $i<sizeof($chaineCoup); $i++){
				echo "<p>".trim($chaineCoup[$i])."</p>";
			}
		?>
	</section>
	<section>
		<h2>Question 2</h2>
		<?php
			$s="Dupont - Durand";
			$sCouper = explode(" - ", $s);
			for ($i=0; $i<sizeof($sCouper); $i++){
				echo "<span>".$sCouper[$i]."</span>";
			}
		?>
	</section>
	<section>
		<h2>Question 3</h2>
		<?php
			function enSpan($s){
				$sCouper = explode(" - ", $s);
				for ($i=0; $i<sizeof($sCouper); $i++){
					echo "<span>".$sCouper[$i]."</span>";
				}
			}
			enSpan($s);
		?>
	</section>
    </body>
</html>

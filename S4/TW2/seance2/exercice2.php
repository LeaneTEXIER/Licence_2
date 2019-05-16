<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Séance 1b PHP - Exercice 2</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
	<script type="text/javascript" src="exercice2.js"></script>
    </head>
    <body>
        <header>
            <h1>Séance 1b PHP - Exercice 2</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
        </header>
	<section>
		<h2>Terrain de jeu</h2>
		<?php
			echo "<table id='Jeu'>\n";
			$tableauTerrain= array();
			$file = fopen('terrain.txt', 'r');
			$ligne = fgets($file);
			$longB = strlen($ligne)-2; /* -2 car il faut enlever le '\n' de la fin pour compter*/
			$long = strlen($ligne)-2;
			$cpt_Nb_Lignes = 0;
			$compteur=0;
			while ($ligne !== FALSE && $longB==$long) {
				$tableauTerrain[$cpt_Nb_Lignes]=$ligne;
				$cpt_Nb_Lignes +=1;
				$ligne = fgets($file);
				if ($ligne !== FALSE){
					$long = strlen($ligne)-2;	
				}	
			}
			if ($longB!==$long || $cpt_Nb_Lignes !== $longB){
				echo "<p> Terrain non valide </p>";
			}
			else {
				for ($i=0; $i<$longB; $i++){
					echo "<tr>";
					for ($j=0; $j<$longB; $j++){
						if ($tableauTerrain[$i][$j] == "-"){
							echo "<td  onclick=\"change_class('$compteur')\" class='vide' id='$compteur'> </td>"; 			
						}
						else if ($tableauTerrain[$i][$j] == "B"){
							echo "<td  onclick=\"change_class('$compteur')\" class='blanc' id='$compteur'><span>". $tableauTerrain[$i][$j]. "</span></td>";
						}
						else{
							echo "<td  onclick=\"change_class('$compteur')\" class='noir' id='$compteur'><span>". $tableauTerrain[$i][$j]. "</span></td>";
						}
					$compteur++;
					}
					echo "</tr>";
				}
			}
			echo "</table>";
			fclose($file);
		?>
	</section>
    </body>
</html>

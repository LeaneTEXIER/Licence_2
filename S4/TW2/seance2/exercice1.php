<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Séance 1b PHP - Exercice 1</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
    </head>
    <body>
        <header>
            <h1>Séance 1b PHP - Exercice 1</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
        </header>
	<section>
		<h2>Liste de noms</h2>
		<?php
			echo "<ul>\n";
			$file = fopen('liste_noms.txt', 'r');
			$ligne = fgets($file);
			while ($ligne !== FALSE) {
				echo "<li> $ligne </li>";
				$ligne = fgets($file);
			}
			echo "</ul>";
			fclose($file);
		?>
	</section>
    </body>
</html>

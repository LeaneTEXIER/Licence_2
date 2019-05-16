<!DOCTYPE html>
<!--Léane Texier-->
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Bibliothèque</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="feuille2.css" />
    </head>
    <body>
        <header>
            <h1>Bibliothèque</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
        </header>
	<section>
		<?php
			require_once("lib/fonctionsLivre.php");
        		$book = fopen('data/exempleLivre.txt','r');
            		echo (bookToHTML(readBook($book)))."\n";
    		?>
    	</section>
    </body>
</html>

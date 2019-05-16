<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Premier exercice PHP</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
    </head>
    <body>
        <header>
            <h1>Premier exercice PHP</h1>
            <h2>Réalisé par <span class="nom">Léane Texier</span></h2>
        </header>
        <section>
            <h2>Question 1</h2>
	    <?php 
		date_default_timezone_set("Europe/Paris");
		echo "<p> Nous sommes le ". date('d / m / Y'). ". </p>";
	    ?> 
        </section>
        <section>
            <h2>Question 2</h2> 
	    <?php
		echo "<p>La version PHP utilisée est ". PHP_VERSION.".";
		echo "Le système d'exploitation du serveur est ", PHP_OS, ".</p>";
	    ?>
        </section>
	<section>
            <h2>Question 3</h2> 
	    <?php
	    $n = 10;
	    $texte = "Bonjour";
	    echo "<p> \$n vaut $n et \$texte vaut $texte. </p>";
	    ?>
        </section>
	<section>
            <h2>Question 4</h2> 
	    <?php
	    	for ($i=0; $i<$n; $i++){
				echo "<p> $texte </p>";
		}
	    ?>
        </section>
	<section>
            <h2>Question 5</h2> 
	    <?php
		for ($j=strlen($texte); $j>0; $j--){
			echo "<p>".substr($texte, 0, $j). "</p>";
		}
	    ?>
        </section>
	<section>
            <h2>Question 6</h2> 
	    <?php
		echo "<ul>";
		for ($j=strlen($texte); $j>0; $j--){
			echo "<li>". substr($texte, 0, $j). "</li>";
		}
		echo "</ul>";
	    ?>
        </section>
	<section>
            <h2>Question 7</h2> 
	    <?php
		echo "<ul>\n";
		for ($k=2; $k<10; $k++){
			echo "<li> 2*$k=", 2*$k ,  "</li>";
		}
		echo "</ul>";
	    ?>
        </section>
	<section>
            <h2>Question 8</h2> 
	    <?php
		echo "<ul>\n";
		for ($l=2; $l<10; $l++){
			echo "<li>\n";
			echo "<ul>\n";
			for ($k=2; $k<10; $k++){
				echo "<li> $l*$k=".$l*$k. "</li>";
			}
			echo "</ul>\n";
			echo "</li>\n";
		}
		echo "</ul>";
	    ?>
        </section>
	<section>
            <h2>Question 9</h2> 
	    <?php
		echo "<table>";
		echo "<tr> <td> * </td> <td> 2 </td> <td> 3 </td> <td> 4 </td> <td> 5 </td> <td> 6 </td> <td> 7 </td> <td> 8 </td> <td> 9 </td> </tr>";
		for ($l=2; $l<10; $l++){
			echo "<tr> <td>". $l. "</td>";
			for ($k=2; $k<10; $k++){
				echo "<td> ". $l*$k . " </td>";
			}
			echo "</tr>";
		}
		echo "</table>";
	    ?>
        </section>
    </body>
    
</html>

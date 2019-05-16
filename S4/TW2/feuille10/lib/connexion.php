<?php
	try{ $connexion = new PDO(
	    "pgsql:host=localhost;dbname=texierl","texierl","jvdHuq1996");
	}catch (PDOException $e){
		echo("Erreur de connexion :" . $e->getMessage() );
		exit();
	}
	return;
?>

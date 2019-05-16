<?php
 require_once('lib/biblio.php');
 session_start();
 try {
   controleAuthentification();
 }
 catch(Exception $e)
 {
   require_once('lib/formuLogin.php');
   exit();
 }
 return;
?>

<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $author = $_GET['author'];
  $follower = $_GET['follower'];
  $mentioned = $_GET['mentioned'];
  $before = $_GET['before'];
  $after = $_GET['after'];
  $count = $_GET['count'];
  header("Content Type: application/json; charset=utf-8");
  if (isset($count)){
    echo json_encode(findMessages($author, $follower, $mentioned, $before, $after, $count));
  }
  else{
    echo json_encode(findMessages($author, $follower, $mentioned, $before, $after));
  }
?>

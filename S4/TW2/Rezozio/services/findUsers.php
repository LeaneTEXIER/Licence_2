<?php
  /* TEXIER Léane */
  require_once("../lib/biblio.php");
  $searched = $_GET['searched'];
  $scope = $_GET['scope'];
  $type = $_GET['type'];
  header("Content Type: application/json; charset=utf-8");
  if (isset($scope)){
    if (isset($type)){
      echo json_encode(findUsers($searched, $scope, $type));
    }
    else{
      echo json_encode(findUsers($searched, $scope));
    }
  }
  else{
    if (isset($type)){
      echo json_encode(findUsers($searched, 'both', $type));
    }
    else{
      echo json_encode(findUsers($searched));
    }
  }
 ?>

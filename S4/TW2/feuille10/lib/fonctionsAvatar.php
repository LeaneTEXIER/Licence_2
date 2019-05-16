<?php
function changeAvatar($login){
  $fileName = $_FILES['avatar']['tmp_name'];
  $type = $_FILES['avatar']['type'];
  $largeur = getimagesize($fileName)[0];
  $hauteur = getimagesize($fileName)[1];
  if ($largeur>70 || $hauteur>70){
    reduce($fileName, $largeur, $hauteur, $type);
    $type = 'image/png';
  }
  $flux = fopen($fileName, "r");
  $name = $_FILES['avatar']['name'];
  require_once('lib/connexion.php');
  $stnt = $connexion->prepare(
    "select *
     from images
     where login = :login"
  );
  $stnt->bindValue(':login', $login);
  $stnt->execute();
  $ligne = $stnt->fetch();
  if (!$ligne){
    $insertion = $connexion->prepare(
      "insert into images
      (nom,type,login, contenu) values (:nom, :type, :login, :contenu)"
    );
  }
  else{
    $insertion = $connexion->prepare(
      "update images
      set (nom, type, contenu) = (:nom, :type, :contenu)
      where login =:login"
    );
  }
  $insertion->bindValue(':nom',$name);
  $insertion->bindValue(':type',$type);
  $insertion->bindValue(':contenu', $flux, PDO::PARAM_LOB );
  $insertion->bindValue(':login', $login);
  $insertion->execute();
  fclose($flux);
}

function square($image, $largeur, $hauteur, $cote){
  $distance = min ($largeur, $hauteur);
  $x = ($largeur - $distance)/2;
  $y = ($hauteur - $distance)/2;
  $newImage = imagecreatetruecolor($cote, $cote);
  imagecopyresampled($newImage, $image,0,0,$x,$y,$cote,$cote,$distance,$distance);
  return $newImage;
}

function reduce($fileName, $largeur, $hauteur, $type){
  switch ($type) {
    case 'image/jpeg': $image = imagecreatefromjpeg($fileName);
      break;
    case 'image/png': $image = imagecreatefrompng($fileName);
      break;
    case 'image/gif': $image = imagecreatefromgif($fileName);
      break;
    case 'image/bmp': $image = imagecreatefromwbmp($fileName);
      break;
  }
  $square = square($image, $largeur, $hauteur, 70);
  imagepng($square, $fileName);
}


function afficheAvatar($login){
  require_once('lib/connexion.php');
  $stnt = $connexion->prepare(
    "select type, contenu
     from images
     where login =:login"
  );
  $stnt->bindValue(':login', $login);
  $stnt->execute();
  $ligne = $stnt->rowCount();
  if ($ligne !== 0){
    $stnt->bindColumn('type', $mimetype);
    $stnt->bindColumn('contenu',$flux,PDO::PARAM_LOB);
    $stnt->fetch(PDO::FETCH_BOUND);
    header("Content-Type: $mimetype");
    fpassthru($flux);
  }
}
 ?>

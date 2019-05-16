<?php
  /* TEXIER Léane */
  require_once ("../lib/connexion.php");
  require_once("Identite.class.php");
  $reponse = array('status', 'args', 'result');

  /*Donne toutes les infos d'une personne grace à son login */
  function infoPersonne($login){
    global $connexion;
    $requete = $connexion->prepare(
      "select *
      from rezoziopassword
      where ident='$login'"
    );
    $requete->execute();
    return $requete->fetch();
  }

  function authentifie($login, $password){
   $info = infoPersonne($login);
   if (!$info){
     return null;
   }
   if (crypt($password, $info['password'])!=$info['password']){
     return null;
   }
   return new Identite($info['ident'],$info['name'],$info['description']);
  }


  function controleAuthentification($login=null, $password=null){
    if (isset($_SESSION['ident'])){
      return false;
    }
    if ($login===null){
      $login = inputFilterString('login');
    }
    if ($password === null){
      $password = inputFilterString('password');
    }
    $ident = authentifie($login,$password);
    if (! $ident){
      $_SESSION['echec']=TRUE;
      throw new Exception('login/password incorrects');
    }
    $_SESSION['ident'] = $ident;
    unset($_SESSION['echec']);
    return true;
  }

  function inputFilterString($name, $requis=TRUE){
    $v = filter_input(INPUT_POST, $name, FILTER_SANITIZE_STRING);
    if ( $requis && $v == NULL )
      throw new Exception("argument $name est requis");
   return $v;
  }

  /* Regarde si l'argument donné est dans la table */
  function exist($param, $typeParam, $table){
    global $connexion;
    $requete = $connexion->prepare(
      "select *
      from $table
      where $typeParam = :param"
    );
    $requete->bindValue(':param',$param);
    $requete->execute();
    $requete->setFetchMode(PDO::FETCH_ASSOC);
    $ligne = $requete->fetch();
    return $ligne;
  }


  function getUser($user, $type="short"){
    $reponse = array('status', 'args', 'result');
    global $connexion;
    if (is_null($user) || !exist($user, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
      $reponse['result'] = null;
    }
    else{
      if ($type == 'long'){
        $requete = $connexion->prepare(
          "select ident, name, description
          from rezoziopassword
          where ident = '$user'"
        );
      }
      else{
        $requete = $connexion->prepare(
          "select ident, name
          from rezoziopassword
          where ident = '$user'"
        );
      }
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $reponse['status'] = "ok";
      $reponse['args']['user'] = $user;
      $reponse['args']['type'] = $type;
      $reponse['result']['User'] = $ligne;
    }
    return $reponse;
  }


  function getMessage($id){
    global $connexion;
    if (is_null($id) || !exist($id, 'id', 'rezoziomessages')){
      $reponse['status'] = "error";
      $reponse['result'] = null;
    }
    else{
      $requete = $connexion->prepare(
        "select *
        from rezoziomessages
        where id = '$id'"
      );
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $reponse['status'] = "ok";
      $reponse['args']['id'] = $id;
      $reponse['result']['Message'] = $ligne;
    }
    return $reponse;
  }


  function getAvatar($user, $size="small"){
    global $connexion;
    if (is_null($user) || !exist($user, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
      $reponse['result'] = null;
      header("Content Type: application/json; charset=utf-8");
      echo json_encode($reponse);
      return;
    }
    $requete = $connexion->prepare(
      "select contenu
       from rezozioimages$size
       where  ident = '$user'"
     );
     $requete->execute();
     $requete->bindColumn('contenu',$flux,PDO::PARAM_LOB);
     $requete->fetch();
     header("Content-Type: image/png");
     fpassthru($flux);
   }


  function findUsers($searched, $scope="both", $type="short"){
    global $connexion;
    if (is_null($searched)){
      $reponse['status'] = "error";
      $reponse['result'] = null;
    }
    else{
      if ($scope=='ident' || $scope=='name'){
        if ($type == 'long'){
          $requete = $connexion -> prepare(
            "select ident, name, description
            from rezoziopassword
            where $scope like :searched"
          );
          $chercher = "%$searched%";
          $requete->bindValue(':searched',$chercher);
        }
        else{
          $requete = $connexion -> prepare(
            "select ident,name
            from rezoziopassword
            where $scope like :searched"
          );
          $chercher = "%$searched%";
          $requete->bindValue(':searched',$chercher);
        }
      }
      else{
        if ($type == 'long'){
          $requete = $connexion -> prepare(
            "select ident, name, description
            from rezoziopassword
            where ident like :searched or name like :searched"
          );
          $chercher = "%$searched%";
          $requete->bindValue(':searched',$chercher);
        }
        else{
          $requete = $connexion -> prepare(
            "select ident,name
            from rezoziopassword
            where ident like :searched or name like :searched"
          );
          $chercher = "%$searched%";
          $requete->bindValue(':searched',$chercher);
        }
      }
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $users = array();
      while($ligne){
        array_push($users, $ligne);
        $ligne = $requete->fetch();
      }
      $reponse['status'] = "ok";
      $reponse['args']['searched'] = $searched;
      $reponse['args']['scope'] = $scope;
      $reponse['args']['type'] = $type;
      $reponse['result']['list'] = $users;
    }
    return $reponse;
  }


  function findMessages($author, $follower, $mentioned, $before, $after, $count = 15){
    global $connexion;
    if ((!is_null($author) && !exist($author, 'ident', 'rezoziopassword')) ||
        (!is_null($follower) && !exist($follower, 'ident', 'rezoziopassword')) ||
        (!is_null($mentioned) && !exist($mentioned, 'ident', 'rezoziopassword')) ||
        (!is_null($before) && !is_numeric($before)) ||
        (!is_null($after) && !is_numeric($after)) ||
        (!is_null($count) && !is_numeric($count) && $count<=0)){
      $reponse['status'] = "error";
      $reponse['result'] = null;
    }
    else{
      $reponse['status'] = "ok";
      $where = "";
      $from = "rezoziomessages";
      if (!is_null($author)){
        $reponse['args']['author'] = $author;
        $where .= "rezoziomessages.author = '$author'";
      }
      if (!is_null($follower)){
        $reponse['args']['follower'] = $follower;
        $from .=", rezoziofollower";
        if ($where!=""){
          $where .=" and ";
        }
        $where .="rezoziomessages.author = rezoziofollower.membre_suivi and rezoziofollower.follower = '$follower'";
      }
      if (!is_null($mentioned)){
        $reponse['args']['mentioned'] = $mentioned;
        $from .=", rezoziocitations";
        if ($where!=""){
          $where .=" and ";
        }
        $where .="rezoziocitations.num_message = rezoziomessages.id and rezoziocitations.pseudo = '$mentioned'";
      }
      if (!is_null($before)){
        $reponse['args']['before'] = $before;
        if ($where!=""){
          $where .=" and ";
        }
        $where .="rezoziomessages.id < $before";
      }
      if (!is_null($after)){
        $reponse['args']['after'] = $after;
        if ($where!=""){
          $where .=" and ";
        }
        $where .="rezoziomessages.id > $after";
      }
      if ($where!=""){
        $requete = $connexion -> prepare(
          "select rezoziomessages.id, rezoziomessages.author, rezoziomessages.content, rezoziomessages.datetime
          from $from
          where $where
          order by rezoziomessages.id desc"
        );
      }
      else{
        $requete = $connexion -> prepare(
          "select rezoziomessages.id, rezoziomessages.author, rezoziomessages.content, rezoziomessages.datetime
          from $from
          order by rezoziomessages.id desc"
        );
      }
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $messages = array();
      $i = 0;
      $reponse['args']['count'] = $count;
      while($ligne && $i++<$count){
        array_push($messages, $ligne);
        $ligne = $requete->fetch();
      }
      $reponse['result']['list'] = $messages;
      if ($ligne){
        $reponse['result']['hasMore'] = true;
      }
      else{
        $reponse['result']['hasMore'] = false;
      }
    }
    return $reponse;
  }


  function getAllUsers(){
    global $connexion;
    $requete = $connexion -> prepare(
      "select ident
      from rezoziopassword"
    );
    $requete->execute();
    $requete->setFetchMode(PDO::FETCH_ASSOC);
    $ligne = $requete->fetch();
    $users = array();
    while($ligne){
      array_push($users, $ligne['ident']);
      $ligne = $requete->fetch();
    }
    return $users;
  }


  function postMessage($source, $login){
    global $connexion;
    if (is_null($source)){
      $reponse['status'] = "error";
      $reponse['result'] = null;
    }
    else{
      require_once("../lib/MessageMentions.class.php");
      $message = new MessageMentions($source);
      $userList = getAllUsers();
      $message->setMentions($userList);
      $messageForBase = $message->getEncodedMessage();
      $dateHour = (new DateTime())->format('Y-m-d H:i:s');
      //Met le message dans la base
      $requete = $connexion -> prepare(
        "insert into rezoziomessages
        (author, content, datetime) values ('$login', :content, '$dateHour')"
      );
      $requete->bindValue(':content',$messageForBase);
      $requete->execute();
      //Récupère l'id correspondant au message
      $requete = $connexion -> prepare(
        "select id
        from rezoziomessages
        where content = :content and datetime='$dateHour'"
      );
      $requete->bindValue(':content',$messageForBase);
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $id = $ligne['id'];
      //Met les citations du messages dans le tableau des citations
      $identCit = $message->getFoundIdents();
      for($i=0; $i<count($identCit); $i++){
        $identC = $identCit[$i];
        $requete = $connexion -> prepare(
          "insert into rezoziocitations
          (pseudo, num_message) values ('$identC', $id)"
        );
        $requete->execute();
      }
      $reponse['status'] = "ok";
      $reponse['args']['source'] = $source;
      $reponse['result'] = $ligne;
    }
    return $reponse;
  }


  function randomSalt(){
    $salt = '$2a$10$';
    $caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    for ($i=0; $i<22; $i++){
      $salt .= $caracteres[rand()%strlen($caracteres)];
    }
    return $salt;
  }


  function createUser($ident, $password, $name){
    global $connexion;
    if (is_null($ident) || is_null($password) || is_null($name) || exist($ident, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
      $reponse['result'] = null;
    }
    else{
      $passwordHache = crypt($password,randomSalt());
      $requete = $connexion->prepare(
        "insert into rezoziopassword
        (ident, password, name, description) values('$ident', '$passwordHache', '$name', '')"
      );
      $requete->execute();
      //Insertion de l'image par défaut en petite taille
      $requete = $connexion->prepare(
        "insert into rezozioimagessmall
        (ident, contenu) values('$ident', 'EnCours')"
      );
      $requete->execute();
      $requete = $connexion->prepare(
        " update rezozioimagessmall
        set contenu = imagesdefautrezozio.contenu
        from imagesdefautrezozio
        where ident='$ident' and size='small'
        "
      );
      $requete->execute();
      //Insertion de l'image par défaut en grande taille
      $requete = $connexion->prepare(
        "insert into rezozioimageslarge
        (ident, contenu) values('$ident', 'EnCours')"
      );
      $requete->execute();
      $requete = $connexion->prepare(
        " update rezozioimageslarge
        set contenu = imagesdefautrezozio.contenu
        from imagesdefautrezozio
        where ident='$ident' and size='large'
        "
      );
      $requete->execute();
      //Arguments
      $reponse['status'] = "ok";
      $reponse['args']['ident'] = $ident;
      $reponse['args']['name'] = $name;
      $reponse['result']['User']['ident'] = $ident;
      $reponse['result']['User']['name'] = $name;
    }
    return $reponse;
  }


  function setProfile($login, $name, $password, $description){
    global $connexion;
    $reponse['status'] = "ok";
    $set = "";
    if (!is_null($name) && $name!==""){
      $reponse['args']['name'] = $name;
      $set .= "name = :name";
    }
    if (!is_null($password) && $password!==""){
      if ($set!=""){
        $set .=", ";
      }
      $passwordHache = crypt($password,randomSalt());
      $set .= "password = '$passwordHache'";
    }
    if (!is_null($description) && $description!==""){
      $reponse['args']['description'] = $description;
      if ($set!=""){
        $set .=", ";
      }
      $set .= "description = :description";
    }
    if ($set!=""){
      $requete = $connexion->prepare(
        "update rezoziopassword
         set $set
         where ident='$login'"
      );
      if (!is_null($description) && $description!==""){
        $requete->bindValue(':description',$description);
      }
      if (!is_null($name) && $name!==""){
        $requete->bindValue(':name',$name);
      }
      $requete->execute();
    }
    $requete = $connexion->prepare(
      "select ident, name, description
      from rezoziopassword
       where ident='$login'"
    );
    $requete->execute();
    $requete->setFetchMode(PDO::FETCH_ASSOC);
    $ligne = $requete->fetch();
    $reponse['result']['User'] = $ligne;
    return $reponse;
  }


  function login($login, $password){
    global $connexion;
    try{
      $controle = controleAuthentification($login, $password);
    }catch(Exception $e){
      $reponse['status'] = "error";
    }
    if ($controle){
      $reponse['status'] = "ok";
      $requete = $connexion->prepare(
        "select ident
        from rezoziopassword
         where ident='$login'"
      );
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $reponse['result'] = $ligne;
    }
    $reponse['args']['login'] = $login;
    return $reponse;
  }


  function logout($login){
    global $connexion;
    $reponse['status'] = "ok";
    $requete = $connexion->prepare(
      "select ident
      from rezoziopassword
       where ident='$login'"
    );
    $requete->execute();
    $requete->setFetchMode(PDO::FETCH_ASSOC);
    $ligne = $requete->fetch();
    $reponse['result'] = $ligne;
    return $reponse;
  }


  function uploadAvatar($login){
    global $connexion;
    $fileName = $_FILES['avatar']['tmp_name'];
    $type = $_FILES['avatar']['type'];
    //si fichier vide
    if ($_FILES['avatar']['error']===UPLOAD_ERR_NO_FILE){
      $reponse['status'] = "error";
      $reponse['result'] = "vide";
    }
    //si taille dépassée
    else if ($_FILES['avatar']['error']==UPLOAD_ERR_INI_SIZE){
      $reponse['status'] = "error";
      $reponse['result'] = "taille";
    }
    //formats acceptés
    else if (($type!='image/jpeg') && ($type!='image/png') && ($type!='image/gif') && ($type!='image/bmp')){
      $reponse['status'] = "error";
      $reponse['result'] = "format";
    }
    else{
      $reponse['status'] = "ok";
      $reponse['args'] = $_FILES['avatar'];
      unset($reponse['args']['tmp_name']);
      $largeur = getimagesize($fileName)[0];
      $hauteur = getimagesize($fileName)[1];
      goodSize($fileName, $largeur, $hauteur, $type, 256);
      $type = 'image/png';
      $flux = fopen($fileName, "r");
      $insertion = $connexion->prepare(
        "update rezozioimageslarge
        set (contenu) = (:contenu)
        where ident ='$login'"
        );
      $insertion->bindValue(':contenu', $flux, PDO::PARAM_LOB );
      $insertion->execute();
      fclose($flux);
      goodSize($fileName, 256, 256, $type, 48);
      $flux = fopen($fileName, "r");
      $insertion = $connexion->prepare(
        "update rezozioimagessmall
        set (contenu) = (:contenu)
        where ident ='$login'"
        );
      $insertion->bindValue(':contenu', $flux, PDO::PARAM_LOB );
      $insertion->execute();
      $flux = fopen($fileName, "r");
      $reponse['result'] = true;
    }
    return $reponse;
  }

  /* Met l'image en carré et à la taille $cote demandé */
  function square($image, $largeur, $hauteur, $cote){
    $distance = min ($largeur, $hauteur);
    $x = ($largeur - $distance)/2;
    $y = ($hauteur - $distance)/2;
    $newImage = imagecreatetruecolor($cote, $cote);
    imagecopyresampled($newImage, $image,0,0,$x,$y,$cote,$cote,$distance,$distance);
    return $newImage;
  }

  /* Permet de mettre l'image en carré et à la taille souhaitée (format png)*/
  function goodSize($fileName, $largeur, $hauteur, $type, $cote){
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
    $square = square($image, $largeur, $hauteur, $cote);
    imagepng($square, $fileName);
  }

  function isLogged(){
    $reponse['status'] = "ok";
    if (isset($_SESSION['ident'])){
      $ident = $_SESSION['ident'];
      $login = $ident->getLogin();
      $reponse['result'] = $login;
    }
    else{
      $reponse['result'] = "";
    }
    return $reponse;
  }

  /* Donne tous les abonnements d'une personne */
  function abonnements($login){
    global $connexion;
    if (!exist($login, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
    }
    else{
      $reponse['status'] = "ok";
      $requete = $connexion -> prepare(
        "select membre_suivi
        from rezoziofollower
        where follower='$login'"
      );
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $users = array();
      while($ligne){
        array_push($users, $ligne['membre_suivi']);
        $ligne = $requete->fetch();
      }
      $reponse['args']['login'] = $login;
      $reponse['result'] = $users;
    }
    return $reponse;
  }

  /* Donne tous les abonnés d'une personne */
  function abonnes($login){
    global $connexion;
    if (!exist($login, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
    }
    else{
      $reponse['status'] = "ok";
      $requete = $connexion -> prepare(
        "select follower
        from rezoziofollower
        where membre_suivi='$login'"
      );
      $requete->execute();
      $requete->setFetchMode(PDO::FETCH_ASSOC);
      $ligne = $requete->fetch();
      $users = array();
      while($ligne){
        array_push($users, $ligne['follower']);
        $ligne = $requete->fetch();
      }
      $reponse['args']['login'] = $login;
      $reponse['result'] = $users;
    }
    return $reponse;
  }

  /* Indique si une personne est abonné à l'autre */
  function aboOuNon($follower, $membre_suivi){
    if (!exist($follower, 'ident', 'rezoziopassword') || !exist($membre_suivi, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
    }
    else{
      $rep = abonnements($follower)['result'];
      $i = 0;
      $test = false;
      while ($rep[$i]!==null && !$test){
        if ($rep[$i]==$membre_suivi){
          $test = true;
        }
        else{
          $i++;
        }
      }
      $reponse['status']="ok";
      $reponse['args']['follower'] = $follower;
      $reponse['args']['membre_suivi'] = $membre_suivi;
      $reponse['result']['Abo'] = $test;
    }
    return $reponse;
  }

  /* Permet de s'abonner ou se désabonner d'une personne suivant le cas */
  function AboDesabo($follower, $membre_suivi){
    global $connexion;
    if (!exist($follower, 'ident', 'rezoziopassword') || !exist($membre_suivi, 'ident', 'rezoziopassword')){
      $reponse['status'] = "error";
    }
    else{
      $rep = aboOuNon($follower, $membre_suivi)['result']['Abo'];
      if ($rep){
        $requete = $connexion -> prepare(
          "delete from rezoziofollower
          where follower = '$follower' and membre_suivi = '$membre_suivi'"
        );
        $reponse['result'] = 'Desabonnement';
      }
      else{
        $requete = $connexion -> prepare(
          "insert into rezoziofollower
          (follower, membre_suivi) values ('$follower', '$membre_suivi')"
        );
        $reponse['result'] = 'Abonnement';
      }
      $requete->execute();
      $reponse['status']="ok";
      $reponse['args']['follower'] = $follower;
      $reponse['args']['membre_suivi'] = $membre_suivi;
    }
    return $reponse;
  }
?>

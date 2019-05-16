<?php
/*Léane Texier */
class Identite{
  private $login;
  private $nom;
  private $prenom;

  public function getLogin(){
    return $this->login;
  }

  public function getNom(){
    return $this->nom;
  }

  public function getPrenom(){
    return $this->prenom;
  }

  public function __construct($login, $nom, $prenom){
    $this->login = $login;
    $this->nom = $nom;
    $this->prenom = $prenom;
  }
}
 ?>

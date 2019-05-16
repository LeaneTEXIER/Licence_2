<?php
  /* TEXIER Léane */
  class Identite {
    private $login;
    private $nom;
    private $description;
    public function __construct($login,$nom,$description)
    {
      $this->login = $login;
      $this->nom = $nom;
      $this->description = $description;
    }
    public function getLogin(){
      return $this->login;
    }
    public function getNom(){
      return $this->nom;
    }
    public function getDescription(){
      return $this->description;
    }
  }
?>

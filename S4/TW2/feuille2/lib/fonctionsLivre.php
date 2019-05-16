<?php
/*Léane Texier*/
  function propertyName($line){
    $pos = strpos($line, ":");
    if ($pos!==false){
      return trim(substr($line, 0, $pos));
    }
    else{
      throw new Exception("Pas de caractère ':' dans la chaîne");
    }
  }

  function propertyValue($line){
    $pos = strpos($line, ":");
    if ($pos!==false){
      return trim(substr($line, $pos+1));
    }
    else{
      throw new Exception("Pas de caractère ':' dans la chaîne");
    }
  }

  function readBook($file){
    $result=array();
    $line=fgets($file);
    while ($line!==FALSE && trim($line=="")){
      $line=fgets($file);
    }
    if ($line===FALSE){
      return "FALSE";
    }
    else{
      while ($line!==FALSE && trim($line)!=""){
        $result[propertyName($line)]=propertyValue($line);
        $line=fgets($file);
      }
    return $result;
    }
  }

  function elementBuilder($propName, $elementType, $text){
    return ("<$elementType class=\"$propName\">$text</$elementType>");
  }

  function authorsToHTML($authors){
    $couper = explode(" - ", $authors);
    $return = "<span>".implode("</span> <span>", $couper)."</span>";
    return $return;
  }

  function coverToHTML($fileName){
    return ("<img src=\"couvertures/$fileName\" alt=\"image de couverture\" />");
  }

  function propertyToHTML($propName,$propValue){
    if ($propName === 'titre'){
      return elementBuilder($propName, 'h2', $propValue);
    }
    else if ($propName === 'couverture'){
      return elementBuilder($propName, 'div', coverToHTML($propValue));
    }
    else if ($propName === 'auteurs'){
      return elementBuilder($propName, 'div', authorsToHTML($propValue));
    }
    else if ($propName === 'année'){
      return elementBuilder($propName, 'time', $propValue);
    }
    else{
      return elementBuilder($propName, 'div', $propValue);
    }
  }

  function bookToHTML($book){
    $description = '<div class="description">'."\n";
    foreach ($book as $propName=>$propValue){
      if ($propName != 'couverture'){
        $description.=propertyToHTML($propName,$propValue)."\n";
      }
    }
    $description.='</div>'."\n";
    $cover= propertyToHTML('couverture', $book['couverture']);
    return "<article class=\"livre\">\n$cover\n$description</article>";
  }

  function libraryToHTML($file){
    $book=readBook($file);
    $return="";
    while ($book!=='FALSE'){
      $return.= bookToHTML($book);
      $book=readBook($file);
    }
    return $return;
  }
?>

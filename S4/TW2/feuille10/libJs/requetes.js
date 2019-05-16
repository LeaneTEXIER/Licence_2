window.addEventListener("load", variable);
var intervalId;

function new_xhr(){
   var xhrObject = null;
   if(window.XMLHttpRequest)
     xhrObject = new XMLHttpRequest();
   else if(window.ActiveXObject) {
     try{
        xhrObject = new ActiveXObject("Msxml2.XMLHTTP");
     }catch (e){
        xhrObject = new ActiveXObject("Microsoft.XMLHTTP");
     }
   }
   else {
      alert("Votre navigateur ne supporte pas les objets XMLHTTPRequest...");
       xhrObject = false;
   }
   return xhrObject;
}

function requete_users(){
   var xhrObject = new_xhr();
   var a = document.getElementById("interest").value;
   xhrObject.open('get','find_user.php?interest='+a, true);
   xhrObject.onreadystatechange = traiteReponse;
   xhrObject.send(null);
 }

function traiteReponse(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var table = "<h3>Utilisateurs aimants ce centre d'intérêts: </h3><table><thead><th>Login</th><th>Nom</th><th>Prénom</th></thead><tbody>";
      for(var i =0;i<myobject.length;i++){
        table += "<tr><td>"+myobject[i]['login']+"</td><td>"+myobject[i]['nom']+"</td><td>"+myobject[i]['prenom']+"</td></tr>";
      }
      table += "</tbody></table>"
      document.getElementById('resultsInterest').innerHTML = table;
    }
    else{
      document.getElementById('resultsInterest').innerHTML ="Chargement en cours...";
    }
  }
}

function requete_vivants(){
   var xhrObject = new_xhr();
   xhrObject.open('get','je_suis_vivant.php', true);
   xhrObject.onreadystatechange = traiteReponseVivant;
   xhrObject.send(null);
 }

 function traiteReponseVivant(){
   if(this.readyState==4){
     if(this.status  == 200){
       var myobject = JSON.parse(this.responseText);
       var table = "<h3>Utilisateurs connectés: </h3><ul>";
       for(var i =0;i<myobject.length;i++){
         table += "<li>"+myobject[i]['login']+"</li>";
       }
       table += "</ul>"
       document.getElementById('usersConnect').innerHTML = table;
     }
     else{
       document.getElementById('usersConnect').innerHTML ="Chargement en cours...";
     }
   }
 }

function variable(){
  requete_vivants();
  intervalId = setInterval(requete_vivants, 10000);
}

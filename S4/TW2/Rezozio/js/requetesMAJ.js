/* TEXIER Léane */

window.addEventListener("load", chargement);

function chargement(){
  var formulaireMAJ = document.forms["maj"];
  formulaireMAJ.addEventListener("submit", requete_MAJInformations);
  var formAvatar = document.forms["avatarMAJ"];
  formAvatar.addEventListener("submit",requete_MAJAvatar);
}

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


function requete_MAJInformations(ev){
  ev.preventDefault();
  var form = this;
  var url = new URL(form.action);
  var data = new FormData(this);
  var xhrObject = new_xhr();
  xhrObject.open('post', url, true);
  xhrObject.addEventListener("load", traiteReponseMAJInformations.bind(xhrObject, form));
  xhrObject.send(data);
  disableForm(form, true);
  document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
}

function traiteReponseMAJInformations(ev){
  if(this.readyState==4){
    if(this.status  == 200){
      var args = JSON.parse(this.responseText)['args'];
      for (var arg in args){
        document.getElementById(arg).value = "";
      }
      document.getElementById("password").value = "";
      document.getElementById("MessageInformation").innerHTML = "<p id=\"Ok\">Informations mises à jour</p>";
    }
    else{
      document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
    }
  }
  disableForm(form, false);
}

function requete_MAJAvatar(ev){
  ev.preventDefault();
  var form = this;
  var url = new URL(form.action);
  var data = new FormData(this);
  var xhrObject = new_xhr();
  xhrObject.open('post', url, true);
  xhrObject.addEventListener("load", traiteReponseMAJAvatar.bind(xhrObject, form));
  xhrObject.send(data);
  disableForm(form, true);
  document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
}


function traiteReponseMAJAvatar(form, ev){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      document.getElementById("avatar").value = "";
      if (myobject['status'] == "ok"){
        document.getElementById("MessageInformation").innerHTML = "<p id=\"Ok\">Avatar mis à jour</p>";
      }
      else{
        if (myobject['result'] == "format"){
          document.getElementById("MessageInformation").innerHTML = "<p id=\"Erreur\">Format non accepté pour l'avatar. Les formats acceptés sont: .jpeg, .jpg, .png, .gif, .bmp</p>";
        }
        else if (myobject['result'] == "taille"){
          document.getElementById("MessageInformation").innerHTML = "<p id=\"Erreur\">Fichier trop gros. Taille maximale: 2 Mo.</p>";
        }
        else{ //if myobject['result'] == "vide"
          document.getElementById("MessageInformation").innerHTML = "<p id=\"Erreur\">Aucun fichier envoyé.</p>";
        }
      }
    }
    else{
      document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
    }
  }
  disableForm(form, false);
}

// Permet l'activation ou la désactivation d'un formualaire form suivant le cas
function disableForm(form, setDisable){
   for (var field of form)
     field.disabled = setDisable;
}

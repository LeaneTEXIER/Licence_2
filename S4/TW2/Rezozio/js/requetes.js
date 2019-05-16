/* TEXIER Léane */

window.addEventListener("load", requete_connexion)

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

function requete_connexion() {
  var xhrObject = new_xhr();
  xhrObject.open('get','services/isLogged.php', true);
  xhrObject.onreadystatechange = traiteReponseConnexion;
  xhrObject.send(null);
}

function traiteReponseConnexion(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      document.getElementById("ListeMessagesAcc").innerHTML = "";
      if (myobject['result'] == ""){
        requete_FindMessages();
        formulaireConnexion();
        var formCo = document.forms["form_Connexion"];
        formCo.addEventListener("submit", requete_FormulaireConnexion);
        formulaireInscription();
        var formInscr = document.forms["form_Inscription"];
        formInscr.addEventListener("submit", requete_FormulaireInscription);
        document.getElementById("MonCompte").innerHTML ="";
        document.getElementById("postMessage").innerHTML = "";
      }
      else{
        var follower = myobject['result'].toString();
        requete_FindMessages(null, follower);
        document.getElementById("Connexion").innerHTML = "<button onclick=\"requete_deconnexion()\">Déconnexion</button>";
        document.getElementById("Inscription").innerHTML = "";
        document.getElementById("MessageInformation").innerHTML ="";
        document.getElementById("MonCompte").innerHTML ="<a href=\"pageMembre.php?login="+follower+"\">Mon Compte</a>";
        formulairePostMessage();
        var formPostMes = document.forms["form_postMessage"];
        formPostMes.addEventListener("submit", requete_FormulairePostMessage);
      }
    }
  }
}

function requete_FindUsers(){
   var xhrObject = new_xhr();
   var a = document.getElementById("recherche_user").value;
   xhrObject.open('get','services/findUsers.php?type=short&searched='+a, true);
   xhrObject.onreadystatechange = traiteReponseFindUsers;
   xhrObject.send(null);
 }

function traiteReponseFindUsers(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var liste = "<h3>Résultats de la recherche: </h3><ul>";
      for(var i in myobject['result']['list']){
        liste += "<li onclick=\"requete_FindMessages('"+myobject['result']['list'][i]['ident']+"',null, null, null, 1)\">"+myobject['result']['list'][i]['name']+" alias "+myobject['result']['list'][i]['ident']+"</li>";
      }
      liste += "</ul>"
      document.getElementById("reponsesRecherche").innerHTML = liste;
    }
    else{
      document.getElementById("reponsesRecherche").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_NameCitation(name, num, j){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/getUser.php?user='+name, true);
  xhrObject.addEventListener("load", traiteReponseNameCitation.bind(xhrObject, num, j));
  xhrObject.send(null);
}

function traiteReponseNameCitation(num, j){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      if (myobject['status']==="error"){
        alert('erreur');
      }
      else{
        var name = myobject['result']['User']['name'];
        var login = myobject['result']['User']['ident'];
        document.getElementById("NameCita"+num+"&"+j).innerHTML = "<img src=\"services/getAvatar.php?user="+login+"\" alt='Photo de profil'><img>"+name;
      }
    }
  }
}

function traiteMessage(message, num){
  var mot_base, mot_remp, login, j;
  //Mots citations en début de message
  var j = 0;
  var citations = message.match(/^@[a-zA-Z0-9_]+/);
  if (citations!=null){
    mot_base = citations[0];
    login = citations[0].split('@')[1];
    mot_remp = "<a href=\"pageMembre.php?login="+login+"\">"+login+"<span id=\"NameCita"+num+"&"+j+"\"></span></a>";
    message = message.replace(mot_base, mot_remp);
    requete_NameCitation(login, num, j);
    j++;
  }
  //Mots citations PAS en début de message
  citations = message.match(/[^\\]@[a-zA-Z0-9_]+/g);
  if (citations!==null){
    for (var i = 0; i<citations.length; i++){
      login = citations[i].split('@')[1];
      mot_base = '@'+login;
      mot_remp = "<a href=\"pageMembre.php?login="+login+"\">"+login+"<span id=\"NameCita"+num+"&"+j+"\"></span></a>";
      message = message.replace(mot_base, mot_remp);
      requete_NameCitation(login, num, j);
      j++;
    }
  }
  message = message.replace(/\\\\/g, '\\');
  message = message.replace(/\\@/g, '@');
  return message;
}


function requete_NameAuthor(author, i){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/getUser.php?user='+author, true);
  xhrObject.addEventListener("load", traiteReponseNameAuthor.bind(xhrObject, i));
  xhrObject.send(null);
}

function traiteReponseNameAuthor(i){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      if (myobject['status']==="error"){
        alert('erreur');
      }
      else{
        document.getElementById("NameAndLogin"+i).innerHTML = myobject['result']['User']['name'] + " alias " + myobject['result']['User']['ident'];
      }
    }
  }
}


function requete_FindMessages(author=null, follower=null, mentioned=null, before=null, nouveau=0){
  if (nouveau!==0){
    document.getElementById("ListeMessagesAcc").innerHTML = "";
  }
   var xhrObject = new_xhr();
   var param ="?";
   if (author!==null){
     param += "author="+author+"&";
   }
   if (follower!==null){
     param += "follower="+follower+"&";
   }
   if (mentioned!==null){
     param += "mentioned="+mentioned+"&";
   }
   if (before!==null){
     param += "before="+before+"&";
   }
   xhrObject.open('get','services/findMessages.php'+param, true);
   xhrObject.onreadystatechange = traiteReponseFindMessages;
   xhrObject.send(null);
 }

function traiteReponseFindMessages(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      if (document.getElementById("ListeMessagesAcc").innerHTML===""){
        document.getElementById("ListeMessagesAcc").innerHTML = "<h3>Derniers messages: </h3>";
      }
      var message, j,  authorMessage, date;
      for(var i in myobject['result']['list']){
        j = myobject['result']['list'][i]['id'];
        message = "";
        message += "<div id=\"MessageIndividuel\">";
        authorMessage = myobject['result']['list'][i]['author'];
        message += "<div id=\"authorMessages\"><img src='services/getAvatar.php?user="+authorMessage+"' alt='Photo de profil'/><a id=\"NameAndLogin"+j+"\" href=\"pageMembre.php?login="+authorMessage+"\"></a></div>";
        message += "<div id=\"ContentMessage\">"+traiteMessage(myobject['result']['list'][i]['content'], j)+"</div>";
        date = myobject['result']['list'][i]['datetime'];
        message += "<div id=\"HeureMessage\"><time datetime=\""+date+"\">"+date+"</time></div>";
        message +=  "</div>";
        document.getElementById("ListeMessagesAcc").innerHTML += message;
        requete_NameAuthor(authorMessage, j);
      }
      if (myobject['result']['hasMore']===true){
        if (typeof myobject['args']['author']!=='undefined'){
          var author = "'"+myobject['args']['author']+"'";
        }
        if (typeof myobject['args']['follower']!=='undefined'){
          var follower = "'"+myobject['args']['follower']+"'";
        }
        if (typeof myobject['args']['mentioned']!=='undefined'){
          var mentioned = "'"+myobject['args']['mentioned']+"'";
        }
        var before = myobject['result']['list'][i]['id'];
        document.getElementById("ButtonMessages").innerHTML = "<button type=\"button\" onclick=\"requete_FindMessages("+author+","+follower+","+mentioned+","+before+")\">Afficher plus de messages</button>";
      }
      else{
        document.getElementById("ButtonMessages").innerHTML = "";
      }
    }
    else{
      document.getElementById("ListeMessagesAcc").innerHTML ="Chargement en cours...";
    }
  }
}



function formulaireConnexion(){
  var form = "<form name=\"form_Connexion\" method=\"post\" id=\"form_Connexion\" action=\"services/login.php\">"
  form += "<fieldset>";
  form += "<legend>Connexion :</legend>";
  form += "<label for=\"login\">Login :</label>";
  form += "<input type=\"text\" name=\"login\" id=\"login\" required=\"required\" /><br/>";
  form += "<label for=\"password\">Mot de passe :</label>";
  form += "<input type=\"password\" name=\"password\" id=\"password\" required=\"required\" /><br/>";
  form += "<button name=\"valid\" value=\"ok\" type=\"submit\">Valider</button>";
  form += "</fieldset>";
  form += "</form>";
  document.getElementById("Connexion").innerHTML = form;
}


function requete_FormulaireConnexion(ev){
  ev.preventDefault();
  var form = this;
  var url = new URL(form.action);
  var data = new FormData(this);
  var xhrObject = new_xhr();
  xhrObject.open('post', url, true);
  xhrObject.addEventListener("load", traiteReponseFormulaireConnexion.bind(xhrObject, form));
  xhrObject.send(data);
  disableForm(form, true);
  document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
 }

function traiteReponseFormulaireConnexion(form, ev){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      if (myobject['status'] == "ok"){
        requete_connexion();
      }
      else{
        document.getElementById("MessageInformation").innerHTML = "<p id=\"Erreur\">Login / Mot de passe incorrects</p>"
      }
    }
    else{
      document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
    }
  }
  disableForm(form, false);
}


function formulaireInscription(){
  var form = "<form name=\"form_Inscription\" method=\"POST\" id=\"form_Inscription\" action=\"services/createUser.php\">"
  form += "<fieldset>";
  form += "<legend>Inscription :</legend>";
  form += "<label for=\"ident\">Login :</label>";
  form += "<input type=\"text\" name=\"ident\" id=\"ident\" required=\"required\" pattern=\"[a-zA-Z0-9_]+\"/><br/>";
  form += "<label for=\"password\">Mot de passe :</label>";
  form += "<input type=\"password\" name=\"password\" id=\"password\" required=\"required\" /><br/>";
  form += "<label for=\"name\">Nom :</label>";
  form += "<input type=\"text\" name=\"name\" id=\"name\" required=\"required\" maxlength=\"25\"/><br/>";
  form += "<button name=\"valid\" value=\"ok\" type=\"submit\">Valider</button>";
  form += "</fieldset>";
  form += "</form>";
  document.getElementById("Inscription").innerHTML = form;
}

function requete_FormulaireInscription(ev){
  ev.preventDefault();
  var form = this;
  var url = new URL(form.action);
  var data = new FormData(this);
  var xhrObject = new_xhr();
  xhrObject.open('post', url, true);
  xhrObject.addEventListener("load", traiteReponseFormulaireInscrption.bind(xhrObject, form));
  xhrObject.send(data);
  disableForm(form, true);
  document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
 }

function traiteReponseFormulaireInscrption(form, ev){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      if (myobject['status'] === "error"){
        document.getElementById("MessageInformation").innerHTML = "<p id=\"Erreur\">Login déjà utilisé: Veillez choisir un autre login.</p>";
      }
      else{
        document.getElementById("MessageInformation").innerHTML = "<p id=\"Ok\">Compte créé avec succès. Vous pouvez maintenant vous connecter.</p>";
      }
      requete_connexion();
    }
    else{
      document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
    }
  }
  disableForm(form, false);
}

function formulairePostMessage(){
  var form = "<form name=\"form_postMessage\" method=\"POST\" id=\"form_postMessage\" action=\"services/postMessage.php\">"
  form += "<fieldset>";
  form += "<label for=\"source\">Ecrire un message :</label>";
  form += "<textarea type=\"text\" name=\"source\" id=\"source\" rows=\"4\" cols=\"26\"></textarea>";
  form += "<button name=\"valid\" value=\"ok\" type=\"submit\">Valider</button>";
  form += "</fieldset>";
  form += "</form>";
  document.getElementById("postMessage").innerHTML = form;
}

function requete_FormulairePostMessage(ev){
  ev.preventDefault();
  var form = this;
  var url = new URL(form.action);
  var data = new FormData(this);
  var xhrObject = new_xhr();
  xhrObject.open('post', url, true);
  xhrObject.addEventListener("load", traiteReponseFormulairePostMessage.bind(xhrObject, form));
  xhrObject.send(data);
  disableForm(form, true);
  document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
 }

function traiteReponseFormulairePostMessage(form, ev){
  if(this.readyState==4){
    if(this.status  == 200){
      document.getElementById("source").value="";
      document.getElementById("MessageInformation").innerHTML = "<p id=\"Ok\">Message ajouté avec succès.</p>";
    }
    else{
      document.getElementById("MessageInformation").innerHTML = "<p id=\"EnCours\">Chargement en cours...</p>";
    }
  }
  disableForm(form, false);
}

function requete_deconnexion(){
  var xhrObject = new_xhr();
  xhrObject.open('GET','services/logout.php', true);
  xhrObject.onreadystatechange = traiteReponseDeconnexion;
  xhrObject.send();
}

function traiteReponseDeconnexion(){
  if(this.readyState==4){
    if(this.status  == 200){
      requete_connexion();
    }
    else{
      document.getElementById("Connexion").innerHTML = "Chargement en cours...";
    }
  }
}

// Permet l'activation ou la désactivation d'un formualaire form suivant le cas
function disableForm(form, setDisable){
   for (var field of form)
     field.disabled = setDisable;
}

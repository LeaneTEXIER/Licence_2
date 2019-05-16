/* TEXIER Léane */

window.addEventListener("load", requete_chargement);

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

function requete_chargement() {
  var paramIndexLogin = location.search.substring(1).split('&').toString().indexOf('login');
  var login = location.search.substring(paramIndexLogin+1).split('&')[0];
  if(login.substring(0,6)=='login='){
    login = login.substring(6);
    var xhrObject = new_xhr();
    xhrObject.open('get','services/getUser.php?type=long&user='+login, true);
    xhrObject.onreadystatechange = traiteReponseChargement;
    xhrObject.send(null);
  }
  else{
    document.body.innerHTML =  "Page non existante: Pas de login";
  }
}

function traiteReponseChargement(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      if (myobject['status']==="error"){
        document.body.innerHTML = "Login innexistant";
        return;
      }
      var texte = "<h3>Informations du membre: </h3>";
      var user = myobject['result']['User'];
      texte += "<p>Login: "+user['ident']+"</p>";
      texte += "<p>Nom: "+user['name']+"</p>";
      texte += "<p>Description: "+user['description']+"</p>";
      document.getElementById("Informations").innerHTML = texte;
      document.getElementById("Photo").innerHTML = "<img src='services/getAvatar.php?size=large&user="+user['ident']+"' alt='Photo de profil'/>";
      requete_isLogged();
    }
    else{
      document.getElementById("Informations").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_isLogged(){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/isLogged.php', true);
  xhrObject.onreadystatechange = traiteReponseIsLogged;
  xhrObject.send(null);
 }


function traiteReponseIsLogged(){
  if(this.readyState==4){
    if(this.status  == 200){
      var paramIndexLogin = location.search.substring(1).split('&').toString().indexOf('login');
      var login = location.search.substring(paramIndexLogin+1).split('&')[0].substring(6);
      var myobject = JSON.parse(this.responseText);
      if (myobject['result']!= ""){
        if (myobject['result']==login){
          document.getElementById("MiseAJour").innerHTML = "<a href='MiseAJour.php'>Mettre à jour mon profil</a>";
        }
        else{
          requete_aboOuNon(myobject['result'], login);
        }
        document.getElementById("Connexion").innerHTML = "<button onclick=\"requete_deconnexion()\">Déconnexion</button>";
        document.getElementById("ListeAbonnements").innerHTML = "<button type=\"button\" onclick=\"requete_FindAbonnements('"+login+"')\">Liste d'abonnements</button>";
        document.getElementById("ListeAbonnes").innerHTML = "<button onclick=\"requete_abonnes('"+login+"')\">Liste d'abonnés</button>";
        document.getElementById("ButtonMessages").innerHTML = "<button onclick=\"requete_messages('"+login+"')\">Liste de messages</button>";
        document.getElementById("ButtonCitations").innerHTML = "<button onclick=\"requete_citations('"+login+"')\">Liste de citations</button>";
      }
      else{
        document.getElementById("MiseAJour").innerHTML = "";
        document.getElementById("Connexion").innerHTML = "";
        //Liste abonnements
        document.getElementById("ListeAbonnements").innerHTML = "";
        document.getElementById("ListeAbonnements").style.border = "none";
        document.getElementById("ListeAbonnements").style.padding = "0px";
        document.getElementById("ListeAbonnements").style.margin = "0px";
        //Liste abonnes
        document.getElementById("ListeAbonnes").innerHTML = "";
        document.getElementById("ListeAbonnes").style.border = "none";
        document.getElementById("ListeAbonnes").style.padding = "0px";
        document.getElementById("ListeAbonnes").style.margin = "0px";
        //Liste Messgaes
        document.getElementById("ListeMessages").innerHTML = "";
        document.getElementById("ListeMessages").style.border = "none";
        document.getElementById("ListeMessages").style.padding = "0px";
        document.getElementById("ListeMessages").style.margin = "0px";
        //Liste citations
        document.getElementById("ListeCitations").innerHTML = "";
        document.getElementById("ListeCitations").style.border = "none";
        document.getElementById("ListeCitations").style.padding = "0px";
        document.getElementById("ListeCitations").style.margin = "0px";
      }
    }
    else{
      document.getElementById("Connexion").innerHTML = "Chargement en cours...";
    }
  }
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
      requete_chargement();
    }
    else{
      document.getElementById("Connexion").innerHTML = "Chargement en cours...";
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

function requete_messages(author, before=-1){
   var xhrObject = new_xhr();
   if (before<=-1){
     xhrObject.open('get','services/findMessages.php?author='+author, true);
   }
   else{
     xhrObject.open('get','services/findMessages.php?author='+author+"&before="+before, true);
   }
   xhrObject.onreadystatechange = traiteReponseMessages;
   xhrObject.send(null);
 }

function traiteReponseMessages(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var author = myobject['args']['author'];
      var button = "";
      if (document.getElementById("ListeM").innerHTML===""){
        document.getElementById("ListeM").innerHTML = "<h3>Messages écrits par "+author+": </h3>";
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
        document.getElementById("ListeM").innerHTML += message;
        requete_NameAuthor(authorMessage, j);
      }
      if (myobject['result']['hasMore']===true){
        var before = myobject['result']['list'][i]['id'];
        button += "<button type=\"button\" onclick=\"requete_messages('"+author+"',"+before+")\">Afficher plus de messages</button>";
      }
      button += "<button type=\"button\" onclick=\"requete_messagesEffacer('"+author+"')\">Cacher les messages</button>";
      document.getElementById("ButtonMessages").innerHTML = button;
    }
    else{
        document.getElementById("ListeM").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_messagesEffacer(login){
  document.getElementById("ListeM").innerHTML = "";
  document.getElementById("ButtonMessages").innerHTML = "<button onclick=\"requete_messages('"+login+"')\">Liste de messages</button>";
}

function requete_citations(mentioned, before=-1){
   var xhrObject = new_xhr();
   if (before<=-1){
     xhrObject.open('get','services/findMessages.php?mentioned='+mentioned, true);
   }
   else{
     xhrObject.open('get','services/findMessages.php?mentioned='+mentioned+"&before="+before, true);
   }
   xhrObject.onreadystatechange = traiteReponseCitations;
   xhrObject.send(null);
 }

function traiteReponseCitations(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var mentioned = myobject['args']['mentioned'];
      var liste = "";
      var button = "";
      if (document.getElementById("ListeC").innerHTML===""){
        document.getElementById("ListeC").innerHTML = "<h3>Messages où "+mentioned+" est cité: </h3>";
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
        document.getElementById("ListeC").innerHTML += message;
        requete_NameAuthor(authorMessage, j);
      }
      if (myobject['result']['hasMore']===true){
        var before = myobject['result']['list'][i]['id'];
        button += "<button type=\"button\" onclick=\"requete_citations('"+mentioned+"',"+before+")\">Afficher plus de messages</button>";
      }
      button += "<button type=\"button\" onclick=\"requete_citationsEffacer('"+mentioned+"')\">Cacher les messages</button>";
      document.getElementById("ButtonCitations").innerHTML = button;
    }
    else{
        document.getElementById("ListeC").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_citationsEffacer(login){
  document.getElementById("ListeC").innerHTML = "";
  document.getElementById("ButtonCitations").innerHTML = "<button onclick=\"requete_citations('"+login+"')\">Liste de citations</button>";
}


function requete_FindAbonnements(login){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/abonnements.php?login='+login, true);
  xhrObject.onreadystatechange = traiteAbonnements;
  xhrObject.send(null);
}

function traiteAbonnements(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var login = myobject['args']['login'];
      var liste = "<h3>Abonnements de "+login+": </h3><ul>";
      for(var i in myobject['result']){
        liste += "<li><a href=\"pageMembre.php?login="+myobject['result'][i]+"\">"+myobject['result'][i]+"</a></li>";
      }
      liste += "</ul><button type=\"button\" onclick=\"requete_abonnementsEffacer('"+login+"')\">Cacher les abonnements</button>";
      document.getElementById("ListeAbonnements").innerHTML = liste;
    }
    else{
        document.getElementById("ListeAbonnements").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_abonnementsEffacer(login) {
  document.getElementById("ListeAbonnements").innerHTML = "<button type=\"button\" onclick=\"requete_FindAbonnements('"+login+"')\">Liste d'abonnements</button>";
}


function requete_abonnes(login){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/abonnes.php?login='+login, true);
  xhrObject.onreadystatechange = traiteAbonnes;
  xhrObject.send(null);
}

function traiteAbonnes(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var login = myobject['args']['login'];
      var liste = "<h3>Abonnés de "+login+": </h3><ul>";
      for(var i in myobject['result']){
        liste += "<li><a href=\"pageMembre.php?login="+myobject['result'][i]+"\">"+myobject['result'][i]+"</a></li>";
      }
      liste += "</ul><button type=\"button\" onclick=\"requete_abonnesEffacer('"+login+"')\">Cacher les abonnés</button>";
      document.getElementById("ListeAbonnes").innerHTML = liste;
    }
    else{
        document.getElementById("ListeAbonnes").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_abonnesEffacer(login) {
  document.getElementById("ListeAbonnes").innerHTML = "<button onclick=\"requete_abonnes('"+login+"')\">Liste d'abonnés</button>";
}


function requete_aboOuNon(follower, membre_suivi){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/aboOuNon.php?follower='+follower+'&membre_suivi='+membre_suivi, true);
  xhrObject.onreadystatechange = traiteAboDesabo;
  xhrObject.send(null);
}

function traiteAboOuNon(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var follower = myobject['args']['follower'];
      var membre_suivi = myobject['args']['membre_suivi'];
      if (myobject['result']['Abo'] === true){
        var abo = "S'abonner";
      }
      else{
        var abo = "Se désabonner";
      }
      document.getElementById("Abo_Desabo").innerHTML = "<button onclick=\"requete_aboDesabo('"+follower+"','"+membre_suivi+"')\">"+abo+"</button>";
    }
    else{
        document.getElementById("Abo_Desabo").innerHTML ="Chargement en cours...";
    }
  }
}

function requete_aboDesabo(follower, membre_suivi){
  var xhrObject = new_xhr();
  xhrObject.open('get','services/AboDesabo.php?follower='+follower+'&membre_suivi='+membre_suivi, true);
  xhrObject.onreadystatechange = traiteAboDesabo;
  xhrObject.send(null);
}

function traiteAboDesabo(){
  if(this.readyState==4){
    if(this.status  == 200){
      var myobject = JSON.parse(this.responseText);
      var follower = myobject['args']['follower'];
      var membre_suivi = myobject['args']['membre_suivi'];
      if (myobject['result'] === 'Abonnement'){
        var abo = "Se désabonner";
      }
      else{
        var abo = "S'abonner";
      }
      document.getElementById("Abo_Desabo").innerHTML = "<button onclick=\"requete_aboDesabo('"+follower+"','"+membre_suivi+"')\">"+abo+"</button>";
    }
    else{
        document.getElementById("Abo_Desabo").innerHTML ="Chargement en cours...";
    }
  }
}

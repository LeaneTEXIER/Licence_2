/* Léane Texier */
window.addEventListener("load",change);
window.addEventListener("load",dessinerCarte);

function change(){
  if (document.getElementById("critere").value == "velosD" || document.getElementById("critere").value == "placesD") {
   document.getElementById("dispo").style.display = "block";
   document.getElementById("nom").style.display = "none";
   document.getElementById("distance").style.display = "none";
   document.getElementById('carteForm').style.width = "0px";
   document.getElementById('carteForm').style.height = "0px";
  }
  else if (document.getElementById("critere").value == "stations" || document.getElementById("critere").value == "communes"){
    document.getElementById("dispo").style.display = "none";
    document.getElementById("nom").style.display = "block";
    document.getElementById("distance").style.display = "none";
    document.getElementById('carteForm').style.width = "0px";
    document.getElementById('carteForm').style.height = "0px";
  }
  else {
    document.getElementById("dispo").style.display = "none";
    document.getElementById("nom").style.display = "none";
    document.getElementById("distance").style.display = "block";
    document.getElementById('carteForm').style.width = "50%";
    document.getElementById('carteForm').style.height = "300px";
  }
}


function dessinerCarte(){
    /* Creation de la carte */
    var map = L.map('carteForm').setView([50.631672, 3.061784], 15);
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '©️ <a href="http://osm.org/copyright">OpenStreetMap>/a> contributors'
    }).addTo(map);
    /*Marqueur*/
    var marker = L.marker([50.631672, 3.061784]).addTo(map);
    map.on('click', placerMarqueur);
    function placerMarqueur(e) {
        marker.setLatLng(e.latlng);
        var mark_pos = marker.getLatLng();
        document.getElementById('lat').value = mark_pos.lat;
        document.getElementById('lng').value = mark_pos.lng;
    };
}

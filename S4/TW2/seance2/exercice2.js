/* Léane Texier */
function change_class(num) { 
	var btn = document.getElementById(num); 
	if (btn.className== "noir"){
		btn.className='vide';
		btn.innerHTML = '';
	}
	else if (btn.className== "blanc"){
		btn.className="noir";
		btn.innerHTML = 'N';
	}
	else{
		btn.className="blanc";
		btn.innerHTML = 'B';
	}
} 

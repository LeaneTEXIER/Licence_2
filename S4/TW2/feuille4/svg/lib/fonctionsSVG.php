<?php
/*Léane Texier*/
function cercle($cx, $cy, $r){
	return '<circle cx='.$cx.' cy='.$cy.' r='.$r.' />';
}

function carre($cx,$cy,$r,$angle=0){
	$c = $r*sqrt(2);
	$x = $cx-($c/2);
	$y = $cy-($c/2);
	return '<rect x='.$x.' y='.$y.' width='.$c.' height='.$c.' transform="rotate('.$angle.','.$cx.','.$cy.')" />';
}

function triangleInscrit($cx,$cy,$r,$angle=0){
	$s1x = $cx;
	$s1y = $cy+$r;
	$s2x = $cx-(($r*sqrt(3))/2);
	$s2y = $cy-($r/2);
	$s3x = $cx+(($r*sqrt(3))/2);
	$s3y = $s2y;
	$points=$s1x.','.$s1y.' '.$s2x.','.$s2y.' '.$s3x.','.$s3y;
	return '<polygon points="'.$points.'" transform="rotate('.$angle.','.$cx.','.$cy.')" />';
}

?>

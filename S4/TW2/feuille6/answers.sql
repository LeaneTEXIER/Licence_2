-- Léane Texier

-- Bases de données - SQL

-- Question 1.1:
-- a
select dossard, nom
from coureurs;

-- b
select dossard, nom
from coureurs
order by dossard;

-- c
select dossard, nom
from coureurs
order by equipe, nom;

-- d
select dossard, nom, taille
from coureurs
order by taille;

-- e
select dossard, nom
from coureurs
where equipe='LavePlusBlanc';

-- f
select coureurs."dossard", coureurs."nom"
from coureurs
where equipe='LavePlusBlanc';

-- g
select nom, taille, equipe
from coureurs
where taille<'180';

-- h
select nom, taille, equipe
from coureurs
where taille<'180'
order by taille;

-- i
select couleur
from equipes;


-- Question 1.2:
-- a
select (nom || ' appartient à l' || chr(39) || 'équipe ' || equipe)
from coureurs;

-- b
select (nom || ' appartient à l' || chr(39) || 'équipe ' || equipe) as appartenance
from coureurs;

-- c
select upper(nom) as "nom maj",
char_length(nom) as "lg"
from coureurs;

-- d
select upper(nom), char_length(nom)
from coureurs
order by char_length(nom);

select upper(nom) as "nom maj",
char_length(nom) as "lg"
from coureurs
order by lg;

-- e
select dossard, initcap(nom), upper(substring(equipe from 1 for 3))
from coureurs;


-- Question 1.3:
-- a
select nom
from coureurs
where nom
like 'a%' ;

-- b
select nom
from coureurs
where nom like '%er%' ;

-- c
select nom
from coureurs
where nom like '_____' ;

-- d
select nom
from coureurs
where nom like '%a__' ;

-- e
select nom
from coureurs
where nom like '%a__%' ;


-- Question 1.4:
-- a
select taille/100
from coureurs;
-- Le résultat ne correspond pas à nos attentes car on divise par 100 qui est un entier donc la division renvois un entier.

-- b
select taille/100.0
from coureurs;
-- Le résultat ne correspond toujours pas à nos attentes car des zéros non significatifs sont ajoutés à la fin. On a un flottant.

-- c
select cast(taille/100.0 as float) from coureurs;


-- Question 1.5:
-- a
select *
from coureurs, equipes;

-- b
select *
from coureurs, equipes
where equipe=equipes.nom;

-- c
select dossard, coureurs.nom, equipes.nom, couleur
from coureurs, equipes
where equipe=equipes.nom;

-- d
select coureurs.nom, directeur
from coureurs, equipes
where equipe=equipes.nom;

-- e
select coureurs.nom, dossard
from coureurs, equipes
where equipe=equipes.nom and directeur='Ralph';

-- f
select directeur
from coureurs, equipes
where equipe=equipes.nom and coureurs.nom='alphonse';


-- Question 1.6:
-- a
insert into equipes
values('TousPourUn', 'Rouge', 'Roland');

-- b
insert into coureurs
values('8', 'léane', 'TousPourUn', 160);

insert into coureurs
values('9', 'florian', 'TousPourUn', 182);

insert into coureurs
values('10', 'quentin', 'TousPourUn', 205);


-- Question 1.7:
-- a
select nom
from equipes
where directeur is null;

-- b
select nom
from equipes
where directeur is not null;


-- Question 1.8:
-- a
update coureurs
set taille = taille-1
where equipe = 'PicsouBank';

-- b
update equipes
set directeur = 'Robert'
where nom = 'Nouvelle Equipe';


-- Question 1.9:
CREATE TABLE etape
(
dossard integer,
arrivee time
);

insert into etape ("dossard")
select "dossard"
from coureurs;

update etape
set arrivee = '17:32:30'
where dossard = 1;

update etape
set arrivee = '17:52:35'
where dossard = 2;

update etape
set arrivee = '18:02:25'
where dossard = 3;

update etape
set arrivee = '16:52:15'
where dossard = 4;

update etape
set arrivee = '17:22:54'
where dossard = 5;

update etape
set arrivee = '17:35:54'
where dossard = 6;

update etape
set arrivee = '17:44:26'
where dossard = 7;

update etape
set arrivee = '17:23:23'
where dossard = 8;

update etape
set arrivee = '17:05:51'
where dossard = 9;

update etape
set arrivee = '17:10:10'
where dossard = 10;


-- Question 1.10
-- a
select etape.dossard, nom, arrivee
from coureurs, etape
where etape.dossard=coureurs.dossard
order by arrivee;

-- b
select etape.dossard, nom, arrivee
from coureurs, etape
where etape.dossard=coureurs.dossard and arrivee<'17:30:00'
order by arrivee;

-- c
select etape.dossard, coureurs.nom, equipes.nom, couleur, arrivee
from coureurs, etape, equipes
where etape.dossard=coureurs.dossard and equipe=equipes.nom
order by arrivee;


-- Question 1.11
-- cf question11.php


-- Question 1.12
-- cf question12.html

-- Question 1.13
-- cf question13.html

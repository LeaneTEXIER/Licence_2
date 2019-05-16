-- TEXIER Léane

-- Exercice 1
-- Question 1.3
-- 1
select code_voie, nom_voie
from voies
where code_commune = '59009'

-- 2
select code_voie, numero
from adresses
where code_voie = '2120' and code_commune = '59009'

-- 3 
select nom_voie, numero
from adresses
where code_voie = '2120' and code_commune = '59009'

-- 4
select count(*)
from adresses
where code_voie = '2120' and code_commune = '59009'

-- 5 
select code_voie, count (nom_voie)
from adresses
where code_commune = '59009'
group by code_voie

-- 6
select code_voie, nom_voie
from voies, communes
where communes.code_commune = voies.code_commune
and nom_commune = 'Lille'

-- 7
select nom_commune
from adresses, communes
where communes.code_commune = adresses.code_commune
and nom_voie = 'Avenue Paul Langevin' 

-- 8
select nom_commune
from adresses, communes
where communes.code_commune = adresses.code_commune
and nom_voie = 'Avenue Paul Langevin'
and numero ='12'

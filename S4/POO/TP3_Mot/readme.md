# Léane Texier

# Le TP et ses objectifs
Le TP3 est sur les mots (objet Word).
Un Word est défini par sa valeur qui est un str.
Ce TP3 a pour but de définir plusieurs fonctions à utiliser sur les mots:
* Connaitre la longueur du mot: nbOfChars()
* Renvoyer une chaîne de caractères corrspondant au mot: toString()
* Connaitre le nombre d'occurences d'un caractère c dans un mot: nbOccurrencesOfChar(char c)
* Retourne un nouveau Word dont sa valeur est l'inverse du mot initial: reverse()
* Savoir si un mot est un palindrome: isPalindrome()
* Savoir si un mot m est contenu dans le mot courant: contains(Word m)
* Savoir si 2 mots ont les 3 mêmes derniers caractères: rhymesWith(Word m)
* Savoir si un mot est un nom propre: isProperNoun()
* Savoir si un mot m est un anagramme du mot courant: isAnagram(Word m)
* Coupe le mot en deux en fonctions du caractère c (retourne un tableau): extractBefore(char c)

# Générer et consulter la documentation
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier TP3.    
Taper: javadoc Word.java -d docs (Cela va générer la doc de Word.java).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.   

# Compiler les classes du projet
Se placer dans le dossier TP3.   
Taper: javac Word.java (Cela va compiler la classe Word).    
Un nouveau fichier Word.class a été créé si tout s'est bien passé.   


# Compiler et executer les tests
A faire obligatoirement après avoir compilé les classes!      
Se placer dans le dossier TP3 si ce n'est pas encore le cas.   
Taper: javac -classpath .:test-1.7.jar WordTest1.java  
Un nouveau fichier WordTest1.class a été créé si tout s'est bien passé.  
Taper: javac -classpath .:test-1.7.jar WordTest.java  
Un nouveau fichier WordTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar WordTest  
Les tests sont alors effectués.  

# Executer le programme (+exemples)
Compiler WordMain en tapant: javac WordMain.java  
Un nouveau fichier WordMain.class a été créé si tout s'est bien passé.  
Lancer le programme(exemples):
* java WordMain radar a darrr
* java WordMain Timéo c im
* java WordMain timéo m siméo

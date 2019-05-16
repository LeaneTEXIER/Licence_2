# Léane Texier

# Le TP et ses objectifs             
Le TP5 est sur Hanoi. Il y a la résolution du problème des tours de Hanoi ainsi qu'un programme permettant de jouer.  


# Générer et consulter la documentation       
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier TP_Hanoi.    
Aller dans le dossier src.      
Taper: javadoc hanoi hanoi.util -d ../docs (Cela va générer la doc).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.   


# Compiler les sources du projet           
Se placer dans le dossier src.   
Taper: javac hanoi/Hanoi.java -d ../classes (Cela va compiler la classe Hanoi et ses sous-classes).   


# Compiler et executer les tests              
A faire obligatoirement après avoir compilé les classes!      
Se placer dans le dossier TP_Hanoi.   
Taper: javac -classpath test-1.7.jar test/TowerTest.java     
Un nouveau fichier TowerTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar TowerTest   
Les tests de TowerTest sont alors effectués.   

Taper: javac -classpath test-1.7.jar test/DiscTest.java    
Un nouveau fichier DiscTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar DiscTest   
Les tests de DiscTest sont alors effectués.  

Taper: javac -classpath test-1.7.jar test/HanoiTest.java    
Un nouveau fichier HanoiTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar HanoiTest   
Les tests de HanoiTest sont alors effectués.   


# Exectuer le programme Main      
Le programme HanoiMain renvois une suite de mouvements qui permet de résoudre le problème des tours de Hanoi pour un nombre de disques donnés.   
Se placer dans le dossier src.  
Compiler HanoiMain en tapant: javac hanoi/HanoiMain.java -d ../classes   
Un nouveau fichier HanoiMain.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.    
Lancer le programme(exemples): (Pour une tour de 3 disques) java hanoi.HanoiMain 3   
			       (Pour une tour de 5 disques) java hanoi.HanoiMain 5   



# Générer le fichier .jar              
Se placer dans le dossier classes.    
Taper: jar cvf ../hanoi.jar hanoi io    


# Executer le jar (+exemples)           
Se placer dans le dossier TP_Hanoi.   
Taper par exemple: java -classpath hanoi.jar hanoi.Hanoi 5      
Cela va executer avec le jar executable avec une tour de 5 (disques).    

Se placer dans le dossier classes.    
Taper par exemple: java hanoi.Hanoi 8   
Cela va executer sans le jar executable avec une tour de 8 (disques).   

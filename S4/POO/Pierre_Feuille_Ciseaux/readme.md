# Léane Texier

# Le TP et ses objectifs             
Le TP6 est sur le jeu Pierre-Feuille-Ciseaux. Il implémente plusieurs stratégies de jeux et permet de jouer.


# Générer et consulter la documentation       
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier Pierre_Feuille_Ciseaux.    
Aller dans le dossier src.      
Taper: javadoc prs prs.strategies -d ../docs (Cela va générer la doc).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.   


# Compiler les sources du projet           
Se placer dans le dossier src.   
Taper: javac prs/Game.java prs/Shape.java -d ../classes(Cela va compiler la classe Game et Shape et ses sous-classes).   
Taper: javac prs/strategies/InteractiveStrat.java prs/strategies/PaperStrat.java prs/strategies/RandomStrat.java prs/strategies/RockStrat.java prs/strategies/SissorsStrat.java -d ../classes    
(Cela va compiler les classes de strategies)    


# Compiler et executer les tests              
A faire obligatoirement après avoir compilé les classes!        
Se placer dans le dossier Pierre_Feuille_Ciseaux.     
Taper: javac -classpath test-1.7.jar test/PlayerTest.java            
Un nouveau fichier PlayerTest.class a été créé si tout s'est bien passé.    
Taper: java -jar test-1.7.jar PlayerTest    
Les tests de PlayerTest sont alors effectués.    

Taper: javac -classpath test-1.7.jar test/ShapeTest.java    
Un nouveau fichier ShapeTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar ShapeTest   
Les tests de ShapeTest sont alors effectués.   


# Exectuer le programme Main      
Le programme Main permet de jouer à Pierre_Feuille_Ciseaux.    
Se placer dans le dossier src.  
Compiler Main en tapant: javac prs/Main.java -d ../classes    
Un nouveau fichier Main.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.   
Lancer le programme: java prs.Main    
Puis compléter les questions pour pouvoir jouer.    


# Générer le fichier .jar              
Se placer dans le dossier classes.    
Taper: jar cvf ../MainPRS.jar prs util     
Cela va créér le jar executable.    


# Executer le jar (+exemples)           
Se placer dans le dossier Pierre_Feuille_Ciseaux.    
Taper: java -classpath MainPRS.jar prs.Main       
Cela va executer avec le jar executable.    

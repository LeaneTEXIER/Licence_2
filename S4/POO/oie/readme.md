# Léane Texier

# Le TP et ses objectifs               
Le TP est sur le jeu de l'oie et son déroulement. On doit donc simuler des parties de ce jeu en fonction d'un certain nombre de joueurs.          

# Générer et consulter la documentation       
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier oie.    
Aller dans le dossier src.      
Taper: javadoc goosegame -d ../docs (Cela va générer la doc).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.     

# Compiler les sources du projet           
Se placer dans le dossier src.   
Taper: javac goosegame/* -d ../classes        
(Cela va compiler toutes les classes présentes dans le dossier goosegame).     

# Compiler et executer les tests              
A faire obligatoirement après avoir compilé les classes!      
Se placer dans le dossier oie.   
Taper: javac -classpath test-1.7.jar test/goosegame/BasicCellTest.java     
Un nouveau fichier BasicCellTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.BasicCellTest    
Les tests de BasicCellTest sont alors effectués.      

Taper: javac -classpath test-1.7.jar test/goosegame/StartCellTest.java     
Un nouveau fichier StartCellTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.StartCellTest    
Les tests de StartCellTest sont alors effectués.     

Taper: javac -classpath test-1.7.jar test/goosegame/JumpCellTest.java     
Un nouveau fichier JumpCellTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.JumpCellTest    
Les tests de JumpCellTest sont alors effectués.     

Taper: javac -classpath test-1.7.jar test/goosegame/WaitCellTest.java     
Un nouveau fichier WaitCellTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.WaitCellTest    
Les tests de WaitCellTest sont alors effectués.    

Taper: javac -classpath test-1.7.jar test/goosegame/GooseCellTest.java     
Un nouveau fichier GooseCellTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.GooseCellTest    
Les tests de GooseCellTest sont alors effectués.      

Taper: javac -classpath test-1.7.jar test/goosegame/TrapCellTest.java     
Un nouveau fichier TrapCellTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.TrapCellTest    
Les tests de TrapCellTest sont alors effectués.     

Taper: javac -classpath test-1.7.jar test/goosegame/PlayerTest.java     
Un nouveau fichier PlayerTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.PlayerTest    
Les tests de PlayerTest sont alors effectués.     

Taper: javac -classpath test-1.7.jar test/goosegame/ClassicBoardTest.java     
Un nouveau fichier ClassicBoardTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar goosegame.ClassicBoardTest    
Les tests de ClassicBoardTest sont alors effectués.       

# Exectuer le programme Main    
Se placer dans le dossier src.
Le GameMain a normalement déjà été compilé. Si ce n'est pas le cas:  
Compiler-le en tapant: javac goosegame/GameMain.java -d ../classes   
Un nouveau fichier GameMain.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.    
Lancer le programme (par exemple): java goosegame.GameMain 3       (Cela va lancer la partie avec 3 joueurs)              
                                   java goosegame.GameMain 5       (Cela va lancer la partie avec 5 joueurs)                  

# Générer le fichier .jar              
Se placer dans le dossier classes.    
Taper: jar cvf ../goosegame.jar goosegame                 

# Executer le jar (+exemples)           
Se placer dans le dossier oie.   
Taper par exemple: java -classpath goosegame.jar goosegame.GameMain 4           
Cela va executer avec le jar executable le main(partie de jeu de l'oie) avec 4 joueurs.     

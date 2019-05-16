# Léane Texier

# Le TP et ses objectifs             
Le TP4 nous apprends à faire des tests unitaires ainsi que les manipulations à effectuer lors d'un tp.  


# Générer et consulter la documentation       
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier TP4.    
Aller dans le dossier src.      
Taper: javadoc example example.util -d ../docs (Cela va générer la doc).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.   


# Compiler les sources du projet           
Se placer dans le dossier src.   
Taper: javac example/Robot.java -d ../classes (Cela va compiler la classe Robot et ses sous-classes).   


# Compiler et executer les tests           
A faire obligatoirement après avoir compilé les classes!      
Se placer dans le dossier TP4.   
Taper: javac -classpath test-1.7.jar test/BoxTest.java   
Un nouveau fichier BoxTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar BoxTest   
Les tests de BoxTest sont alors effectués.  

Taper: javac -classpath test-1.7.jar test/RobotTest.java     
Un nouveau fichier RobotTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar RobotTest   
Les tests de RobotTest sont alors effectués.  


# Générer le fichier .jar              
Se placer dans le dossier classes.    
Taper: jar cvf ../appli.jar example   


# Executer le programme (+exemples)           
Se placer dans le dossier TP4.   
Taper: java -classpath appli.jar example.Robot   
Cela va executer avec le jar executable.  

Se placer dans le dossier classes.    
Taper: java example.Robot   
Cela va executer sans le jar executable.   

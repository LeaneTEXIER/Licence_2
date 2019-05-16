# Léane Texier

# Le TP et ses objectifs             
Le TP est sur les agences de location.
On manipule les collections et on fait des héritages.

# Générer et consulter la documentation       
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier agence.    
Aller dans le dossier src.      
Taper: javadoc rental -d ../docs (Cela va générer la doc).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.   


# Compiler les sources du projet           
Se placer dans le dossier src.   
Taper: javac rental/InterCriterion.java -d ../classes        
(Cela va compiler la classe InterCriterion et ses sous-classes).    
Taper: javac rental/RentalAgency.java -d ../classes        
(Cela va compiler la classe RentalAgency et ses sous-classes).           
Taper: javac rental/Car.java  -d ../classes      
(Cela va compiler la classe Car et ses sous-classes).    
Taper: javac rental/MotorBike.java  -d ../classes         
(Cela va compiler la classe MotorBike et ses sous-classes).    
Taper: javac rental/SuspiciousRentalAgency.java  -d ../classes         
(Cela va compiler la classe SuspiciousRentalAgency et ses sous-classes).

# Compiler et executer les tests              
A faire obligatoirement après avoir compilé les classes!      
Se placer dans le dossier agence.   
Taper: javac -classpath test-1.7.jar test/rental/InterCriterionTest.java     
Un nouveau fichier InterCriterionTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar rental.InterCriterionTest    
Les tests de InterCriterionTest sont alors effectués.   

Taper: javac -classpath test-1.7.jar test/rental/RentalAgencyTest.java         
Un nouveau fichier RentalAgencyTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar rental.RentalAgencyTest      
Les tests de RentalAgencyTest sont alors effectués.  

Taper: javac -classpath test-1.7.jar test/rental/CarTest.java         
Un nouveau fichier CarTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar rental.CarTest      
Les tests de CarTest sont alors effectués.

Taper: javac -classpath test-1.7.jar test/rental/MotorBikeTest.java         
Un nouveau fichier MotorBikeTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar rental.MotorBikeTest      
Les tests de MotorBikeTest sont alors effectués.

Taper: javac -classpath test-1.7.jar test/rental/SuspiciousRentalAgencyTest.java         
Un nouveau fichier SuspiciousRentalAgencyTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar rental.SuspiciousRentalAgencyTest      
Les tests de SuspiciousRentalAgency sont alors effectués.


# Exectuer le programme MainQ2    
Se placer dans le dossier src.  
Compiler MainQ2 en tapant: javac rental/MainQ2.java -d ../classes   
Un nouveau fichier MainQ2.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.    
Lancer le programme: java rental.MainQ2     

# Exectuer le programme MainQ5    
Se placer dans le dossier src.  
Compiler MainQ5 en tapant: javac rental/MainQ5.java -d ../classes   
Un nouveau fichier MainQ5.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.    
Lancer le programme: java rental.MainQ5   

# Exectuer le programme MainQ7    
Se placer dans le dossier src.  
Compiler MainQ5 en tapant: javac rental/MainQ7.java -d ../classes   
Un nouveau fichier MainQ7.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.    
Lancer le programme: java rental.MainQ7


# Générer le fichier .jar              
Se placer dans le dossier classes.    
Taper: jar cvf ../agency.jar rental      


# Executer le jar (+exemples)           
Se placer dans le dossier agence.   
Taper par exemple: java -classpath agency.jar rental.MainQ2         
Cela va executer avec le jar executable du main de la question 2.    

Taper par exemple: java -classpath agency.jar rental.MainQ5            
Cela va executer avec le jar executable du main de la question 5.       

Taper par exemple: java -classpath agency.jar rental.MainQ7         
Cela va executer avec le jar executable du main de la question 7.    

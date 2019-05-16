# Léane Texier

# Le TP et ses objectifs             
Le TP6 est sur le traitement d'images.
On apprend à créer des images, changer des pixels (couleur), créer des images avec un certains nombres de gris et avec seulement les contours.


# Générer et consulter la documentation       
Ouvrir un terminal   
Récuperer le projet par git pull.    
Se placer dans le dossier image.    
Aller dans le dossier src.      
Taper: javadoc image image.color -d ../docs (Cela va générer la doc).    
Pour consulter la documentation, se placer dans le dossier docs généré ci-dessus puis ouvrir index.html dans un navigateur.   
Consulter la doc.   


# Compiler les sources du projet           
Se placer dans le dossier src.   
Taper: javac image/Image.java -d ../classes (Cela va compiler la classe Image et ses sous-classes).   
       
          
# Compiler et executer les tests              
A faire obligatoirement après avoir compilé les classes!      
Se placer dans le dossier image.   
Taper: javac -classpath test-1.7.jar test/GrayColorTest.java     
Un nouveau fichier GrayColorTest.class a été créé si tout s'est bien passé.   
Taper: java -jar test-1.7.jar GrayColorTest   
Les tests de GrayColorTest sont alors effectués.   
                 
Taper: javac -classpath test-1.7.jar test/ImageTest.java    
Un nouveau fichier ImageTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar ImageTest   
Les tests de ImageTest sont alors effectués.  
             
Taper: javac -classpath test-1.7.jar test/PixelTest.java    
Un nouveau fichier PixelTest.class a été créé si tout s'est bien passé.  
Taper: java -jar test-1.7.jar PixelTest   
Les tests de PixelTest sont alors effectués.   
     
         
# Executer le programme Example        
Le programme ImageExample renvois 4 images:       
*L'image initiale (3 rectangles avec un niveau différent de gris)    
*L'image avec extraction des contours selon le seuil 10    
*L'image avec extraction des contours selon le seuil 90    
*L'image avec extraction des contours selon le seuil 248    
               
Se placer dans le dossier src.         
Compiler ImageExample en tapant: javac image/ImageExample.java -d ../classes     
Un nouveau fichier ImageExample.class a été créé si tout s'est bien passé.    
Se placer dans le dossier classes.    
Lancer le programme: java image.ImageExample    
Les 4 images s'affichent.    


# Générer le fichier .jar de Example              
Se placer dans le dossier classes.    
Taper: jar cvf ../ImageExample.jar image     


# Executer le jar (+exemples) de Example                       
Se placer dans le dossier image.   
Taper: java -classpath ImageExample.jar image.ImageExample         
Cela va executer ImageExample avec le jar executable.    


# Programme Main      
Le programme ImageMain renvois 3 images:    
*L'image initiale (1er paramètre)   
*L'image avec extraction des contours selon le seuil rentré (2ème paramètre)   
*L'image avec un nombre de niveaux de gris donné (3ème paramètre)   
          
Se placer dans le dossier src.  
Compiler ImageMain en tapant: javac image/ImageMain.java -d ../classes   
Un nouveau fichier ImageMain.class a été créé si tout s'est bien passé.    


# Générer le fichier .jar du Main            
Se placer dans le dossier classes.    
Taper: jar cvf ../ImageMain.jar image ../images     


# Executer le jar (+exemples) du Main             
Se placer dans le dossier image.   
Taper par exemple: java -classpath ImageMain.jar image.ImageMain /images/fruit.pgm 15 16      
Cela va executer ImageMain avec le jar executable avec l'image fruits.pgm, un seuil de contour de 15 et un niveau de gris de 16.    
Taper par exemple: java -classpath ImageMain.jar image.ImageMain /images/casablanca.pgm 14 5   
Cela va executer ImageMain avec le jar executable avec l'image casablanca.pgm, un seuil de contour de 14 et un niveau de gris de 4.     

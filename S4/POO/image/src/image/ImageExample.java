package image;

import image.Image;
import image.*;
import image.color.*;

import java.util.*;
/**
 * Example of image (edges)
 *
 * @author Leane Texier
 * @version 1.0
 */
public class ImageExample{
  public static void main(String[] args){
    Image img = new Image(100, 200);
    /* Création d'un rectangle noir de taille 20x30 à partir du point (10,30) */
    for (int x=10; x<10+20; x++){
      for (int y=30; y<30+30; y++){
        img.changeColorPixel(x, y, GrayColor.BLACK);
      }
    }
    /* Création d'un rectangle gris (niv. 64) de taille 20x50 à partir du point (50,50) */
    for (int x=50; x<50+20; x++){
      for (int y=50; y<50+50; y++){
        img.changeColorPixel(x, y, new GrayColor(64));
      }
    }
    /* Création d'un rectangle gris (niv. 230) de taille 20x50 à partir du point (20,110) */
    for (int x=20; x<20+20; x++){
      for (int y=110; y<110+50; y++){
        img.changeColorPixel(x, y, new GrayColor(230));
      }
    }
    /*Création des différentes images grace à la fonction edge suivant diverses valeurs*/
    Image img1 = img.edge(10);
    Image img2 = img.edge(90);
    Image img3 = img.edge(248);
    /* Création ImageDisplayer*/
    ImageDisplayer imgDis = new ImageDisplayer();
    /*Affichage des différentes images */
    imgDis.display(img, "Image originale", 100, 200);
    imgDis.display(img1, "Image edge:10", 100, 200);
    imgDis.display(img2, "Image edge:90", 100, 200);
    imgDis.display(img3, "Image edge:248", 100, 200);
  }
}

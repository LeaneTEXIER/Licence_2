package image;

import image.Image;
import image.*;
import image.color.*;

import java.util.*;
/**
 * Display initial image, with edges and with a number of gray levels
 *
 * @author Leane Texier
 * @version 1.0
 */
public class ImageMain{
  public static void main(String[] args){
    /* Image initiale */
    ImageDisplayer disp = new ImageDisplayer();
    Image im = new Image(1000, 1000);
    Image img = im.initImagePGM(args[0]);
    /* Récupération de données utiles */
    int width = img.getWidth();
    int height = img.getHeight();
    int sContour = Integer.parseInt(args[1]);
    int nbGray = Integer.parseInt(args[2]);
    /* Création des 2 autres images: edges et avec un certain nombre de gris */
    Image img1 = img.edge(sContour);
    Image img2 = img.decreaseNbGrayLevels(nbGray);
    /* Affichage des images */
    disp.display(img, "Image initiale", width, height);
    disp.display(img1, "Image avec contours", width, height);
    disp.display(img2, "Image avec un certains nombres de niveaux de gris", width, height);
  }
}

package image;

import image.Image;
import image.*;
import image.color.*;

import java.util.*;
/**
 * Image
 *
 * @author Leane Texier
 * @version 1.0
 */
public class Image implements ImageInterface {
    /** width of the image */
    private int width;
    /** height of the image */
    private int height;
    /** pixels of the image */
    private Pixel[][] thePixels;


    /** creates an image with pixels of color White
    * @param width the width of the image to create
    * @param height the height of the image to create
    */
    public Image(int width, int height){
      this.width = width;
      this.height = height;
      this.thePixels = new Pixel[width][height];
      for (int x=0; x<width; x++){
        for (int y=0; y<height; y++){
          this.thePixels[x][y] = new Pixel(GrayColor.WHITE);
        }
      }
    }

    /** get the width of the image
    * @return width of the image
    */
    public int getWidth(){
      return this.width;
    }

    /** get the height of the image
    * @return height of the image
    */
    public int getHeight(){
      return this.height;
    }


    /** gets the pixel at coord (x,y) of the image. (0,0) is top left corner pixel
    * @param x horizontal coordinate
    * @param y vertical coordinate
    * @return pixel at coord x,y of this image
    * @exception UnknownPixelException if pixel of coord (x,y) does not exist
    */
    public Pixel getPixel(int x, int y) throws UnknownPixelException{
      if ( 0<=x && x<this.width && 0<=y && y<this.height){
        return this.thePixels[x][y];
      }
      else{
        throw new UnknownPixelException ("Pixel non define");
      }
    }


    /** sets the pixel at coord (x,y) of the image. (0,0) is top left corner pixel.
    * @param x horizontal coordinate
    * @param y vertical coordinate
    * @param p new pixel
    * @exception UnknownPixelException if pixel of coord (x,y) does not exist
    */
    public void setPixel(int x, int y, Pixel p) throws UnknownPixelException{
      if ( 0<=x && x<this.width && 0<=y && y<this.height){
        this.thePixels[x][y] = p;
      }
      else{
        throw new UnknownPixelException ("Pixel non define");
      }
    }


    /** changes the color of the pixel at coord (x,y) with the given color
     * @param x horizontal coordinate of the pixel
     * @param y vertical coordinate of the pixel
     * @param color new color of the pixel
     */
    public void changeColorPixel(int x, int y, GrayColor color) throws UnknownPixelException{
      if ( 0<=x && x<this.width && 0<=y && y<this.height){
        this.thePixels[x][y].setColor(color);
      }
      else{
        throw new UnknownPixelException ("Pixel non define");
      }
    }


    /** returns an image with only the edges of the image.
    * A pixel is an edge if the right pixel or the one on its bottom are differents grays.
    * Grays are differents if the difference of level is bigger than the given threhold.
    * @param threshold int
    * @return Image
    */
    public Image edge(int threshold) {
      Image img = new Image(this.getWidth(), this.getHeight());
      for (int x=0; x<this.getWidth(); x++){
        for (int y=0; y<this.getHeight(); y++){
          if (x==this.getWidth()-1 && y==this.getHeight()-1){
            continue;
          }
          else if (x==this.getWidth()-1){
            if (this.getPixel(x,y).colorLevelDifference(this.getPixel(x,y+1))>=threshold){
              img.setPixel(x, y, new Pixel(GrayColor.BLACK));
            }
          }
          else if (y==this.getHeight()-1){
            if (this.getPixel(x,y).colorLevelDifference(this.getPixel(x+1,y))>=threshold){
              img.setPixel(x, y, new Pixel(GrayColor.BLACK));
            }
          }
          else{
            if (this.getPixel(x,y).colorLevelDifference(this.getPixel(x,y+1))>=threshold || this.getPixel(x,y).colorLevelDifference(this.getPixel(x+1,y))>=threshold){
              img.setPixel(x, y, new Pixel(GrayColor.BLACK));
            }
          }
        }
      }
      return img;
    }


    /** returns an image as the image but with number of grays (given number) between 2 and 128.
    * @param nbGrayLevels between 2 and 128
    * @return Image
    */
    public Image decreaseNbGrayLevels(int nbGrayLevels) {
      Image img = new Image(this.getWidth(), this.getHeight());
      int t = (GrayColor.WHITE.getGrayLevel()+1)/nbGrayLevels;
      for (int x=0; x<this.getWidth(); x++){
        for (int y=0; y<this.getHeight(); y++){
          img.changeColorPixel(x, y, new GrayColor((this.thePixels[x][y].getColor().getGrayLevel())/t*t));
        }
      }
      return img;
    }


    // ======================================================================
    /** Reads a PGM image from file.
     * It is assumed that file respects the following PGM file syntax:
     *  <ul><li> first line with string "P2"</li>
     *  <li>second line : a comment</li>
     *  <li>one int for width <code>w</code>, one int for height<code>h</code></li>
     *  <li>one int for max gray level (not used here, we consider this level to be 255 in our images)</li>
     *  <li><code>w</code> x <code>h</code> integers between 0 and max (for us max=255) for each pixel</li></ul>
     *
     * @param fileName the name of the image file in PGM format
     * @return the image built from the file
     */
    public static Image initImagePGM(String fileName) {
        Scanner scan = new Scanner(Image.class.getResourceAsStream(fileName));

        scan.nextLine(); // line P2
        scan.nextLine(); // line comment
        // read width
        int width = scan.nextInt();
        // read height
        int height = scan.nextInt();
        // read max gray level (not used)
        scan.nextInt();
        // create an initially white image
        Image result = new Image(width, height);
        // rad pixels
        for (int x = 0; x < height; x++) {
            for (int y = 0; y < width; y++) {
                result.changeColorPixel(y, x, new GrayColor(scan.nextInt()));
            }
        }
        return result;
    }


}

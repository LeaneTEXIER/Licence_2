package image;
import image.color.*;
import java.lang.Math;
/**
 * class for Pixel
 *
 * @author Leane Texier
 * @version 1.0
 */
public class Pixel{
  /** attribut of the pixel of type GrayColor */
  private GrayColor color;


  /**creates a pixel
  * @param color color of the new pixel
  */
  public Pixel(GrayColor color){
    this.color = color;
  }



  /** get the color of the object pixel
  * @return color of the object pixel
  */
  public GrayColor getColor(){
    return this.color;
  }

  /** set the color of the object pixel
  * @param color color to set
  */
  public void setColor(GrayColor color){
    this.color = color;
  }

  /** compares if the current object and the given one are the same
  * @param o the object to compare
  * @return <code>true</code> if both objects are the same, else <code>false</code>
  */
  public boolean equals(Object o){
    if (o instanceof Pixel){
      Pixel other = (Pixel) o;
      return this.getColor() == other.getColor();
    }
    return false;
  }

  /** returns the difference of level between the current pixel and the given one
  * @param p the pixel to compare to
  * @return the difference of level of the pixels
  */
  public int colorLevelDifference(Pixel p){
    return Math.abs(p.getColor().getGrayLevel() - this.getColor().getGrayLevel());
  }

}

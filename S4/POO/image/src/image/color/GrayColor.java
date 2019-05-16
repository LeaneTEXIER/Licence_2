package image.color;
/**
 * class for Gray Color
 *
 * @author Leane Texier
 * @version 1.0
 */
public class GrayColor{
  /** level of gray is 0, so it's WHITE */
  public static final GrayColor WHITE = new GrayColor(255);

  /** level of gray is 255, so it's BLACK */
  public static final GrayColor BLACK = new GrayColor(0);

  /** number of grayLevel */
  public static final int nb_grayLevel = 256;

  /** level of gray */
  private int grayLevel;

  /**creates GrayColor
  * @param level level of grey
  */
  public GrayColor(int level){
    this.grayLevel = level;
  }

  /**returns the level of gray
  * @return the level of gray
  */
  public int getGrayLevel(){
    return this.grayLevel;
  }

  /** compares if the current object and the given one are the same
  * @param o the object to compare
  * @return <code>true</code> if both objects are the same, else <code>false</code>
  */
  public boolean equals(Object o){
    if (o instanceof GrayColor){
      GrayColor other = (GrayColor) o;
      return this.grayLevel == other.grayLevel;
    }
    return false;
  }
}

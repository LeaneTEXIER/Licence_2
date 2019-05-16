package hanoi.util;
/**
 * Disc of Hanoi
 *
 * @author Leane Texier
 * @version 1.0
 */

public class Disc{
  private int size;

  /**creates a Disc
  * @param size the size of the disc
  */
  public Disc(int size){
    this.size = size;
  }

  /**returns the size of the disc
  * @return the size of the disc
  */
  public int getSize(){
    return this.size;
  }

  /**compare the size of two discs, returns 0 if the both discs have the same size, 1 if the current disc have a superior size to the other, else -1
  * @param other the disc to compare
  * @return 0 if the both discs have the same size, 1 if the current disc have a superior size to the other, else -1
  */
  public int compareTo(Disc other){
    if (this.size==other.size){
      return 0;
    }
    else if (this.size>other.size){
      return 1;
    }
    else{
      return -1;
    }
  }

  /**
  * @see java.lang.Object#toString()
  */
  public String toString(){
    return String.format("%i",this.size);
  }
}

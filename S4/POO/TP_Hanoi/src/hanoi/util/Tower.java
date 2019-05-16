package hanoi.util;
/**
 * Tower of Hanoi
 *
 * @author Leane Texier
 * @version 1.0
 */

public class Tower{
    private Disc[] theDiscs;
    private int capacity;
    private int nbDisc;

    /**creates a Tower
    * @param capacity the capacity of the tower
    */
    public Tower(int capacity){
      this.theDiscs = new Disc[capacity];
      this.capacity = capacity;
      this.nbDisc = 0;
    }

    /**returns the capacity of the tower
    * @return the capacity of the tower
    */
    public int getCapacity(){
      return this.capacity;
    }

    /**returns the number of discs of the tower
    * @return the nbDisc of the tower
    */
    public int getnbDisc(){
      return this.nbDisc;
    }

    /**returns the table of discs of the tower of Hanoi
    * @return the table of discs of the tower of Hanoi
    */
    public Disc[] getTheDiscs(){
      return this.theDiscs;
    }

    /** tells whether tower is empty
  	 * @return <code>true</code> if tower is empty
  	 */
    public boolean isEmpty(){
      return this.nbDisc==0;
    }

    /** tells whether tower is full
  	 * @return <code>true</code> if tower is full
  	 */
    public boolean isFull(){
      return this.nbDisc==this.capacity;
    }

    /** returns the disc on top of the tower
    * @return the disc on top of the tower
    */
    public Disc top(){
      return this.theDiscs[this.nbDisc-1];
    }

    /** takes the disc on top of the tower
    * @return the disc that was on top of the tower
    */
    public Disc pop() throws IllegalStateException{
      if (!this.isEmpty()){
        Disc d = this.top();
        this.theDiscs[this.nbDisc-1] = null;
        this.nbDisc = this.nbDisc - 1;
        return d;
      }
      else{
        throw new IllegalStateException("Tower is empty");
      }
    }

    /** puts the disc d given on the top of the tower if it's possible
    * @param d the disc to put on the tower
    */
    public void push (Disc d) throws IllegalStateException{
      if (this.isFull()){
        throw new IllegalStateException("Tower is full");
      }
      else if (this.isEmpty() || this.top().getSize() > d.getSize()){
        this.theDiscs[this.nbDisc] = d;
        this.nbDisc = this.nbDisc + 1;
      }
      else{
        throw new IllegalStateException("Disc d have a bigger diameter than the disc at the top of the tower");
      }
    }

    /**
    * @see java.lang.Object#toString()
    */
    public String toString(){
      String res = "";
      if (!this.isEmpty()){
        res += this.theDiscs[0].getSize();
      }
      for (int i=1; i<this.nbDisc; i++){
        res += ","+this.theDiscs[i].getSize();
      }
      return res;
    }

}

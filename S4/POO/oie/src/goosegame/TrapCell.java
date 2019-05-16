package goosegame;

public class TrapCell extends BasicCell{
  /** Creates a TrapCell at the number index
  *@param index the number of the cell
  */
  public TrapCell(int index){
    super(index);
  }

  public boolean canBeLeft(){
    return false;
  }

  public String toString(){
    return new String("cell "+index+" (trap)");
  }
}

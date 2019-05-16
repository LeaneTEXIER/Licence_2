package goosegame;

public class JumpCell extends BasicCell{

  protected int jumpIndex;
  /** Creates a JumpCell at the number index
  * @param index the number of the cell
  * @param jumpIndex the number of the arrival cell
  */
  public JumpCell(int index, int jumpIndex){
    super(index);
    this.jumpIndex = jumpIndex;
  }

  public int handleMove(int dicethrow){
    return this.jumpIndex;
  }

  public String toString(){
    return new String("cell "+index+" (teleport to "+jumpIndex+")");
  }
}

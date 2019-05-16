package goosegame;

public class GooseCell extends BasicCell{
  /** Creates a GooseCell at the number index
  * @param index the number of the cell
  */
  public GooseCell(int index){
    super(index);
  }

  public int handleMove(int dicethrow){
    return this.getIndex()+dicethrow;
  }

  public String toString(){
    return new String("cell "+index+" (goose)");
  }
}

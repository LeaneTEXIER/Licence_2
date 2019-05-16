package goosegame;

public class BasicCell implements Cell{
  protected int index;
  protected Player player;

  /** Creates a basic cell at the number index
  * @param index the number of the cell
  */
  public BasicCell(int index){
    this.index = index;
    this.player = null;
  }

  public int getIndex(){
    return this.index;
  }

  public Player getPlayer(){
    return this.player;
  }

  public boolean canBeLeft(){
    return true;
  }

  public int handleMove(int dicethrow){
    return this.index;
  }

  public boolean isBusy(){
    return this.player!=null;
  }

  public void putPlayerOnCell(Player p){
    this.player = p;
    if (p!=null){
      p.setCell(this);
    }
  }

  public String toString(){
    return new String("cell "+index);
  }
}

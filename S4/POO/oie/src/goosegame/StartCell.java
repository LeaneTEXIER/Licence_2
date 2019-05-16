package goosegame;

public class StartCell implements Cell{

  protected int index;
  protected Player player;
  
  /** Creates a start cell at the cell 0
  */
  public StartCell(){
    this.index = 0;
    this.player = null;
  }

  public int getIndex(){
    return 0;
  }

  public Player getPlayer(){
    return null;
  }

  public boolean canBeLeft(){
    return true;
  }

  public int handleMove(int dicethrow){
    return 0;
  }

  public boolean isBusy(){
    return false;
  }

  public void putPlayerOnCell(Player p){
    if (p!=null){
      p.setCell(this);
    }
  }

  public String toString(){
    return new String("start cell");
  }
}

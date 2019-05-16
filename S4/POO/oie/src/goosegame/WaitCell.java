package goosegame;

public class WaitCell extends BasicCell{

  protected int duration;
  protected int time;
  /** Creates a WaitCell at the number index
  * @param index the number of the cell
  * @param duration the duration to wait
  */
  public WaitCell(int index, int duration){
    super(index);
    this.duration = duration;
    this.time = duration;
  }

  public boolean canBeLeft(){
    if (time == 0){
      return true;
    }
    else{
      time --;
      return false;
    }
  }

  public void putPlayerOnCell(Player p){
    time = duration;
    super.putPlayerOnCell(p);
  }

  public String toString(){
    return new String("cell "+index+" (waiting for "+duration+" turns)");
  }
}

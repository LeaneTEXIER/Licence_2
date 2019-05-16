package goosegame;

public class ClassicBoard extends Board{
  /** Create a ClassicBoard for the gooseGame
  */
  public ClassicBoard(){
    super(63+1);
  }

  /** init the Board */
  protected void initBoard(){
    for (int i=1; i<=63; i++){
      if ((i%9) == 0 && i!=63){
        this.theCells[i] = new GooseCell(i);
      }
      else{
        this.theCells[i] = new BasicCell(i);
      }
    }
    this.theCells[31] = new TrapCell(31);
    this.theCells[52] = new TrapCell(52);

    this.theCells[19] = new WaitCell(19,2);

    this.theCells[6] = new JumpCell(6,12);
    this.theCells[42] = new JumpCell(42,30);
    this.theCells[58] = new JumpCell(58,1);
  }
}

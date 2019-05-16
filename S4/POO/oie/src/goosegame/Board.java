package goosegame;

public abstract class Board{
  protected static int nbOfCells;
  protected Cell[] theCells;

  /** Create a Board
  * @param nbOfCells the number of cells
  */
  public Board(int nbOfCells){
    this.nbOfCells = nbOfCells;
    this.theCells = new Cell[nbOfCells];
    this.theCells[0] = new StartCell();
    initBoard();
  }

  /** init the Board */
  protected abstract void initBoard();

  /** Return the cell at the number index
  * @param index the index(=number) of the Cell
  * @return the cell at the number index
  */
  public Cell getCell(int index){
    return this.theCells[index];
  }

  /** Return the number of cells of the Board
  * @return the nb of cells of the Board
  */
  public int getNbOfCells(){
    return this.nbOfCells;
  }
}

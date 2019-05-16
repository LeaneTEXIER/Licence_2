package goosegame;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;


import goosegame.ClassicBoard;
import goosegame.Board;
import goosegame.Cell;
import goosegame.StartCell;
import goosegame.BasicCell;
import goosegame.GooseCell;

public class ClassicBoardTest{

  private Board board;

  @Before
  public  void before(){
    this.board = new ClassicBoard();
  }

  @Test
  public void createTest(){
    assertNotNull(board);
  }

  @Test
  public void getNbOfCellsTest(){
    assertSame(64, board.getNbOfCells());
  }

  @Test
  public void getCellAndinitBoard(){
    board.initBoard();
    assertNotNull(board.getCell(0));
    assertNotNull(board.getCell(9));
    assertNotNull(board.getCell(31));
    assertNotNull(board.getCell(63));
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(ClassicBoardTest.class);
    }
}

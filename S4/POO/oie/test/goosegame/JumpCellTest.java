package goosegame;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;


import goosegame.Cell;
import goosegame.BasicCell;
import goosegame.JumpCell;
import goosegame.Player;

public class JumpCellTest{

  private Cell cell1;
  private Cell cell2;
  private Player p;

  @Before
  public  void before(){
    this.cell1 = new JumpCell(2,28);
    this.cell2 = new JumpCell(5,21);
    this.p = new Player("toto", cell1);
  }

  @Test
  public void createTest(){
    assertNotNull(cell1);
  }

  @Test
  public void getIndexTest(){
    assertSame(2, cell1.getIndex());
    assertSame(5, cell2.getIndex());
  }

  @Test
  public void getPlayerAndputPlayerOnCellTest(){
    assertSame(null, cell2.getPlayer());
    cell2.putPlayerOnCell(p);
    assertSame(p, cell2.getPlayer());
  }

  @Test
  public void canBeLeftTest(){
    assertTrue(cell1.canBeLeft());
  }

  @Test
  public void isBusyTest(){
    assertFalse(cell1.isBusy());
    cell1.putPlayerOnCell(p);
    assertTrue(cell1.isBusy());
  }

  @Test
  public void handleMoveTest(){
    assertSame(cell1.handleMove(3),28);
    assertSame(cell1.handleMove(9),28);
    assertSame(cell2.handleMove(2),21);
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(JumpCellTest.class);
    }
}

package goosegame;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;


import goosegame.Cell;
import goosegame.BasicCell;
import goosegame.WaitCell;
import goosegame.Player;

public class WaitCellTest{

  private Cell cell1;
  private Cell cell2;
  private Player p;

  @Before
  public  void before(){
    this.cell1 = new WaitCell(2,2);
    this.cell2 = new WaitCell(5,1);
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
    assertFalse(cell1.canBeLeft());
    assertFalse(cell1.canBeLeft());
    assertTrue(cell1.canBeLeft());
    assertFalse(cell2.canBeLeft());
    assertTrue(cell2.canBeLeft());
  }

  @Test
  public void isBusyTest(){
    assertFalse(cell1.isBusy());
    cell1.putPlayerOnCell(p);
    assertTrue(cell1.isBusy());
  }

  @Test
  public void handleMoveTest(){
    assertSame(cell1.handleMove(3),2);
    assertSame(cell1.handleMove(9),2);
    assertSame(cell2.handleMove(2),5);
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(WaitCellTest.class);
    }
}

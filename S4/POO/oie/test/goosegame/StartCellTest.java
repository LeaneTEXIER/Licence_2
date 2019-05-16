package goosegame;

import org.junit.*;
import static org.junit.Assert.*;

import goosegame.Cell;
import goosegame.StartCell;
import goosegame.Player;

public class StartCellTest{

  private Cell cell1;
  private Cell cell2;
  private Player p;

  @Before
  public  void before(){
    this.cell1 = new StartCell();
    this.p = new Player("toto", cell1);
  }

  @Test
  public void createTest(){
    assertNotNull(cell1);
  }

  @Test
  public void getIndexTest(){
    assertSame(0, cell1.getIndex());
  }

  @Test
  public void getPlayerAndputPlayerOnCellTest(){
    assertSame(null, cell1.getPlayer());
    cell1.putPlayerOnCell(p);
    assertSame(null, cell1.getPlayer());
    assertSame(cell1, p.getCell());
  }

  @Test
  public void canBeLeftTest(){
    assertTrue(cell1.canBeLeft());
  }

  @Test
  public void isBusyTest(){
    assertFalse(cell1.isBusy());
    cell1.putPlayerOnCell(p);
    assertFalse(cell1.isBusy());
  }

  @Test
  public void handleMoveTest(){
    assertSame(cell1.handleMove(3),0);
    assertSame(cell1.handleMove(9),0);
  }

  public static junit.framework.Test suite(){
    return new junit.framework.JUnit4TestAdapter(StartCellTest.class);
  }
}

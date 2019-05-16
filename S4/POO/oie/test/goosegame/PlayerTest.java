package goosegame;

import org.junit.*;
import static org.junit.Assert.*;

import goosegame.Player;
import goosegame.Cell;
import goosegame.BasicCell;

public class PlayerTest{

  private Player p1;
  private Player p2;
  private Cell c1;
  private Cell c2;

  @Before
  public  void before(){
    this.c1 = new BasicCell(2);
    this.c1 = new BasicCell(29);
    this.p1 = new Player("toto", c1);
    this.p2 = new Player("biblio");
  }

  @Test
  public void createTest (){
      assertNotNull(p1);
      assertNotNull(p2);
  }

  @Test
  public void getCellandsetCellTest() {
    assertSame(c1, p1.getCell());
    assertSame(null, p2.getCell());
    p2.setCell(c1);
    assertSame(c1, p2.getCell());
    p2.setCell(c2);
    assertSame(c2, p2.getCell());
  }

  @Test
  public void twoDiceThrow() {
    int d = p1.twoDiceThrow();
    assertTrue (d>=2 && d<=12);
  }

  public static junit.framework.Test suite(){
    return new junit.framework.JUnit4TestAdapter(PlayerTest.class);
  }
}

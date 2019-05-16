import org.junit.*;
import static org.junit.Assert.*;

import prs.Player;
import prs.Shape;
import prs.Strategy;
import prs.strategies.*;

public class PlayerTest{
  private String name1;
  private String name2;
  private Strategy s1;
  private Strategy s2;
  private Player p1;
  private Player p2;


  @Before
  public void beforeTest(){
    name1 = "Leane";
    name2 = "Flo";
    s1 = new PaperStrat();
    s2 = new RockStrat();
    p1 = new Player(name1, s1);
    p2 = new Player(name2, s2);
  }

  @Test
  public void getNameTest(){
    assertEquals(name1, p1.getName());
    assertEquals(name2, p2.getName());
  }

  @Test
  public void getAndAddPointsTest(){
    assertEquals(0, p1.getPoints());
    p1.addPoints(2);
    assertEquals(2, p1.getPoints());
    p1.addPoints(1);
    assertEquals(3, p1.getPoints());
  }

  @Test
  public void getAndSetStrategyTest(){
    assertEquals(p1.getStrategy(),s1);
    assertEquals(Shape.PAPER, p1.play());
    p1.setStrategy(s2);
    assertEquals(p1.getStrategy(),s2);
    assertEquals(Shape.ROCK, p1.play());
  }

  @Test
  public void playTest(){
    assertEquals(Shape.PAPER, p1.play());
    assertEquals(Shape.ROCK, p2.play());
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(PlayerTest.class);
    }

}

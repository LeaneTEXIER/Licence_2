import org.junit.*;
import static org.junit.Assert.*;

import hanoi.*;
import hanoi.util.*;

public class HanoiTest{

  @Test
  public void testHanoiandgetCapacityandgettheTowers(){
    Hanoi h = new Hanoi(5);
    assertEquals(h.getCapacity(),5);
    assertTrue(h.gettheTowers()[0].isFull());
  }

  @Test
  public void testMoveOneDisc(){
    Hanoi h = new Hanoi(5);
    h.moveOneDisc(0,1);
    assertSame(h.gettheTowers()[1].top().compareTo(new Disc(1)), 0);
    assertSame(h.gettheTowers()[0].getnbDisc(),4);
  }

  @Test
  public void testMove(){
    Hanoi h = new Hanoi(5);
    h.move(5,0,2,1);
    assertTrue(h.gettheTowers()[1].isEmpty());
    assertTrue(h.gettheTowers()[0].isEmpty());
    assertTrue(h.gettheTowers()[2].isFull());
  }

  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(HanoiTest.class);
    }

}

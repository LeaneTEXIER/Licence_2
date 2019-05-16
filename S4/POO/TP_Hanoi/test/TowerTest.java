import org.junit.*;
import static org.junit.Assert.*;

import hanoi.util.*;

public class TowerTest{

  @Test
  public void testTower(){
    Tower t = new Tower(3);
    assertNotNull(t);
  }

  @Test
  public void testgetCapacity(){
    Tower t = new Tower(3);
    assertSame(t.getCapacity(),3);
  }

  @Test
  public void testgetnbDisc(){
    Tower t = new Tower(3);
    assertSame(t.getnbDisc(),0);
    t.push(new Disc(3));
    assertSame(t.getnbDisc(),1);
    t.push(new Disc(2));
    assertSame(t.getnbDisc(),2);
  }

  @Test
  public void testgetTheDiscs(){
    Tower t = new Tower(3);
    Disc d = new Disc(5);
    t.push(d);
    assertSame(t.getTheDiscs()[0],d);
  }

  @Test
  public void testpushOKAndtop(){
    Tower t = new Tower(3);
    Disc d = new Disc(5);
    t.push(d);
    assertSame(t.getnbDisc(),1);
    assertEquals(d, t.top());
    t.push(new Disc(3));
    assertSame(t.getnbDisc(),2);
  }

  @Test(expected = IllegalStateException.class)
  public void testpushKOFull(){
    Tower t = new Tower(3);
    t.push(new Disc(9));
    t.push(new Disc(7));
    t.push(new Disc(5));
    t.push(new Disc(3));
  }

  @Test(expected = IllegalStateException.class)
  public void testpushKOTooLargeDisc(){
    Tower t = new Tower(3);
    t.push(new Disc(9));
    t.push(new Disc(11));
  }

  @Test
  public void testpopOK(){
    Tower t = new Tower(3);
    Disc d = new Disc(9);
    t.push(d);
    assertSame(t.getnbDisc(), 1);
    assertSame(t.pop(),d);
    assertSame(t.getnbDisc(),0);
  }

  @Test (expected = IllegalStateException.class)
  public void testpopKO(){
    Tower t = new Tower(3);
    t.pop();
  }

  @Test
  public void testisEmpty(){
    Tower t = new Tower(3);
    assertTrue(t.isEmpty());
    t.push(new Disc(5));
    assertFalse(t.isEmpty());
  }

  @Test
  public void testisFull(){
    Tower t = new Tower(3);
    assertFalse(t.isFull());
    t.push(new Disc(5));
    t.push(new Disc(3));
    t.push(new Disc(2));
    assertTrue(t.isFull());
  }



  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(TowerTest.class);
    }

}

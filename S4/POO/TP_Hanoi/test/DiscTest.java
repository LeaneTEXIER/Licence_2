import org.junit.*;
import static org.junit.Assert.*;

import hanoi.util.Disc;

public class DiscTest{

  @Test
  public void testDisc(){
    Disc d = new Disc(3);
    assertNotNull(d);
  }

  @Test
  public void testgetSize(){
    Disc d = new Disc(5);
    assertSame(d.getSize(),5);
  }

  @Test
  public void testcompareTo(){
    Disc d1 = new Disc(5);
    Disc d2 = new Disc(5);
    Disc d3 = new Disc(7);
    assertSame(d1.compareTo(d2),0);
    assertSame(d1.compareTo(d3),-1);
    assertSame(d3.compareTo(d2),1);
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(DiscTest.class);
    }

}

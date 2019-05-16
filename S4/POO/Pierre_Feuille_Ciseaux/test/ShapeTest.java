import org.junit.*;
import static org.junit.Assert.*;

import prs.Shape;

public class ShapeTest{

  @Test
  public void compareShapeTest(){
    Shape sh1 = Shape.PAPER;
    Shape sh2 = Shape.SISSORS;
    Shape sh3 = Shape.ROCK;
    assertEquals(0, sh1.compareShape(sh1));
    assertEquals(-1, sh1.compareShape(sh2));
    assertEquals(1, sh1.compareShape(sh3));

    assertEquals(0, sh2.compareShape(sh2));
    assertEquals(-1, sh2.compareShape(sh3));
    assertEquals(1, sh2.compareShape(sh1));

    assertEquals(0, sh3.compareShape(sh3));
    assertEquals(-1, sh3.compareShape(sh1));
    assertEquals(1, sh3.compareShape(sh2));
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(ShapeTest.class);
    }

}

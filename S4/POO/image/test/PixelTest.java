import org.junit.*;
import static org.junit.Assert.*;

import image.Pixel;
import image.color.*;

public class PixelTest{

  @Test
  public void PixelTest(){
    Pixel p1 = new Pixel(GrayColor.WHITE);
    assertNotNull(p1);
  }

  @Test
  public void setAndGetColorTest(){
    Pixel p1 = new Pixel(GrayColor.WHITE);
    assertEquals(p1.getColor(), GrayColor.WHITE);
    p1.setColor(GrayColor.BLACK);
    assertEquals(p1.getColor(), GrayColor.BLACK);
  }

  @Test
  public void equalsTest(){
    Pixel p1 = new Pixel(GrayColor.WHITE);
    Pixel p2 = new Pixel(GrayColor.WHITE);
    Pixel p3 = new Pixel(GrayColor.BLACK);
    assertTrue(p1.equals(p2));
    assertFalse(p1.equals(p3));
    assertFalse(p1.equals(255));
  }

  @Test
  public void colorLevelDifferencetest(){
    Pixel p1 = new Pixel(new GrayColor(125));
    Pixel p2 = new Pixel(new GrayColor(125));
    Pixel p3 = new Pixel(new GrayColor(25));
    assertEquals(0, p1.colorLevelDifference(p2));
    assertEquals(100, p1.colorLevelDifference(p3));

  }

  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(PixelTest.class);
    }

}

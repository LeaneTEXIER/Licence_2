import org.junit.*;
import static org.junit.Assert.*;

import image.color.*;

public class GrayColorTest{

  @Test
  public void getGrayLevelTest(){
    GrayColor color = new GrayColor(125);
    assertEquals(color.getGrayLevel(),125);
  }

  @Test
  public void equalsTest(){
    GrayColor color1 = new GrayColor(125);
    GrayColor color2 = new GrayColor(125);
    GrayColor color3 = new GrayColor(25);
    assertTrue(color1.equals(color2));
    assertFalse(color1.equals(color3));
    assertFalse(color1.equals(125));
  }

  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(GrayColorTest.class);
    }

}

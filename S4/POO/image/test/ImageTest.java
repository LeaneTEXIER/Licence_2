import org.junit.*;
import static org.junit.Assert.*;

import image.*;
import image.color.*;

public class ImageTest{

  @Test
  public void ImageTest(){
    Image im =  new Image(150, 120);
    Pixel blanc  = new Pixel(GrayColor.WHITE);
    for (int x=0; x<150; x++){
      for (int y=0; y<120; y++){
        assertTrue((im.getPixel(x,y).equals(blanc)));
      }
    }
  }

  @Test
  public void getHeightTest() {
    Image im1 =  new Image(150, 120);
    Image im2 =  new Image(250, 200);
    assertEquals(120,im1.getHeight());
    assertEquals(200,im2.getHeight());
  }

  @Test
  public void getWidthTest() {
    Image im1 =  new Image(150, 120);
    Image im2 =  new Image(250, 200);
    assertEquals(150,im1.getWidth());
    assertEquals(250,im2.getWidth());
  }

  @Test
  public void getandsetPixelTestOK() {
    Image im = new Image(150, 120);
    Pixel p1 = new Pixel(GrayColor.WHITE);
    Pixel p2 = new Pixel(new GrayColor(50));
    assertTrue(p1.equals(im.getPixel(100, 100)));
    im.setPixel(100, 100, p2);
    assertTrue(p2.equals(im.getPixel(100, 100)));
    assertFalse(p1.equals(im.getPixel(100, 100)));
    assertFalse(p2.equals(im.getPixel(10, 10)));
  }

  @Test(expected = UnknownPixelException.class)
  public void getPixelTestKO() {
    Image im = new Image(150, 120);
    im.getPixel(160,121);
  }

  @Test(expected = UnknownPixelException.class)
  public void setPixelTestKO() {
    Image im = new Image(150, 120);
    Pixel p = new Pixel(new GrayColor(30));
    im.setPixel(151, 100, p);
  }

  @Test
  public void changeColorPixelTestOK(){
    Image im = new Image(150, 120);
    GrayColor color = new GrayColor(50);
    assertTrue(GrayColor.WHITE.equals(im.getPixel(100,100).getColor()));
    assertTrue(GrayColor.WHITE.equals(im.getPixel(10,10).getColor()));
    im.changeColorPixel(100, 100, color);
    assertFalse(GrayColor.WHITE.equals(im.getPixel(100,100).getColor()));
    assertTrue(GrayColor.WHITE.equals(im.getPixel(10,10).getColor()));
    assertTrue(color.equals(im.getPixel(100,100).getColor()));
    assertFalse(color.equals(im.getPixel(10,10).getColor()));
  }

  @Test (expected = UnknownPixelException.class)
  public void changeColorPixelTestKO(){
    Image im = new Image(150, 120);
    GrayColor color = new GrayColor(50);
    im.changeColorPixel(153, 53, color);
  }


  public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(ImageTest.class);
    }

}

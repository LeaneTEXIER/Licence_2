import org.junit.*;
import static org.junit.Assert.*;

import example.Robot;
import example.util.*;

public class RobotTest {

    @Test
    public void testTake(){
      Robot Robbie=new Robot();
      Box someBox = new Box(10);
      Robbie.take(someBox);
      assertSame(someBox,Robbie.getCarriedBox());
      Box someBox2 = new Box(20);
      Robbie.take(someBox2);
      assertSame(someBox,Robbie.getCarriedBox());
    }

    @Test
    public void TestcarryBox(){
      Robot Robbie=new Robot();
      assertFalse(Robbie.carryBox());
      Box someBox = new Box(10);
      Robbie.take(someBox);
      assertTrue(Robbie.carryBox());
    }



    @Test
    public void TestputOnBoxOk(){
      // Test quand la boite est posée sur le tapis
      Robot Robbie=new Robot();
      Box someBox = new Box(9);
      ConveyerBelt belt1 = new ConveyerBelt(10);
      Robbie.take(someBox);
      Robbie.putOn(belt1);
      assertFalse(Robbie.carryBox());
    }

    @Test
    public void TestputOnNoBox(){
      // Test quand le robot ne porte pas de boite
      Robot Robbie=new Robot();
      ConveyerBelt belt1 = new ConveyerBelt(10);
      Robbie.putOn(belt1);
      assertFalse(Robbie.carryBox());
    }

    @Test
    public void TestputOnBoxHeavy(){
      // Test quand la boite est trop lourde pour etre posée
      Robot Robbie=new Robot();
      Box someBox = new Box(15);
      ConveyerBelt belt1 = new ConveyerBelt(10);
      Robbie.take(someBox);
      Robbie.putOn(belt1);
      assertTrue(Robbie.carryBox());
      assertSame(someBox,Robbie.getCarriedBox());
    }

    @Test
    public void TestputOnBeltFull(){
      // Test quand le tapis ne peut plus prendre de caisses (cad quand il y a deja 2 caisses sur le tapis)
      Robot Robbie=new Robot();
      Box someBox = new Box(9);
      ConveyerBelt belt1 = new ConveyerBelt(10);
      Robbie.take(someBox);
      Robbie.putOn(belt1);
      Robbie.take(someBox);
      Robbie.putOn(belt1);
      assertFalse(Robbie.carryBox());
      Robbie.take(someBox);
      Robbie.putOn(belt1);
      assertTrue(Robbie.carryBox());
    }


    // ---Pour permettre l'exécution des test----------------------
    public static junit.framework.Test suite() {
        return new junit.framework.JUnit4TestAdapter(RobotTest.class);
    }

}

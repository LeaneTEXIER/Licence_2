package rental;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import rental.Vehicle;

public class MotorBikeTest {

	private MotorBike m1;
	private MotorBike m2;

	@Before
	public void before() {
		m1 = new MotorBike("brand1","model1",2015,100.0f, 750);
		m2 = new MotorBike("brand2","model2",2000,200.0f, 1400);
	}

  @Test
  public void createTest(){
    assertNotNull(m1);
    assertNotNull(m2);
  }

  @Test
  public void getCylindreeTest(){
    assertEquals(750, m1.getCylindree());
    assertEquals(1400, m2.getCylindree());
  }

    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
	return new junit.framework.JUnit4TestAdapter(rental.MotorBikeTest.class);
    }

}

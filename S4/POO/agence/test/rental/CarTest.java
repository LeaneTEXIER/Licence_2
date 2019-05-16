package rental;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import rental.Vehicle;

public class CarTest {

	private Car c1;
	private Car c2;

	@Before
	public void before() {
		c1 = new Car("brand1","model1",2015,100.0f, 2);
		c2 = new Car("brand2","model2",2000,200.0f, 5);
	}

  @Test
  public void createTest(){
    assertNotNull(c1);
    assertNotNull(c2);
  }

  @Test
  public void getNbpassagersTest(){
    assertEquals(2, c1.getNbpassagers());
    assertEquals(5, c2.getNbpassagers());
  }

    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
	return new junit.framework.JUnit4TestAdapter(rental.CarTest.class);
    }

}

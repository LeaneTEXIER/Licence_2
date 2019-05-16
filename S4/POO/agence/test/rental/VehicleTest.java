package rental;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class VehicleTest {
 
	private Vehicle v1;
	private Vehicle v2;

	
	@Before 
	public void before() {
		this.v1 = new Vehicle("brand1","model1",2015,100.0f);
		this.v2 = new Vehicle("brand2","model2",2000,200.0f);
	}

	@Test
	public void createTest() {
		assertNotNull(this.v1);
	}
	
	@Test
	public void testGetBrand() {
		assertEquals("brand1",this.v1.getBrand());
		assertEquals("brand2",this.v2.getBrand());
	}

	@Test
	public void testGetModel() {
		assertEquals("model1",this.v1.getModel());
		assertEquals("model2",this.v2.getModel());
	}

	@Test
	public void testGetDailyPrice() {
	    assertEquals(100.0f,this.v1.getDailyPrice(),0.0001);
	    assertEquals(200.0f,this.v2.getDailyPrice(),0.0001);
	}

	@Test
	public void testGetProductionYear() {
	    assertEquals(2015,this.v1.getProductionYear());
	    assertEquals(2000,this.v2.getProductionYear());
	}

	@Test
	public void testEquals() {
		Vehicle v3 = new Vehicle("brand1","model1",2015,100.0f);
		Vehicle v4 = new Vehicle("brand1","model1",2015,200.0f);
		assertTrue(v1.equals(v3));
		assertFalse(v1.equals(v2));
		assertFalse(v1.equals(v4));
		assertFalse(v1.equals(new Object()));
	}

    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
	return new junit.framework.JUnit4TestAdapter(rental.VehicleTest.class);
    }

}

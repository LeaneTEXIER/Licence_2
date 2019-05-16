package rental;

import static org.junit.Assert.*;

import org.junit.Test;

public class PriceCriterionTest {

	@Test
	public void testPriceCriterion() {
		assertNotNull(new PriceCriterion(100));
	}

	@Test
	public void testIsSatisfiedBy() {
		PriceCriterion criterion = new PriceCriterion(150);
		Vehicle v1 = new Vehicle("brand1","model1",2015,100);
		Vehicle v2 = new Vehicle("brand2","model2",2000,200);
		assertTrue(criterion.isSatisfiedBy(v1));
		assertFalse(criterion.isSatisfiedBy(v2));
	}
    
    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
	return new junit.framework.JUnit4TestAdapter(rental.PriceCriterionTest.class);
    }

}

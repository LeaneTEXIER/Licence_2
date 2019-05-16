package rental;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import rental.*;
import rental.BrandCriterion;
import rental.PriceCriterion;

public class InterCriterionTest {

  private Vehicle v1;
  private Vehicle v2;
  private Criterion c1;
  private Criterion c2;
  private Criterion c3;
  private InterCriterion criterions;
  private InterCriterion criterions2;

  @Before
  public void before(){
    v1 = new Vehicle ("brand1","model1",2015,100);
		v2 = new Vehicle("brand2","model2",2000,200);
    c1 = new PriceCriterion (120);
    c2 = new BrandCriterion ("brand2");
    c3 = new BrandCriterion ("brand1");
    criterions = new InterCriterion();
    criterions2 = new InterCriterion();
  }

  @Test
  public void createTest(){
    assertNotNull(new InterCriterion());
  }

  @Test
  public void addCriterionAndisSatisfiedByTest1(){
    criterions.addCriterion(c1);
    assertTrue(criterions.isSatisfiedBy(v1));
    assertFalse(criterions.isSatisfiedBy(v2));
    criterions.addCriterion(c2);
    assertFalse(criterions.isSatisfiedBy(v1));
    assertFalse(criterions.isSatisfiedBy(v2));
  }

  @Test
  public void addCriterionAndisSatisfiedByTest2(){
    criterions2.addCriterion(c1);
    assertTrue(criterions2.isSatisfiedBy(v1));
    assertFalse(criterions2.isSatisfiedBy(v2));
    criterions2.addCriterion(c3);
    assertTrue(criterions2.isSatisfiedBy(v1));
    assertFalse(criterions2.isSatisfiedBy(v2));
  }

    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
      return new junit.framework.JUnit4TestAdapter(rental.InterCriterionTest.class);
    }
}

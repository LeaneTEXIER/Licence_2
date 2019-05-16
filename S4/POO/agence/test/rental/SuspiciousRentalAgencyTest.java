package rental;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import rental.*;

public class SuspiciousRentalAgencyTest {
  private Vehicle v1;
  private Vehicle v2;
  private Client c1;
  private Client c2;
  public SuspiciousRentalAgency a;


  @Before
  public void before(){
    v1 = new Vehicle ("brand1","model1",2015,100F);
		v2 = new Vehicle("brand2","model2",2000,100F);
    a = new SuspiciousRentalAgency();
    c1 = new Client("Léane", 20);
    c2 = new Client("Flo", 27);
  }

  @Test
  public void createTest(){
    assertNotNull(this.a);
  }

  @Test
  public void rentVehicleTest(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    assertTrue((a.rentVehicle(c1,v1))==110F);
    assertTrue((a.rentVehicle(c2,v2))==100F);
  }

    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
      return new junit.framework.JUnit4TestAdapter(SuspiciousRentalAgencyTest.class);
    }
}

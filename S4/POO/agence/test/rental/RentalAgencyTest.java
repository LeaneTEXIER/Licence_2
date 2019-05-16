package rental;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import rental.*;

public class RentalAgencyTest {
  private Vehicle v1;
  private Vehicle v2;
  private Client c1;
  private Client c2;
  public RentalAgency a;


  @Before
  public void before(){
    v1 = new Vehicle ("brand1","model1",2015,100);
		v2 = new Vehicle("brand2","model2",2000,200);
    a = new RentalAgency();
    c1 = new Client("Léane", 20);
    c2 = new Client("Flo", 21);
  }

  @Test
  public void createTest(){
    assertNotNull(new RentalAgency());
  }

  @Test
  public void addVehicleAndgetVehiclesTest(){
    a.addVehicle(v1);
    assertEquals(v1,a.getVehicles().get(0));
    a.addVehicle(v2);
    assertEquals(v1,a.getVehicles().get(0));
    assertEquals(v2,a.getVehicles().get(1));
  }

  @Test
  public void selectTest(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    Criterion crit = new BrandCriterion("brand1");
    assertTrue(a.select(crit).get(0).equals(v1));
  }

  @Test
  public void rentVehicleTestAndgetRentedVehiclesOK(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    a.rentVehicle(c1,v1);
    assertEquals(v1,a.getRentedVehicles().get(c1));
  }

  @Test (expected = UnknownVehicleException.class)
  public void rentVehicleTestKO1(){
    a.addVehicle(v1);
    a.rentVehicle(c1, v2);
  }

  @Test (expected = IllegalStateException.class)
  public void rentVehicleTestKO2(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    a.rentVehicle(c1, v1);
    a.rentVehicle(c1, v2);
  }

  @Test (expected = IllegalStateException.class)
  public void rentVehicleTestKO3(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    a.rentVehicle(c1, v1);
    a.rentVehicle(c2, v1);
  }

  @Test
  public void hasRentedAVehicleTest(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    a.rentVehicle(c1,v1);
    assertTrue(a.hasRentedAVehicle(c1));
    assertFalse(a.hasRentedAVehicle(c2));
  }

  @Test
  public void isRentedTest(){
    a.addVehicle(v1);
    a.addVehicle(v2);
    a.rentVehicle(c1,v1);
    assertTrue(a.isRented(v1));
    assertFalse(a.isRented(v2));
  }


  public void returnVehicleTest(Client client){
    a.rentVehicle(c1,v1);
    assertTrue(a.hasRentedAVehicle(c1));
    a.returnVehicle(c1);
    assertFalse(a.hasRentedAVehicle(c1));
  }


    // ---Pour permettre l'execution des tests ----------------------
    public static junit.framework.Test suite() {
      return new junit.framework.JUnit4TestAdapter(rental.RentalAgencyTest.class);
    }
}

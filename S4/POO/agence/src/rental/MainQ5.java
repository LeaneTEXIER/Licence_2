package rental;

import java.util.*;
import rental.*;

/** main to test for question  Q5 */
public class MainQ5 {

    public static void main(String[] args) {
      RentalAgency agency = new RentalAgency();
      Vehicle v1 = new Vehicle("brand1","model1",2012,100);
      agency.addVehicle(v1);
      Vehicle v2 = new Vehicle("brand1","model2",2015,150);
      agency.addVehicle(v2);
      Vehicle v3 = new Vehicle("brand2","model3",2016,200);
      agency.addVehicle(v3);
      Car c1 = new Car("brand1","model11",2011,110,5);
      agency.addVehicle(c1);
      Car c2 = new Car("brand2","model21",2006,170,2);
      agency.addVehicle(c2);
      Car c3 = new Car("brand3","model31",2014,120,7);
      agency.addVehicle(c3);
      MotorBike m1 = new MotorBike("brand1","model13",2008,123,750);
      agency.addVehicle(m1);
      MotorBike m2 = new MotorBike("brand4","model23",2004,80,1400);
      agency.addVehicle(m2);
      MotorBike m3 = new MotorBike("brand5","model33",2012,133,1250);
      agency.addVehicle(m3);
      Criterion crit = new PriceCriterion(130);
      System.out.println("RentalAgency: ");
      System.out.println("Selection des véhicules d'une agence suivant son prix (inférieur à 130):");
      agency.displaySelection(crit);
    }
}

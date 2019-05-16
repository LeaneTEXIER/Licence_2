package rental;

import java.util.*;
import rental.*;

/** main to test for question  Q7 */
public class MainQ7 {

    public static void main(String[] args) {
      SuspiciousRentalAgency agency = new SuspiciousRentalAgency();
      Vehicle v = new Vehicle("brand1","model1",2012,100);
      agency.addVehicle(v);
      Car c = new Car("brand1","model11",2011,150,5);
      agency.addVehicle(c);
      MotorBike m = new MotorBike("brand1","model13",2008,200,750);
      agency.addVehicle(m);
      Client client1 =  new Client("Flo", 27);
      Client client2 =  new Client("Leane", 20);
      System.out.println("SuspiciousRentalAgency:");
      System.out.println("Location d'un Vehicle a initialement un prix de 100:");
      System.out.println("Client de 27 ans:" + agency.rentVehicle(client1,v));
      agency.returnVehicle(client1);
      System.out.println("Client de 20 ans:" + agency.rentVehicle(client2,v));
      agency.returnVehicle(client2);
      System.out.println("Location d'un Car a initialement un prix de 150:");
      System.out.println("Client de 27 ans:" + agency.rentVehicle(client1,c));
      agency.returnVehicle(client1);
      System.out.println("Client de 20 ans:" + agency.rentVehicle(client2,c));
      agency.returnVehicle(client2);
      System.out.println("Location d'un MotorBike a initialement un prix de 200:");
      System.out.println("Client de 27 ans:" + agency.rentVehicle(client1,m));
      agency.returnVehicle(client1);
      System.out.println("Client de 20 ans:" + agency.rentVehicle(client2,m));
      agency.returnVehicle(client2);
    }
}

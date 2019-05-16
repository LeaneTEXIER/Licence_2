package rental;

import java.util.*;
import rental.Vehicle;
import rental.UnknownVehicleException;
import rental.IllegalStateException;


/** a rental vehicle agency, client can rent one vehicle at a time */
public class RentalAgency {
    // vehicles of this agency
    private List<Vehicle> theVehicles;

    // maps client and rented vehicle (at most one vehicle by client)
    private Map<Client,Vehicle> rentedVehicles;

    public RentalAgency() {
      this.theVehicles = new ArrayList<Vehicle>();
    	this.rentedVehicles = new HashMap <Client,Vehicle>();
    }

    /** returns the list of the vehicles of the agency
    * @return list of the vehicles not rented
    */
    public List<Vehicle> getVehicles(){
      return this.theVehicles;
    }

    /** returns the map of the rented vehicles of the agency
    * @return map of the rented vehicles
    */
    public Map<Client,Vehicle> getRentedVehicles(){
      return this.rentedVehicles;
    }

    /** adds a vehicle to this agency
    * @param v the added vehicle
    */
    public void addVehicle(Vehicle v) {
    	this.theVehicles.add(v);
    }

    /** provides the list of the vehicles that satisfy the criterion c
    * @param c the selection criterion
    * @return  the list of the vehicles that satisfy the criterion c
    */
    public List<Vehicle> select(Criterion c) {
      List <Vehicle> res = new ArrayList<Vehicle>();
      for (Vehicle v: this.theVehicles){
        if (c.isSatisfiedBy(v)){
          res.add(v);
        }
      }
      return res;
    }


    /** displays the vehicles that satisfy the criterion c
    * @param c the selection criterion
    */
    public void displaySelection(Criterion c) {
      for (Vehicle v: this.theVehicles){
        if (c.isSatisfiedBy(v)){
          System.out.println(v.toString());
        }
      }
    }

    /** client rents a vehicle
    * @param client the renter
    * @param v the rented vehicle
    * @return the daily rental price
    * @exception UnknownVehicleException   if v is not a vehicle of this agency
    * @exception IllegalStateException if v is already rented or client rents already another vehicle
    */
    public float rentVehicle(Client client, Vehicle v) throws UnknownVehicleException, IllegalStateException {
    	if (this.theVehicles.contains(v)==false){
        throw new UnknownVehicleException();
      }
      else if (this.isRented(v) || this.hasRentedAVehicle(client)){
        throw new IllegalStateException();
      }
      else{
        this.rentedVehicles.put(client, v);
        return v.getDailyPrice();
      }
    }

    /** returns <em>true</em> iff client c is renting a vehicle
    * @param client the client to see if he has rented a vehicle
    * @return <em>true</em> iff client c is renting a vehicle
    */
    public boolean hasRentedAVehicle(Client client){
      for (Client c : this.rentedVehicles.keySet()){
        if (c.equals(client)){
          return true;
        }
      }
      return false;
    }

    /** returns <em>true</em> iff vehicle v is rented
    * @param v the vehicle to see if it is rented
    * @return <em>true</em> iff vehicle v is rented
    */
    public boolean isRented(Vehicle v){
      if (rentedVehicles.containsValue(v)){
        return true;
      }
      else{
        return false;
      }
    }

    /** the client returns a rented vehicle. Nothing happens if client didn't have rented a vehicle.
    * @param client the client who returns a vehicle
    */
    public void returnVehicle(Client client){
      if (this.hasRentedAVehicle(client)){
        this.rentedVehicles.remove(client);
      }
    }

    /** provides the collection of rented vehicles for this agency
    * @return collection of currently rented vehicles
    */
    public Collection<Vehicle> allRentedVehicles(){
      return this.rentedVehicles.values();
    }

}

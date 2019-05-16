package rental;

import rental.RentalAgency;
import rental.Vehicle;

public class SuspiciousRentalAgency extends RentalAgency{
  private float surcout;

  public SuspiciousRentalAgency(){
    this.surcout = 0.1F;
  }

  public float getSurcout(){
    return this.surcout;
  }

  /** client rents a vehicle
  * @param client the renter
  * @param v the rented vehicle
  * @return the daily rental price (with a surcout if the client is under 25 years)
  * @exception UnknownVehicleException   if v is not a vehicle of this agency
  * @exception IllegalStateException if v is already rented or client rents already another vehicle
  */
  public float rentVehicle(Client client, Vehicle v) throws UnknownVehicleException, IllegalStateException {
    super.rentVehicle(client, v);
    if (client.getAge()>25){
      return v.getDailyPrice();
    }
    else{
      return (v.getDailyPrice()*(1+surcout));
    }  
  }
}

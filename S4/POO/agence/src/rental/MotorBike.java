package rental;

import rental.Vehicle;

public class MotorBike extends Vehicle{
  private int cylindree;

  /**
	 * creates a car with given informations
	 *
	 * @param brand
	 *            the vehicle's brand
	 * @param model
	 *            the vehicle's model
	 * @param productionYear
	 *            the vehicle's production year
	 * @param dailyRentalPRice
	 *            the daily rental price
   * @param cylindree
	 *            the engine size (in cm^3)
  */
  public MotorBike(String brand, String model, int productionYear, float dailyRentalPRice, int cylindree){
    super(brand, model, productionYear, dailyRentalPRice);
    this.cylindree = cylindree;
  }

  /**
	 * @return the engine size (in cm^3) for this vehicle
	 */
  public int getCylindree(){
    return this.cylindree;
  }

  public String toString(){
    return super.toString() + " " + this.cylindree;
  }
}

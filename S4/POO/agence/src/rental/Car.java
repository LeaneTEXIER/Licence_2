package rental;

import rental.Vehicle;

public class Car extends Vehicle{
  private int nbPassengers;

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
   * @param nbPassengers
	 *            the number of passengers
  */
  public Car(String brand, String model, int productionYear, float dailyRentalPRice, int nbPassengers){
    super(brand, model, productionYear, dailyRentalPRice);
    this.nbPassengers = nbPassengers;
  }

  /**
	 * @return the capacity of number of passengers for this vehicle
	 */
  public int getNbpassagers(){
    return this.nbPassengers;
  }

  public String toString(){
    return super.toString() + " " + this.nbPassengers;
  }
}

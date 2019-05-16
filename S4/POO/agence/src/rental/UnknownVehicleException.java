package rental;

/**
* Exception UnknownVehicle
*
* @author Leane Texier
* @version 1.0
*/
public class UnknownVehicleException extends RuntimeException{
  public UnknownVehicleException(){
  }

  public UnknownVehicleException(String msg){
    super(msg);
  }
}

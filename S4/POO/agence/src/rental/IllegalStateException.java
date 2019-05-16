package rental;

/**
* Exception IllegalState
*
* @author Leane Texier
* @version 1.0
*/
public class IllegalStateException extends RuntimeException{
  public IllegalStateException(){
  }

  public IllegalStateException(String msg){
    super(msg);
  }
}

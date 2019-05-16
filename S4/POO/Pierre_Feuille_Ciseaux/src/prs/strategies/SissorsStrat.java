package prs.strategies;
import prs.Strategy;
import prs.Shape;


public class SissorsStrat implements Strategy{
  private String strat;

  public SissorsStrat(){
    this.strat = "SissorsStrat";
  }

  public Shape chooseShape(){
    return Shape.SISSORS;
  }
}

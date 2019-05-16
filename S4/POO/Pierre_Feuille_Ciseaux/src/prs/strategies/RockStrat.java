package prs.strategies;
import prs.Strategy;
import prs.Shape;


public class RockStrat implements Strategy{
  private String strat;

  public RockStrat(){
    this.strat = "RockStrat";
  }

  public Shape chooseShape(){
    return Shape.ROCK;
  }
}

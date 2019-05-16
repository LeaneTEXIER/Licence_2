package prs.strategies;
import prs.Strategy;
import prs.Shape;


public class RandomStrat implements Strategy{
  private String strat;

  public RandomStrat(){
    this.strat = "SissorsRandom";
  }

  public Shape chooseShape(){
    int n = (int) (Math.random()*3);
    return Shape.values()[n];
  }
}

package prs.strategies;

import prs.Strategy;
import prs.Shape;


public class PaperStrat implements Strategy{
  private String strat;

  public PaperStrat(){
    this.strat = "PaperStrat";
  }

  public Shape chooseShape(){
    return Shape.PAPER;
  }
}

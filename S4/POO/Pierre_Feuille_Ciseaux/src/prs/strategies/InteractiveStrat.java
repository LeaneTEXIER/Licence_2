package prs.strategies;
import prs.Strategy;
import prs.Shape;
import util.*;


public class InteractiveStrat implements Strategy{
  private String strat;

  public InteractiveStrat(){
    this.strat = "InteractiveStrat";
  }

  public Shape chooseShape(){
    Shape c = null;
    while (c == null){
      System.out.println("Choose a shape(ROCK, PAPER, SISSORS):");
      String answer = Input.readString();
      try{
        c = Shape.valueOf(answer.toUpperCase());
      }catch (IllegalArgumentException e){
        System.out.println("Shape invalide");
        c = null;
      }
    }
    return c;
  }
}

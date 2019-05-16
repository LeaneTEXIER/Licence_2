package prs;
import prs.Strategy;


public class Player{
  private String name;
  private int points;
  private Strategy myStrategy;

  /**Creates a player
   * @param name the name of the player
   * @param myStrategy the player's strategy
   */
  public Player (String name, Strategy myStrategy){
    this.points = 0;
    this.name = name;
    this.myStrategy = myStrategy;
  }

  /**Gives the name of the player
  * @return the name of the player
  */
  public String getName(){
    return this.name;
  }

  /**Gives the points of the player
  * @return the points of the player
  */
  public int getPoints(){
    return this.points;
  }

  /**Gives the strategy of the player
  * @return the strategy of the player
  */
  public Strategy getStrategy(){
    return this.myStrategy;
  }

  /**Sets a strategy to the player
  * @param s the strategy to set to the player
  */
  public void setStrategy(Strategy s){
    this.myStrategy = s;
  }

  /** Adds points to the player
  * @param p the number of points to add
  */
  public void addPoints(int p){
    this.points += p;
  }

  /** Returns "Player" and the name of the player
  * @return The name of the player
  */
  public String toString(){
    return "Player "+this.name;
  }

  /** The player chooses a Shape
  * @return the shape chosen
  */
  public Shape play(){
    return this.myStrategy.chooseShape();
  }
}

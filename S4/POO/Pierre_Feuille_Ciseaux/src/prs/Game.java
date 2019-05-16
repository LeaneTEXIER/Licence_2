package prs;
import prs.Player;
import prs.Strategy;
import prs.strategies.InteractiveStrat;


public class Game{
  private Player p1;
  private Player p2;
  private final int victory_points = 2;
  private final int defeat_points = 0;
  private final int tie_points = 1;
  private int nb_tours;


  /** Creates a game
  * @param p1 the first player
  * @param p2 the second player
  * @param nb_tours  the number of tours
  */
  public Game(Player p1 , Player p2, int nb_tours){
    this.nb_tours = nb_tours;
    this.p1 = p1;
    this.p2 = p2;
  }


    /** Plays the game
     */
  public void playGame(){
    for (int i=0; i<this.nb_tours; i++){
      this.playOneRound();
    }
    this.endOfGame();
  }

  /** Displays who wins at the end
   */
  public void endOfGame(){
    int score1 = this.p1.getPoints();
    int score2 = this.p2.getPoints();
    if (score1 > score2){
      System.out.println(this.p1.toString()+" wins the game");
    }
    else if (score1 < score2){
      System.out.println(this.p2.toString()+" wins the game");
    }
    else{
      System.out.println("Tie game (Nobody wins the game)");
    }
  }

  /** Gives points
   * @param income result of the tour
   */
  public void givePoints(int income){
    if (income == 0){
      this.p1.addPoints(this.tie_points);
      this.p2.addPoints(this.tie_points);
      System.out.println("Tie game");
    }
    else if (income < 0){
      this.p1.addPoints(this.defeat_points);
      this.p2.addPoints(this.victory_points);
      System.out.println(this.p2.toString()+" wins");
    }
    else{
      this.p1.addPoints(this.victory_points);
      this.p2.addPoints(this.defeat_points);
      System.out.println(this.p1.toString()+" wins");
    }
  }

  /** Plays one round of the game and add the points to the players
  */
  public void playOneRound(){
    Shape c1 = this.p1.play();
    Shape c2 = this.p2.play();
    System.out.println(this.p1.toString()+" plays "+c1);
    System.out.println(this.p2.toString()+" plays "+c2);
    int income = c1.compareShape(c2);
    this.givePoints(income);
  }
}

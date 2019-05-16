package goosegame;

import java.util.*;
import goosegame.*;

public class Game {
  protected List<Player> thePlayers;
  protected Board board;

  /** Create a Game
  * @param board the board of the Game
  */
  public Game(Board board){
    this.thePlayers = new ArrayList<Player>();
    this.board = board;
  }

  /** Add a player in the Game
  * @param p the player to add
  */
  public void addPlayer(Player p){
    thePlayers.add(p);
  }

  /** Move a player
  * @param p the player to move
  * @param currentCell the currentCell of the player p
  * @param reachedCell the reachedCell of the player p
  */
  public void movePlayer(Player p, Cell currentCell, Cell reachedCell){
    if (reachedCell.isBusy()){
      Player other = reachedCell.getPlayer();
      if (p!=other){
        System.out.println("... cell is busy, "+other.toString()+" is sent to "+currentCell.toString()+"\n");
        currentCell.putPlayerOnCell(other);
      }
      else{
        System.out.println("");
      }
    }
    else{
      System.out.println("");
      currentCell.putPlayerOnCell(null);
    }
    reachedCell.putPlayerOnCell(p);
  }


  /** Play the gooseGame
  */
  public void play(){
    boolean won = false;
    Player p = this.thePlayers.get(0);
    int i = 0; /*Pour parcourir liste des joueurs */
    int nb = this.board.getNbOfCells()-1; /* Nombre de cellules du plateau de jeu sans celle de départ*/
    Cell currentCell, nextCell;
    int currentIndex, nextIndex, d;
    String res = ""; /*Phrase pour afficher le coup du joueur*/
    while (!won){
      p = this.thePlayers.get((i++)%this.thePlayers.size());
      currentCell = p.getCell();
      currentIndex = currentCell.getIndex();
      res += p.toString() +" is in cell "+ currentIndex+", ";
      if (currentCell.canBeLeft()){
        d = p.twoDiceThrow();
        res += p.toString()+" throws "+d;
        nextIndex = currentIndex + d;
        if (nextIndex>nb){
          nextIndex = nb-(nextIndex-nb);
        }
        nextCell = this.board.getCell(nextIndex);
        res += " and reaches "+ nextCell.toString();
        nextIndex = nextCell.handleMove(d);
        if (nextIndex>nb){
          nextIndex = nb-(nextIndex-nb);
        }
        if ((nextCell instanceof GooseCell) || (nextCell instanceof JumpCell)){
          nextCell = this.board.getCell(nextIndex);
          res += " and jumps to "+nextCell.toString();
        }
        System.out.println(res+".");
        res ="";
        movePlayer(p, currentCell, nextCell);
        won = (nextIndex == nb);
      }
      else{
        res += p.toString()+" cannot play.";
        System.out.println(res+"\n");
        res ="";
      }
    }
    System.out.println(p.toString()+" has won.\n");
  }


}

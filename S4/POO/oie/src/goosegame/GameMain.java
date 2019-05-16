package goosegame;

import goosegame.*;

public class GameMain{
    public static void main(String[] args){
      ClassicBoard plateau= new ClassicBoard();
      Game game = new Game(plateau);
      int nb = Integer.parseInt(args[0]);
      for (int i=1; i<=nb; i++){
        game.addPlayer(new Player("Player"+i, plateau.getCell(0)));
      }
      game.play();
    }
}

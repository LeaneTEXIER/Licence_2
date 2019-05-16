package prs;
import prs.*;
import prs.strategies.*;
import util.*;


public class Main{
  public static void main(String[] args){
    Input in = new Input();
    int nb_tours;
    Strategy s1, s2;
    nb_tours = 0;
    while (nb_tours<=0){
      System.out.println("Indiquez le nombre de tours (Nombre positif):");
      try{
        nb_tours = in.readInt();
      } catch (java.io.IOException e){
        nb_tours = 0;
        System.out.println("Nombre de tours incorrect");
      }
    }
    System.out.println('\n');
    System.out.println("Stratégies possibles: PAPERSTRAT, ROCKSTRAT, SISSORSSTRAT, INTERACTIVESTRAT, RANDOMSTRAT");
    System.out.println("Nom du premier joueur:");
    String p1 = in.readString();
    boolean test = false;
    s1 = new RandomStrat();
    while (!test){
      System.out.println("Indiquez la stratégie du joueur 1:");
      String strat1 = in.readString();
      switch(strat1.toUpperCase()){
        case "PAPERSTRAT":
          s1 = new PaperStrat();
          test=true;
          break;
        case "ROCKSTRAT":
          s1 = new RockStrat();
          test = true;
          break;
        case "SISSORSSTRAT":
          s1 = new SissorsStrat();
          test = true;
          break;
        case "INTERACTIVESTRAT":
          s1 = new InteractiveStrat();
          test = true;
          break;
        case "RANDOMSTRAT":
          s1 = new RandomStrat();
          test = true;
          break;
      }
      if (!test){
        System.out.println("Strategie incorrecte.");
        System.out.println("Stratégies possibles: PAPERSTRAT, ROCKSTRAT, SISSORSSTRAT, INTERACTIVESTRAT, RANDOMSTRAT");
      }
    }
    System.out.println('\n');
    System.out.println("Nom du deuxième joueur:");
    String p2 = in.readString();
    test = false;
    s2 = new RandomStrat();
    while (!test){
      System.out.println("Indiquez la stratégie du joueur 2:");
      String strat2 = in.readString();
      switch(strat2.toUpperCase()){
        case "PAPERSTRAT":
          s2 = new PaperStrat();
          test = true;
          break;
        case "ROCKSTRAT":
          s2 = new RockStrat();
          test = true;
          break;
        case "SISSORSSTRAT":
          s2 = new SissorsStrat();
          test = true;
          break;
        case "INTERACTIVESTRAT":
          s2 = new InteractiveStrat();
          test = true;
          break;
        case "RANDOMSTRAT":
          s2 = new RandomStrat();
          test = true;
          break;
      }
      if (!test){
        System.out.println("Strategie incorrecte.");
        System.out.println("Stratégies possibles: PAPERSTRAT, ROCKSTRAT, SISSORSSTRAT, INTERACTIVESTRAT, RANDOMSTRAT");
      }
    }
    System.out.println('\n');
    Player pl1 = new Player(p1, s1);
    Player pl2 = new Player(p2, s2);
    Game jeu = new Game(pl1, pl2, nb_tours);
    jeu.playGame();
  }
}

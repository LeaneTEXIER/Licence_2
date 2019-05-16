package hanoi;
import hanoi.util.*;
import io.*;
/**
 * Hanoi Game
 *
 * @author Leane Texier
 * @version 1.0
 */

public class Hanoi{
  private int capacity;
  private Tower[] theTowers;

  /**creates Hanoi
  * @param capacity the capacity of Hanoi
  */
  public Hanoi(int capacity){
    this.capacity = capacity;
    this.theTowers = new Tower[3];
    for (int i = 0 ; i<3 ; i++){
      this.theTowers[i] = new Tower(capacity);
    }
    for (int j=capacity; j>0; j--){
      this.theTowers[0].push(new Disc(j));
    }
  }

  /**returns the capacity of the 3 towers of Hanoi
  * @return the capacity of the 3 towers of Hanoi
  */
  public int getCapacity(){
    return this.capacity;
  }

  /**returns the table of towers of Hanoi
  * @return the table of towers of Hanoi
  */
  public Tower[] gettheTowers(){
    return this.theTowers;
  }

  /** Moves the discs
  * @param nbDisc the number of discs
  * @param source the tower of start
  * @param dest the tower of destination
  * @param inter the intermadiate tower
  */
  public void move(int nbDisc, int source, int dest, int inter){
    if (nbDisc==1){
      moveOneDiscText(source, dest);
    }
    else{
      move(nbDisc-1, source, inter, dest);
      moveOneDiscText(source, dest);
      move(nbDisc-1, inter, dest, source);
    }
  }

  /** Moves one disc from the tower source to the tower dest if it's possible
  * @param source the tower of start
  * @param dest the tower of destination
  */
  public void moveOneDisc(int source, int dest){
    Tower tsource = this.theTowers[source];
    Tower tdest = this.theTowers[dest];
    if (!tdest.isFull() && (tdest.isEmpty() || tdest.top().getSize() > tsource.top().getSize())){
      Disc d = tsource.pop();
      tdest.push(d);
    }
    else {
      System.out.println("Wrong move");
    }
  }

  /** Moves one disc from the tower source to the tower dest, and print the move
  * @param source the tower of start
  * @param dest the tower of destination
  */
  public void moveOneDiscText(int source, int dest){
    moveOneDisc(source, dest);
    System.out.println("Déplace disque de tour "+(source)+" à tour "+(dest));
  }

  /** Displays the tower (their composition)
  */
  public void display(){
    Tower t1 = this.theTowers[0];
    Tower t2 = this.theTowers[1];
    Tower t3 = this.theTowers[2];
    System.out.println("Tour 1: " + t1.getnbDisc()+" discs: " + t1.toString());
    System.out.println("Tour 2: " + t2.getnbDisc()+" discs: " + t2.toString());
    System.out.println("Tour 3: " + t3.getnbDisc()+" discs: " + t3.toString());
  }


 /**
 * The Hanoi's game, to play with text
 */
  public void hanoiGameAnn(){
    HanoiInput input = new HanoiInput();
    this.display();
    while (!this.theTowers[2].isFull()){
      try{
        input.readInput();
        Tower source = this.theTowers[input.getFrom()];
        Tower dest = this.theTowers[input.getTo()];
        this.moveOneDisc(input.getFrom(),input.getTo());
        this.display();
      }
      catch (IllegalStateException e){
        System.out.println("Fini!");
        System.exit(0);
      }
    }
  }


  /**
  * Draw a line of a tower
  * @param t the tower
  * @param i the high of the tower we look
  * @return a line of the tower (of the high i)
  */
  public String dessineTour(Tower t, int i){
    String line= "";
    /*Si un disque est présent à cette hauteur */
    if (i<t.getnbDisc()){
      int size=t.getTheDiscs()[i].getSize();
      /*Construit le coté gauche de la tour*/
      for (int j=capacity; j>=size; j--){
        line+= " ";
      }
      for (int j=size; j>0; j--){
        line+= "_";
      }
      /*Bare centrale */
      line += "|";
      /*Construit le coté droit de la tour*/
      for (int j=size; j>0; j--){
        line+= "_";
      }
      for (int j=capacity; j>=size; j--){
        line+= " ";
      }
     }
     /*Si aucun disque est présent à cette hauteur */
    else{
      int k=0;
      while (k!=2){
        for (int j=capacity; j>=0; j--){
          line+= " ";
        }
        if (k==0){
          line += "|";
        }
        k++;
     }
    }
    return line;
  }

  /**
  * Draw the tower with their discs
  */
  public void tourDessin(){
    Tower t1 = this.theTowers[0];
    Tower t2 = this.theTowers[1];
    Tower t3 = this.theTowers[2];
    int capacity = getCapacity();
    for (int i=capacity-1; i>=0; i--){
      String line= "";
      /* Tour 1*/
      line+=dessineTour(t1, i);
      /* Tour 2*/
      line+=dessineTour(t2, i);
      /* Tour 3*/
      line+=dessineTour(t3, i);
      /* Imprime la ligne */
      System.out.println(line);
    }
  }


  /**
  * The Hanoi's game, to play with drawing
  */
   public void hanoiGame(){
     HanoiInput input = new HanoiInput();
     this.tourDessin();
     while (!this.theTowers[2].isFull()){
       try{
         input.readInput();
         Tower source = this.theTowers[input.getFrom()];
         Tower dest = this.theTowers[input.getTo()];
         this.moveOneDisc(input.getFrom(),input.getTo());
         this.tourDessin();
       }
       catch (IllegalStateException e){
         System.out.println("Fini!");
         System.exit(0);
       }
     }
   }


  /** To play
  * @param args the size of the Hanoi tower
  */
  public static void main (String[] args){
    System.out.println("Les trois tours son désignées respectivement par les lettres g comme GAUCHE , c comme CENTRE et d comme DROITE. Pour effectuer un déplacement, il faut taper le mot de deux lettres correspondant à tour de départ tour d'arrivée. Par exemple en tapant gc, on déplace le disque au sommet de la tour gauche sur la tour centrale. On peut quitter en tapant quit");
    Hanoi h = new Hanoi(Integer.parseInt(args[0]));
    h.hanoiGame();
  }


  }

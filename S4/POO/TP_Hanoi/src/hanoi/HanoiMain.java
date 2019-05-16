package hanoi;
import hanoi.util.*;
/**
 * Hanoi resolution
 *
 * @author Leane Texier
 * @version 1.0
 */

public class HanoiMain{
     /**
     * Resolve the Hanoi problem for a number of discs given
     * @param args the size of the Hanoi tower
     */
     public static void main(String[] args){
         Hanoi h = new Hanoi(Integer.parseInt(args[0]));
         h.move(Integer.parseInt(args[0]),0,2,1);
     }
}

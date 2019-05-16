package example;
import example.util.*;
/**
 * A robot can carry one box at a time and put it on a coveyer belt
 *
 * @author jc
 * @version 1.0
 */

public class Robot {
    /**
     * creates a robot
     */
    public Robot() {
	this.carriedBox = null;
    }

    // les attributs de la classe Robot
    /** the box carried by robot  */
    private Box carriedBox;

    // les methodes de la classe Robot
    /**
     * this robot takes a box if it was not allready carrying one, else nothing happens
     * @param box the carried box
     */
    public void take(Box box) {
	if (!this.carryBox()) { // already carrying a box ?
	    this.carriedBox = box;
	}
    }

    /**
     * this robot puts the carried box on the belt
     *
     * @param belt the bel on which box is put
     *
     */
    public void putOn(ConveyerBelt belt) {
	if (this.carryBox() && belt.accept(carriedBox) && !belt.isFull()) {
	    // put box on belt
	    belt.receive(carriedBox);
	    // no more box is carried
	    this.carriedBox = null;
	} else {
	    if (!this.carryBox()) {
		System.out.println("no box carried");
	    } else if (belt.isFull()) {
		System.out.println("belt is full");
	    } else {
		System.out.println("box weights too much for this belt : " + this.carriedBox.getWeight() + " against "
				   + belt.getMaxWeight() + " max");
	    }
	}
    }

    /**
     * returns <code>true</code> iff this robot is carrying a box
     *
     * @return <code>true</code> iff this robot is carrying a box
     */
    public boolean carryBox() {
	return this.carriedBox != null;
    }

    /** returns the carried box
     * @return the carried box
     */
    public Box getCarriedBox() {
        return this.carriedBox;
    }

    public static void main(String[] args) {

    System.out.println("beginning of main from robot.Robot");

    Robot robbie = new Robot();
    ConveyerBelt belt1 = new ConveyerBelt(50);
    ConveyerBelt belt2 = new ConveyerBelt(150);
    Box box10 = new Box(10);
    Box box15 = new Box(15);
    Box box100 = new Box(100);
    Box box60 = new Box(60);

    robbie.take(box10);
    robbie.putOn(belt1);
    robbie.take(box15);
    robbie.putOn(belt1);
    robbie.take(box100);
    robbie.putOn(belt2);

    belt1.display();

    System.out.println("end of main from robot.Robot");
    }
}

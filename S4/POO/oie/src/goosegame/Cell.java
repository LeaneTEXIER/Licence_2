package goosegame;

public interface Cell{
  /** Get the index of the cell
  * @return the index of the current cell
  */
  public int getIndex();

  /** Get the player who is at the current cell
  * @return the player who is at the current cell
  */
  public Player getPlayer();

  /** Return <code>true</code> iif the player who is on the current cell can left this cell, else <code>false</code>
  * @return <code>true</code> iif the player can left the cell, else <code>false</code>
  */
  public boolean canBeLeft();

  /** Return the index of the cell really reached by a player when a player reaches this cell.
  * If it is a Basic Cell, return the current index. Else, it depends on the type of the cell and the dicethrow.
  * @param dicethrow the result of the dice lanch by the player when he reaches this cell
  * @return the index of the cell really reached by a player when a player reaches this cell
  */
  public int handleMove(int dicethrow);

  /** Return <code>true</code> iif there is a player on the current cell, else <code>false</code>
  * @return <code>true</code> iif there is a player on the cell, else <code>false</code>
  */
  public boolean isBusy();

  /** Put the player p on the current cell
  * @param p the player to move
  */
  public void putPlayerOnCell(Player p);

  /**
  *@see java.lang.Object#toString()
  */
  public String toString();
}

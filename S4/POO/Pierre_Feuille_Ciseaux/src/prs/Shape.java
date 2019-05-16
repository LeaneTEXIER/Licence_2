package prs;


public enum Shape{
  ROCK, PAPER, SISSORS;

  /** Return 0 if it's the same Shape, 1 if the current one is stronger than the given one, else -1
  * @param c Shape of the player number 2
  * @return 0 if it's the same Shape, 1 if the current one is stronger than the given one, else -1
  */
  public int compareShape (Shape c){
    if (this == c){
      return 0;
    }
    else if (this == ROCK){
      if (c == PAPER){
        return -1;
      }
      else{
        return 1;
      }
    }
    else if (this == PAPER){
      if (c == SISSORS){
        return -1;
      }
      else{
        return 1;
      }
    }
    else{
      if (c == ROCK){
        return -1;
      }
      else{
        return 1;
      }
    }
  }
}

package rental;

/** represent clients of a rental agency, the names are supposed to be
 * unique then two Client objects with same name are considered equals
*/
public class Client {

    private String name;
    private int age;

    /** create a client with given name and age, two different clients
     * have different names by assumption (no verification)
     * @param name name of the client
     * @param age age of the client
    */
    public Client(String name, int age) {
        this.name = name;
        this.age = age;
    }

    /** @return the client's name
      */
    public String getName() {
        return this.name;
    }

    /**@return the client's age
    */
    public int getAge() {
        return this.age;
    }

    /** Compares 2 clients
    * @param o the object to compare
    * @return <code>true</code> if the current client and the given one are equals, else <code>false</code>
    */
    public boolean equals(Object o){
      if (o instanceof Client){
        Client other = (Client) o;
        return this.name.equals(other.name);
      }
      return false;
    }

    /** @return the hashCode for a client
    */
    public int hashCode(){
      return this.name.hashCode();
    }

}

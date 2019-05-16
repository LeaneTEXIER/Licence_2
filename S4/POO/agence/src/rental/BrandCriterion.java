package rental;
/** a BrandCriterion allows to select a Vehicle for a given brand
*/

public class BrandCriterion implements Criterion {
    private String brand;
    /**
     *  @param brand the required brand 
     *  */
    public BrandCriterion(String brand) {
        this.brand = brand;
    }
    /** @return <code>true</code> if v's brand is the same than the required brand 
     *  @see Criterion#isSatisfiedBy(Vehicle) */
    public boolean isSatisfiedBy(Vehicle v) {
        return this.brand.equals(v.getBrand());
    }
}

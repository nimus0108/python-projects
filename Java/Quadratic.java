package u10.ex;

/**
 * Created by sumin1 on 5/1/15.
 */
public class Quadratic {
    private double a, b, c;

    public Quadratic(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public double getC() {
        return c;
    }

    public double getDiscriminant() {
        return (b * b) - (4 * (a * c));
    }

    public double getRoot1(){
        if(getDiscriminant()>=0){
            return ((-1 * b) + Math.pow(getDiscriminant(), 0.5)) / (2 * a);
        } else {
            return 0;
        }
    }

    public double getRoot2(){
        if(getDiscriminant()>=0){
            return ((-1 * b) - Math.pow(getDiscriminant(), 0.5)) / (2 * a);
        } else {
            return 0;
        }
    }
}
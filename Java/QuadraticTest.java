package u10.ex;

import java.util.Scanner;

/**
 * Created by sumin1 on 5/1/15.
 */
public class QuadraticTest {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double a, b, c;

        System.out.println("Enter a: ");
        a = scan.nextDouble();

        System.out.println("Enter b: ");
        b = scan.nextDouble();

        System.out.println("Enter c: ");
        c = scan.nextDouble();

        Quadratic q = new Quadratic(a, b, c);


        if(q.getDiscriminant()>0){
            System.out.println(q.getRoot1());
            System.out.println(q.getRoot2());
        } else if(q.getDiscriminant()==0){
            System.out.println(q.getRoot1());
        } else{
            System.out.println("The equation has no roots");
        }
    }
}

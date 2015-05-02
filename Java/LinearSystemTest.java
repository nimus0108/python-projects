package u10.ex;

import java.util.Scanner;

/**
 * Created by sumin1 on 5/1/15.
 */
public class LinearSystemTest {
    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        double a, b, c, d, e, f;

        System.out.println("Enter a: ");
        a = scan.nextDouble();
        b = scan.nextDouble();
        c = scan.nextDouble();
        d = scan.nextDouble();
        e = scan.nextDouble();
        f = scan.nextDouble();

        LinearSystem x = new LinearSystem(a, b, c, d, e, f);

        if(x.isSolvable()){
            System.out.println("x: " + x.getX());
            System.out.println("y: " + x.getY());
        }
    }
}

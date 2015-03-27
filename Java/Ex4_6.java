package org.bca.introcs.u1;

/**
 * Created by sumin1 on 3/9/15.
 */
public class Ex4_6 {
    public static void main (String args[]){
        double miles, kilometers;
        double miles2, kilometers2=20;

        System.out.printf("%-10s %-13s  |  %-13s %-10s \n", "Miles", "Kilometers", "Kilometers", "Miles");

        for (miles = 1; miles <= 10; miles ++){

                miles2 = kilometers2 / 1.609;
                kilometers = miles * 1.609;
                System.out.printf("%-10.0f %-13.3f  |  %-13.0f %-10.3f \n", miles, kilometers, kilometers2, miles2);

                kilometers2 += 5;
        }

    }
}

package org.bca.introcs.u1;

public class Ex4_3 {
    public static void main (String args[]) {
        double kg;
        double pounds;

        System.out.printf("%-15s %6s \n", "Kilograms", "Pounds");
        for (kg=1; kg <= 199; kg++){
            pounds = kg*2.2;
            System.out.printf("%-15.0f %6.1f \n", kg, pounds);
        }

    }
}

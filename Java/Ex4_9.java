package org.bca.introcs.u1;

import java.util.Scanner;

public class Ex4_9 {
    public static void main (String args[]){
        String name="", sname="", tname;
        int score=0, sscore=0, tscore;

        Scanner scan = new Scanner(System.in);

        System.out.println("How many students? ");
        int num = scan.nextInt();


        for (int i=0; i < num; i++){
            scan.nextLine();
            tname = scan.nextLine();
            tscore = scan.nextInt();


            if (tscore > score) {
                sscore = score;
                sname = name;
                score = tscore;
                name = tname;
            } else if (tscore > sscore){
                sscore = tscore;
                sname = tname;
            }
        }

        System.out.printf("1. %-10s %3d \n", name, score);
        System.out.printf("2. %-10s %3d", sname, sscore);



    }
}

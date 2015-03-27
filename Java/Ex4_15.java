package org.bca.introcs.u1;


import java.util.ArrayList;

public class Ex4_15 {
    public static void main (String args[]){
        int num;
        ArrayList answers = new ArrayList();
        for(num=33;num<=126;num++){
            answers.add((char)num);
        }

        int length = answers.size();
        int tens = length/10;
        int ones = length%10;
        int current=0;
        for(int i=0; i<(tens); i++){
            for(int g=0; g<10; g++) {
                System.out.print(answers.get(current) + " ");
                current++;
            }
            System.out.println();
        }
        for (int i=0; i<ones; i++){
            System.out.print(answers.get(current));
            current++;
        }


    }
}

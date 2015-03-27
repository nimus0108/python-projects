package org.bca.introcs.u1;

import java.util.ArrayList;

public class Ex4_10 {
    public static void main (String args[]){
        int cNum;
        ArrayList<Integer> answer = new ArrayList<Integer>();


        for(cNum=100; cNum <= 1000; cNum++){
            if (cNum%30==0){
                answer.add(cNum);
            }
        }


        int length = answer.size();
        //Because I know there are 30 numbers
        for(int i=0; i<length; i+=10){
            System.out.print(answer.get(i) + " ");
            System.out.print(answer.get(i+1) + " ");
            System.out.print(answer.get(i+2) + " ");
            System.out.print(answer.get(i+3) + " ");
            System.out.print(answer.get(i+4) + " ");
            System.out.print(answer.get(i+5) + " ");
            System.out.print(answer.get(i+6) + " ");
            System.out.print(answer.get(i+7) + " ");
            System.out.print(answer.get(i+8) + " ");
            System.out.println(answer.get(i+9) + " ");
        }


    }
}

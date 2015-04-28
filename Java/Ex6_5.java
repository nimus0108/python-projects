package u9.ex;

import java.util.Scanner;

/**
 * Created by sumin1 on 4/17/15.
 */
public class Ex6_5 {
    public static void main (String args[]){
        Scanner scan = new Scanner(System.in);
        int temp;

        System.out.print("Enter ten numbers: ");
        int[] answer = new int[10];
        boolean b = true;
        int ansIndex =0;

        for(int i=0; i<10; i++){
            temp = scan.nextInt();
            for(int j=0; j<answer.length; j++){
                if(temp==answer[j]){
                    b=false;
                }
            }

            if(b==true){
                answer[ansIndex] = temp;
                ansIndex++;
            }
            b = true;
        }

        System.out.print("The distinct numbers are: ");
        for(int i=0; i<answer.length; i++){
            if(answer[i]!=0){
                System.out.print(answer[i] + " ");
            }
        }


    }
}

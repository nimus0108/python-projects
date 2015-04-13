package u9.ex;

import java.util.Scanner;

public class Ex6_2 {
    public static void main (String args[]){
        int[] list = new int[10];
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter ten numbers: ");
        for(int i=0; i<10; i++){
            list[i] = scan.nextInt();
        }

        for(int i=9; i>=0; i--){
            System.out.print(list[i] + " ");
        }

    }
}

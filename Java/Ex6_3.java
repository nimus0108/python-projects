package u9.ex;

import java.util.Scanner;

public class Ex6_3 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int[] times = new int[100];
        int temp;

        System.out.println("Enter the integers between 1 and 100: ");
        temp=scan.nextInt();

        while (temp!=0){
            times[temp]++;
            temp=scan.nextInt();
        }
        for (int i=0; i<100; i++){
            if (times[i]!=0){
                System.out.print(i+" occurs "+times[i]);
                if (times[i]>1){
                    System.out.println(" times.");
                }
                else{
                    System.out.println(" time.");
                }
            }
        }
    }
}

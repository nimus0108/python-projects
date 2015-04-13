package u9.ex;

import java.util.Scanner;

public class Ex6_1 {
    public static void main (String args[]){
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the number of students: ");
        int num = scan.nextInt();
        System.out.print("Enter " + num + " scores: ");
        scan.nextLine();
        String input = scan.nextLine();
        String[] list = new String[num];
        String[] gradeList = new String[num];
        list = input.split(" ");
        int numGrade, max=0;
        int bestDiff;

        for(int i=0; i<list.length; i++){
            numGrade = Integer.parseInt(list[i]);
            max = Math.max(max,numGrade);
        }

        for(int i=0; i<list.length; i++){
            bestDiff = max- Integer.parseInt(list[i]);
            if (bestDiff <= 10){
                gradeList[i] = "A";
            } else if (bestDiff <=20){
                gradeList[i] = "B";
            } else if (bestDiff<=30){
                gradeList[i] = "C";
            } else if (bestDiff<=40){
                gradeList[i] = "D";
            } else{
                gradeList[i] = "F";
            }
        }

        for(int i=0; i<list.length; i++){
            System.out.println("Student " + i + " score is " + list[i] + " and grade is " + gradeList[i]);
        }

    }
}

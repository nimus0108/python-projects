package org.bca.introcs.u1;

import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
	public static void main (String args[]){
		//Scores of the user and the computer, and var to store whether or not to continue
		int userScore = 0, compScore = 0;
		String cont = "y";
		String compChoice = "";
		
		Scanner input = new Scanner(System.in);
		Random rand = new Random();
		
		System.out.println("Let's play rock paper scissors");
		
		while(userScore<5 && compScore<5 && cont.equals("y")){
			System.out.println("Enter your choice (r)ock, (p)aper, (s)cissors");
			String userChoice = input.nextLine();
			
			if (userChoice.equals("r")){
				userChoice = "Rock";
			} else if(userChoice.equals("p")){
				userChoice = "Paper";
			} else if(userChoice.equals("s")){
				userChoice = "Scissors";
			} else{
				System.out.println("Error: Invalid");
				break;
			}

			int random = rand.nextInt(3) + 1;

			if (random == 1){
				compChoice = "Rock";
			} else if (random == 2) {
				compChoice = "Paper";
			} else if (random == 3){
				compChoice = "Scissors";
			}


			if (userChoice==compChoice){
				System.out.println("It is a tie! You both choose " + compChoice);
			} else if (userChoice=="Rock" && compChoice=="Scissors"){
				System.out.println("You won!");
				System.out.println("The Computer chose " + compChoice + ", and you chose " + userChoice);
				userScore++;
			} else if (userChoice=="Rock" && compChoice=="Paper"){
				System.out.println("The computer won!");
				System.out.println("The Computer chose " + compChoice + ", and you chose " + userChoice);
				compScore++;
			} else if (userChoice=="Scissors" && compChoice=="Rock"){
				System.out.println("The computer won!");
				System.out.println("The Computer chose " + compChoice + ", and you chose " + userChoice);
				userScore++;
			} else if (userChoice=="Paper" && compChoice=="Rock"){
				System.out.println("The computer won!");
				System.out.println("The Computer chose " + compChoice + ", and you chose " + userChoice);
				compScore++;
			} else if (userChoice=="Scissors" && compChoice=="Paper"){
				System.out.println("You won!");
				System.out.println("The Computer chose " + compChoice + ", and you chose " + userChoice);
				userScore++;
			} else if (userChoice=="Paper" && compChoice=="Scissors"){
				System.out.println("The computer won!");
				System.out.println("The Computer chose " + compChoice + ", and you chose " + userChoice);
				compScore++;
			} else {
				System.out.println("Error");
			}
					
			System.out.println("Current Score is: You: " + userScore + "; Computer: " + compScore);
			
			if (userScore != 5 || compScore != 5){
				System.out.println("Would you like to continue playing? (y/n)");
				cont = input.nextLine();
			}
		}
		
		System.out.println("It has been fun. Here is the final score:");
		System.out.println("You: " + userScore + "; Computer: " + compScore);	
	}
}

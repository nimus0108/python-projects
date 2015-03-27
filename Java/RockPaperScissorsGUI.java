package org.bca.introcs.u1;

import java.util.Random;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class RockPaperScissorsGUI {
	public static void main (String args[]){
		//Scores of the user and the computer, and var to store whether or not to continue
		int userScore = 0, compScore = 0;
		int cont = 0;
		String compChoice = "";
		Object[] rps = {"Rock", "Paper", "Scissors"};
        Random rand = new Random();


		JOptionPane.showMessageDialog(null, "Let's play rock paper scissors");
		
		while(userScore<5 && compScore<5 && cont == 0){
			Object userChoice = JOptionPane.showInputDialog(null, "What hand will you play?", "Input", JOptionPane.QUESTION_MESSAGE, null,rps, rps[0]);

			int random = rand.nextInt(3) + 1;

			if (random == 1){
				compChoice = "Rock";
			} else if (random == 2) {
				compChoice = "Paper";
			} else if (random == 3){
				compChoice = "Scissors";
			}


			if (userChoice.equals(compChoice)){
				JOptionPane.showMessageDialog(null,"It is a tie! You both choose " + compChoice);
			} else if (userChoice.equals("Rock") && compChoice.equals("Scissors")){
				JOptionPane.showMessageDialog(null,"You won! The Computer chose " + compChoice + ", and you chose " + userChoice);
				userScore++;
			} else if (userChoice.equals("Rock") && compChoice.equals("Paper")){
				JOptionPane.showMessageDialog(null,"The computer won! The Computer chose " + compChoice + ", and you chose " + userChoice);
				compScore++;
			} else if (userChoice.equals("Scissors") && compChoice.equals("Rock")){
				JOptionPane.showMessageDialog(null,"The computer won! The Computer chose " + compChoice + ", and you chose " + userChoice);
				userScore++;
			} else if (userChoice.equals("Paper") && compChoice.equals("Rock")){
				JOptionPane.showMessageDialog(null,"The computer won! The Computer chose " + compChoice + ", and you chose " + userChoice);
				compScore++;
			} else if (userChoice.equals("Scissors") && compChoice.equals("Paper")){
				JOptionPane.showMessageDialog(null,"You won! The Computer chose " + compChoice + ", and you chose " + userChoice);
				userScore++;
			} else if (userChoice.equals("Paper") && compChoice.equals("Scissors")){
				JOptionPane.showMessageDialog(null,"The computer won! The Computer chose " + compChoice + ", and you chose " + userChoice);
				compScore++;
			} else {
				JOptionPane.showMessageDialog(null,"Error");
			}
					
			JOptionPane.showMessageDialog(null,"Current Score is: You: " + userScore + "; Computer: " + compScore);
			
			if (userScore != 5 && compScore != 5){
                JFrame frame = new JFrame();
                Object stringArray[] = { "Yes", "No" };
                cont = JOptionPane.showOptionDialog(frame, "Continue playing?", "Select an Option",
                        JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE, null, stringArray,
                        stringArray[0]);
			}

		}
		
		JOptionPane.showMessageDialog(null,"It has been fun. Here is the final score: \nYou: " + userScore + "; Computer: " + compScore);
	}
}

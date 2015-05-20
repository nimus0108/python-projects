package u10.u10.capitals;

import javax.swing.*;
import java.io.FileNotFoundException;

/**
 * Created by sumin1 on 5/14/15.
 */
public class StateCapitalQuiz {
    public static void main(String[] args) throws FileNotFoundException {
        String[] states = {"states_all.txt", "states_central.txt", "states_east.txt", "states_west.txt", "states_small_test.txt", "states_south.txt"};
        int correct = 0;
        int guess = 0;
        String a = "";

        JOptionPane.showMessageDialog(null, "Welcome to the State Quiz Challenge!");
        String whichFile = (String) JOptionPane.showInputDialog(null, "Which quiz file would you like to use?",
                "Quiz", JOptionPane.QUESTION_MESSAGE, null, states, states[0]);
        StateCapitalList list = new StateCapitalList(whichFile);

        while(list.statesRemaining()!= 0){
            System.out.println(list.statesRemaining());
            StateCapital q = list.getRandomState();
            a = JOptionPane.showInputDialog("What is the capital of " + q.getState());
            if (a.toUpperCase().equals(q.getCapital().toUpperCase())){
                JOptionPane.showMessageDialog(null, "Correct!");
                list.remove(q);
                System.out.println("Answer: " + q.getState());
                correct++;
            }
            else{
                JOptionPane.showMessageDialog(null, "Incorrect. The capital is " + q.getCapital());
            }
            guess++;
        }


        JOptionPane.showMessageDialog(null,
                "You named " + correct + " correct capitals in " + guess + " guesses.");

    }

}

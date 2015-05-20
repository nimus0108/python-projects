package u10.u10.capitals;

import javax.swing.plaf.nimbus.State;
import java.io.FileReader;
import java.util.Random;
import java.util.Scanner;
import java.io.FileNotFoundException;

/**
 * Created by sumin1 on 5/14/15.
 */

public class StateCapitalList {
    StateCapital[] x = new StateCapital[1];
    int length = 0;

    public StateCapitalList(String fileName) throws FileNotFoundException{
        Scanner scan = new Scanner(new FileReader(fileName));

        while(scan.hasNextLine()) {
            String[] tList = scan.nextLine().split("\t");
            StateCapital tST = new StateCapital(tList[0], tList[1]);
            if (length >= x.length){
                StateCapital[] tempState = new StateCapital[x.length * 2];
                for (int j = 0; j < x.length; j++) {
                    tempState[j] = x[j];
                }
                x = tempState;
            }
            x[length] = tST;
            length++;
        }
    }

    public StateCapital getRandomState(){
        Random r = new Random();
        int index = r.nextInt(length);
        return x[index];
    }

    public void remove(StateCapital remove){
        int index = 0;
        for (int i=0; i<length; i++){
            if (x[i].equals(remove)){
                index = i;
            }
        }

        for (; index<length-1; index++){
            x[index] = x[index+ 1];
        }
        length--;
    }

    public int statesRemaining(){
        return length;
    }
}

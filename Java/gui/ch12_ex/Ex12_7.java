package u11.ch12_ex;

import javax.swing.*;
import java.awt.*;
import java.util.Random;

/**
 * Created by sumin1 on 5/26/15.
 */
public class Ex12_7 extends JFrame{
    Random rand = new Random();
    private ImageIcon o = new ImageIcon("image/o.gif");
    private ImageIcon x = new ImageIcon("image/x.gif");

    public Ex12_7(){
        setLayout(new GridLayout(3,3,5,5));

        for(int i=0; i<9; i++){
            int c = rand.nextInt(3) + 1;
            if(c==1){add(new JLabel());}
            else if(c==2){add(new JLabel(o));}
            else if(c==3){add(new JLabel(x));}
        }

    }

    public static void main(String args[]){
        Ex12_7 frame = new Ex12_7();
        frame.setTitle("TestImageIcon");
        frame.setSize(200,200);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

    }
}

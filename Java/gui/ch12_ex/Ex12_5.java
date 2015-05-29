package u11.ch12_ex;

import gui.ShowGridLayout;

import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.LineBorder;
import java.awt.*;

/**
 * Created by sumin1 on 5/26/15.
 */
public class Ex12_5 extends JFrame{
    public Ex12_5(){

        Border lineBorder = new LineBorder(Color.BLACK, 2);
        setLayout(new GridLayout(4,1,5,5));
        JLabel a = (new JLabel("Department of Computer Science"));
        JLabel b = (new JLabel("SCHOOL OF Computing"));
        JLabel c = (new JLabel("Armstrong Atlantic STate University"));
        JLabel d = (new JLabel("Tel: (912) 921-6440"));
        add(a);
        add(b);
        add(c);
        add(d);

        a.setBorder(lineBorder);
        b.setBorder(lineBorder);
        c.setBorder(lineBorder);
        d.setBorder(lineBorder);
    }

    public static void main(String args[]){
        Ex12_5 frame = new Ex12_5();
        frame.setTitle("12_5");
        frame.setSize(200,125);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

}

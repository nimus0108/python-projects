package u11.ch12_ex;

import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.LineBorder;
import java.awt.*;

/**
 * Created by sumin1 on 5/26/15.
 */
public class Ex12_6 extends JFrame{
    private ImageIcon usIcon = new ImageIcon("image/us.gif");
    private ImageIcon myIcon = new ImageIcon("image/my.jpg");
    private ImageIcon frIcon = new ImageIcon("image/fr.gif");
    private ImageIcon ukIcon = new ImageIcon("image/uk.gif");

    public Ex12_6(){
        Border lineBorder = new LineBorder(Color.BLACK, 2);

        setLayout(new GridLayout(2, 2, 5, 5));
        JLabel a = (new JLabel(usIcon));
        JLabel b =(new JLabel(myIcon));
        JLabel c = (new JLabel(frIcon));
        JLabel d = (new JLabel(ukIcon));

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
        Ex12_6 frame = new Ex12_6();
        frame.setTitle("12_6");
        frame.setSize(200,200);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

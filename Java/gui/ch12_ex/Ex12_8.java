package u11.ch12_ex;

import javax.swing.*;
import javax.swing.border.Border;
import javax.swing.border.LineBorder;
import javax.swing.border.TitledBorder;
import java.awt.*;

/**
 * Created by sumin1 on 5/28/15.
 */
public class Ex12_8 extends JFrame{
    public Ex12_8(){
        setLayout(new GridLayout(2,3,5,5));
        JLabel black = (new JLabel("Black"));
        JLabel blue = (new JLabel("Blue"));
        JLabel cyan = (new JLabel("Cyan"));
        JLabel green = (new JLabel("Green"));
        JLabel magenta = (new JLabel("Magenta"));
        JLabel orange = (new JLabel("Orange"));

        Border lineBorder = new LineBorder(Color.YELLOW);
        black.setBorder(lineBorder);
        blue.setBorder(lineBorder);
        cyan.setBorder(lineBorder);
        green.setBorder(lineBorder);
        magenta.setBorder(lineBorder);
        orange.setBorder(lineBorder);

        black.setForeground(Color.BLACK);
        blue.setForeground(Color.BLUE);
        cyan.setForeground(Color.CYAN);
        green.setForeground(Color.GREEN);
        magenta.setForeground(Color.MAGENTA);
        orange.setForeground(Color.ORANGE);

        Font font = new Font("TimesRoman", Font.BOLD, 20);
        black.setFont(font);
        blue.setFont(font);
        cyan.setFont(font);
        green.setFont(font);
        magenta.setFont(font);
        orange.setFont(font);

        add(black);
        add(blue);
        add(cyan);
        add(green);
        add(magenta);
        add(orange);


    }

    public static void main(String[] args) {
        Ex12_8 frame = new Ex12_8();
        frame.setTitle("Ex12_8");
        frame.setSize(300, 150);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

package gui;

import javax.swing.*;
import java.awt.*;

/**
 * Created by sumin1 on 5/18/15.
 */
public class ShowGridLayout extends JFrame{
    public ShowGridLayout(){

        setLayout(new GridLayout(3,2,5,5));

        add(new JLabel("First Name"));
        add(new JTextField(8));
        add(new JLabel("MI"));
        add(new TextField(1));
        add(new JLabel("Last Name"));
        add(new JTextField(8));
    }

    public static void main(String[] args){
        ShowGridLayout frame = new ShowGridLayout();
        frame.setTitle("ShowGridLayout");
        frame.setSize(200,125);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

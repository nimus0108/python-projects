package gui;

/**
 * Created by sumin1 on 5/18/15.
 */
import javax.swing.*;
import java.awt.*;

public class ShowFlowLayout extends JFrame{
    public ShowFlowLayout(){
        setLayout(new FlowLayout(FlowLayout.LEFT, 10, 20));

        add(new JLabel("First Name"));
        add(new JTextField(8));
        add(new JLabel("MI"));
        add(new TextField(1));
        add(new JLabel("Last Name"));
        add(new JTextField(8));
    }

    public static void main(String[] args){
        ShowFlowLayout frame = new ShowFlowLayout();
        frame.setTitle("ShowFlowLayout");
        frame.setSize(200,200);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}

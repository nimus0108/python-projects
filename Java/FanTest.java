package u10.ex;

/**
 * Created by sumin1 on 5/1/15.
 */
public class FanTest {
    public static void main(String[] args){
        Fan fan1 = new Fan(Fan.FAST, true, 10, "yellow");
        Fan fan2 = new Fan(Fan.MEDIUM, false, 5, "blue");

        System.out.println(fan1.toString());
        System.out.println(fan2.toString());

    }
}

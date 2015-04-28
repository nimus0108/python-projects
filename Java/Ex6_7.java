package u9.ex;

/**
 * Created by sumin1 on 4/17/15.
 */
public class Ex6_7 {
    public static void main(String args[]){
        int[] count = new int[10];
        for(int i=0; i<100; i++){
            int random = (int)(Math.random() * 10);
            count[random]++;
        }

        for(int i=0; i<10; i++){
            System.out.println(count[i]);
        }
    }
}

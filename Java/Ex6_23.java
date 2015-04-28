package u9.ex;

/**
 * Created by sumin1 on 4/17/15.
 */
public class Ex6_23 {
    public static void main(String args[]){
        boolean[] lockers = new boolean[100];

        for(int i=1; i<=100; i++){
            for(int j=1; j*i<=100; j++){
                if (lockers[(j * i) - 1]) {
                    lockers[(j * i) - 1] = false;
                } else {
                    lockers[(j * i) - 1] = true;
                }

            }

        }


        for(int i=0; i<100; i++){
            System.out.println(lockers[i]);
        }

    }
}

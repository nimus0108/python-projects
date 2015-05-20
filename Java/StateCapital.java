package u10.u10.capitals;


/**
 * Created by sumin1 on 5/14/15.
 */
public class StateCapital {
    String state;
    String capital;

    public boolean equals(Object o){
        StateCapital x = (StateCapital) o;
        return (this.state.equals(x.state));
    }

    public String getState() {
        return state;
    }

    public String getCapital() {
        return capital;
    }

    public StateCapital(String state, String capital) {

        this.state = state;
        this.capital = capital;
    }
}

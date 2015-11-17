package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import networking.response.*;
import utility.DataReader;

public class RequestChangeHealth extends GameRequest {

    // Data
    private String username;
    private int healthChange;
    
// Responses
        private ResponseChangeHealth responseChangeHealth;
    
    
    public RequestChangeHealth() {
                responses.add( responseChangeHealth= new ResponseChangeHealth());
    
    }

    @Override
    public void parse() throws IOException {
        username=DataReader.readString(dataInput);
        healthChange = DataReader.readInt(dataInput);
       
    }

    @Override
    public void doBusiness() throws Exception {
    
        System.out.println("healthChange=="+healthChange);
    System.out.println("username=="+username);
        
 responseChangeHealth.setCarId("health");

    }

}

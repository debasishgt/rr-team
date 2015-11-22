package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import networking.response.*;
import utility.DataReader;

public class RequestPowerUpPickUp extends GameRequest {

    // Data
    private int powerId;
 
    // Responses
        private ResponsePowerUpPickUp responsePowerUpPickUp;
    
    
    public RequestPowerUpPickUp() {
                responses.add(responsePowerUpPickUp = new ResponsePowerUpPickUp());
    
    }

    @Override
    public void parse() throws IOException {
        powerId = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
    
        System.out.println("powerId=="+powerId);
        responsePowerUpPickUp.setUsername("manish");
        responsePowerUpPickUp.setPowerId(5);
        
    
    }
}


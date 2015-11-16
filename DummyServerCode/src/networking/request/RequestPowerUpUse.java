package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestPowerUpUse extends GameRequest {

    // Data
    private int powerId;
 
    // Responses
        private ResponsePowerUpUse responsePowerUpUse;
 
        
          
    public RequestPowerUpUse() {
       
      responses.add(responsePowerUpUse = new ResponsePowerUpUse());
    }

    @Override
    public void parse() throws IOException {
        powerId = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
         	System.out.println("powerId=="+powerId);
     responsePowerUpUse.setUsername("powerupuse");
  
    }
}

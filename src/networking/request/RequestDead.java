

package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestDead extends GameRequest {

    // Data
    
    // Responses
    
        private ResponseDead responseDead;
    
    
    public RequestDead() {
       responses.add(responseDead = new ResponseDead());
    }

    @Override
    public void parse() throws IOException {
    
    }

    @Override
    public void doBusiness() throws Exception {
    
        responseDead.setUsername("manish");
    
    }
}






package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestReady extends GameRequest {

    // Data
    
    // Responses
    
        private ResponseReady responseReady;
    
    
    public RequestReady() {
       responses.add(responseReady = new ResponseReady());
    }

    @Override
    public void parse() throws IOException {
    
    }

    @Override
    public void doBusiness() throws Exception {
    responseReady.setNumberOfUsers(5);
    responseReady.setUsername("manish");
    responseReady.setStatus(5);
    }
}




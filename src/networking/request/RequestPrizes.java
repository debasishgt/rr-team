

package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import networking.response.*;
import utility.DataReader;

public class RequestPrizes extends GameRequest {

    // Data
    
    
    
    // Responses
        private ResponsePrizes responsePrizes;
    
    
    public RequestPrizes() {
                responses.add(responsePrizes = new ResponsePrizes());
    
    }

    @Override
    public void parse() throws IOException {
    
    }

    @Override
    public void doBusiness() throws Exception {
    
        responsePrizes.setItemid(5);
    }
}




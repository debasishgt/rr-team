

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
    
    private String username;

    
    // Responses
        private ResponsePrizes responsePrizes;
    
    
    public RequestPrizes() {
                responses.add(responsePrizes = new ResponsePrizes());
    
    }

    @Override
    public void parse() throws IOException {
        username = DataReader.readString(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        System.out.println("username=="+username);
        responsePrizes.setUsername("prizes");
    }
}




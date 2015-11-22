package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestSetRank extends GameRequest {

    // Data
    
    // Responses
        private ResponseSetRank responseSetRank;
    
    
    public RequestSetRank() {
     responses.add(responseSetRank = new ResponseSetRank());
    
    }

    @Override
    public void parse() throws IOException {
    
    }

    @Override
    public void doBusiness() throws Exception {
    
    responseSetRank.setRank(5);
    }
}



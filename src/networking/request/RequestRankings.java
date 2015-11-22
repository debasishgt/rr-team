

package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestRankings extends GameRequest {

    // Data
    
    // Responses
        private ResponseRankings responseRankings;
    
    
    public RequestRankings() {
                responses.add(responseRankings = new ResponseRankings());
    
    }

    @Override
    public void parse() throws IOException {
    
    }

    @Override
    public void doBusiness() throws Exception {
   
        responseRankings.setNumber_of_players(5);
    
    }
}





package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestResults extends GameRequest {

    // Data
    private int gameId;
 
    // Responses
        private ResponseResults responseResults;
    
    
    public RequestResults() {
                responses.add(responseResults = new ResponseResults());
    
    }

    @Override
    public void parse() throws IOException {
        gameId = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
      System.out.println("gameId=="+gameId);
    responseResults.setNumber_of_players(2);
     responseResults.setPlace(5);
    }
}





package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestRankings extends GameRequest {

    // Data
    private int gameId;
 
    // Responses
        private ResponseRankings responseRankings;
    
    
    public RequestRankings() {
                responses.add(responseRankings = new ResponseRankings());
    
    }

    @Override
    public void parse() throws IOException {
        gameId = DataReader.readInt(dataInput);
    
    }

    @Override
    public void doBusiness() throws Exception {
   System.out.println("gameId=="+gameId);
     responseRankings.setMsg("rankings");
    
    }
}




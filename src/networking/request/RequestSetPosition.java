package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestSetPosition extends GameRequest {

    // Data
    
    // Responses
        private ResponseSetPosition responseSetPosition;
    
    
    public RequestSetPosition() {
     responses.add(responseSetPosition = new ResponseSetPosition());
    
    }

    @Override
    public void parse() throws IOException {
    
    }

    @Override
    public void doBusiness() throws Exception {
    
    responseSetPosition.setNumberOfUsers(5);
    responseSetPosition.setUsername("manish");
    responseSetPosition.setX(5);
    responseSetPosition.setY(4);
    responseSetPosition.setZ(5);
    responseSetPosition.setH(1);
    }
}



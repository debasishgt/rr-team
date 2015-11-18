package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponseReady;
// Custom Imports
//import core.GameServer;

public class RequestReady extends GameRequest {
	
	// Responses
	private ResponseReady responseReady;

	public RequestReady() {
		responses.add(responseReady = new ResponseReady());
	}

	@Override
	public void parse() throws IOException {
		//Nothing Recieved
	}

	@Override
	public void doBusiness() throws Exception{
		//Tells the session that this player is ready.
	}
}

package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
import networking.response.ResponseResults;
// Custom Imports
//import core.GameServer;
import utility.DataReader;
import utility.Player;

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
		//Sets the list of Players from the current session
		//client.getSession().getActivePlayers();
	}
}

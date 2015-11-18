package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
import networking.response.ResponseRankings;
// Custom Imports
//import core.GameServer;
import utility.DataReader;
import utility.Player;

public class RequestRankings extends GameRequest {

	// Data
	private int gameId;
	// Responses
	private ResponseRankings responseRankings;
	private int player_id;

	public RequestRankings() {
		responses.add(responseRankings = new ResponseRankings());

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

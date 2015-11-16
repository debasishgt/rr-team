package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponseDead;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestDead extends GameRequest {

	// Data
	private int gameId;
	// Responses
	private ResponseDead responseDead;

	public RequestDead() {
		//responses.add(responseDead = new ResponseDead());
		responseDead = new ResponseDead();

	}

	@Override
	public void parse() throws IOException {
		gameId = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		responseDead.setPlayerId(client.getId());
		//Need a way to send this to only people in the same game.
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseDead);

	}
}

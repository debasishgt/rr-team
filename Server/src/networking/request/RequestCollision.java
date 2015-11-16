package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponseCollision;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestCollision extends GameRequest {

	// Data
	private int playerId;
	private int damage;
	// Responses
	private ResponseCollision responseCollision;

	public RequestCollision() {
		//responses.add(responseCollision = new ResponseCollision());
		responseCollision = new ResponseCollision();
	}

	@Override
	public void parse() throws IOException {
		playerId = DataReader.readInt(dataInput);
		damage = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		responseCollision.setDamage(damage);
		client.getServer().addResponseForUser(client.getServer().getActivePlayer(playerId).getUsername(), responseCollision);

	}
}

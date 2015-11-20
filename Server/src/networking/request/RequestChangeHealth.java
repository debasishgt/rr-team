package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.GameResponse;
import networking.response.ResponseChangeHealth;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestChangeHealth extends GameRequest {

	// Data
	private int healthChange;
	// Responses
	private ResponseChangeHealth responseChangeHealth;

	public RequestChangeHealth() {
		responseChangeHealth = new ResponseChangeHealth();

	}

	@Override
	public void parse() throws IOException {
		String username = DataReader.readString(dataInput);
		healthChange = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		System.out.println(healthChange);
        responseChangeHealth.setUsername(client.getPlayer().getUsername()); 
        responseChangeHealth.setHealthChange(healthChange); 
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), (GameResponse) responseChangeHealth); 
    }
}
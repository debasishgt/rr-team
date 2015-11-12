package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.GameResponse;
import networking.response.ResponsePowerUpUse;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestPowerUpUse extends GameRequest {

	// Data
	private int powerId;
	// Responses
	private ResponsePowerUpUse responsePowerUpUse;

	public RequestPowerUpUse() {
		responsePowerUpUse = new ResponsePowerUpUse();
	}

	@Override
	public void parse() throws IOException {
		powerId = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		
		System.out.println(powerId);
        responsePowerUpUse.setPowerId(powerId);
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), (GameResponse) responsePowerUpUse); 
    }
}

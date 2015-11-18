package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponsePowerPickUp;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestPowerPickUp extends GameRequest {

	// Data
	private int powerId;
	// Responses
	private ResponsePowerPickUp responsePowerPickUp;

	public RequestPowerPickUp() {
		responses.add(responsePowerPickUp = new ResponsePowerPickUp());

	}

	@Override
	public void parse() throws IOException {
		powerId = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		
		//Check session if the powerup is available.

		responsePowerPickUp.setValidate(0);

	}
}

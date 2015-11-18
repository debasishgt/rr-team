package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponsePrizes;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestPrizes extends GameRequest {

	// Data
	private String username;
	// Responses
	private ResponsePrizes responsePrizes;

	public RequestPrizes() {
		responses.add(responsePrizes = new ResponsePrizes());

	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		//Determine the user's prize based on their rank in the game.
		responsePrizes.setItemId(0);
	}
}

package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
// Custom Imports
//import core.GameServer;
import networking.response.ResponseRegister;
import utility.DataReader;
import utility.Player;

public class RequestRegister extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseRegister responseRegister;

	public RequestRegister() {
		responses.add(responseRegister = new ResponseRegister());
	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		DatabaseDriver db = client.getServer().getDAO();
		int player_id = db.createPlayer(username, password);
		if (player_id != 0) {
			responseRegister.setNumber(1);
		} else {
			responseRegister.setNumber(0);
		}

	}
}
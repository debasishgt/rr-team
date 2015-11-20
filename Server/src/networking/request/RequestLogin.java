package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
import model.Player;
import networking.response.ResponseAuth;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestLogin extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseAuth responseAuth;

	public RequestLogin() {
		responses.add(responseAuth = new ResponseAuth());

	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		DatabaseDriver db = DatabaseDriver.getInstance();
		int player_id = db.checkAuth(username, password);

		if (player_id != -1) {
			System.out.println("Connected !");
			client.setPlayer(db.getPlayerById(player_id));
			responseAuth.setAnswer((short) 1);
		} else {
			System.out.println("Wrong credentials");
			responseAuth.setAnswer((short) 0);
		}
	}
}

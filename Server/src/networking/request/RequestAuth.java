package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
import model.Player;
import networking.response.ResponseAuth;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestAuth extends GameRequest {

	// Data
	private String username;
	private String password;
	// Responses
	private ResponseAuth responseAuth;

	public RequestAuth() {
		responses.add(responseAuth = new ResponseAuth());

	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {

		if (client.getServer().getThreadByPlayerUserName(username) != null) {
			responseAuth.setAnswer((short) 2);

		} else {
			DatabaseDriver db = DatabaseDriver.getInstance();
			int player_id = db.checkAuth(username, password);

			if (player_id != -1) {
				System.out.println("Connected !");
				client.setPlayer(new Player(username, player_id));
				responseAuth.setAnswer((short) 1);
			} else {
				System.out.println("Wrong credentials");
				responseAuth.setAnswer((short) 0);
			}
		}
		//responses.add(responseAuth);
	}
}

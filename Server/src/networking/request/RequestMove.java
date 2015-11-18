package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
import networking.response.GameResponse;
import networking.response.ResponseMove;
// Custom Imports
//import core.GameServer;
import utility.DataReader;
import utility.Player;

public class RequestMove extends GameRequest {

	// Data
	private Float x;
	private Float y;
	private Float z;
	private Float h;
	private String keys;
	// Responses
	private ResponseMove responseMove;

	public RequestMove() {
		responseMove = new ResponseMove();
	}

	@Override
	public void parse() throws IOException {
		x = DataReader.readFloat(dataInput);
		y = DataReader.readFloat(dataInput);
		z = DataReader.readFloat(dataInput);
		h = DataReader.readFloat(dataInput);
		keys = DataReader.readString(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		System.out.println(x + "," + y + "," + z + "," + h);
		System.out.println(keys);
		responseMove.setUsername(client.getPlayer().getUsername());
		responseMove.setX(x);
		responseMove.setY(y);
		responseMove.setZ(z);
		responseMove.setH(h);
		responseMove.setKeys(keys);
        client.getServer().addResponseForAllOnlinePlayers(client.getId(), (GameResponse) responseMove); 
	}
}

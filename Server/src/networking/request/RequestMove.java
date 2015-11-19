package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseMove;

public class RequestMove extends GameRequest {
	
	float x, y, z, h;
	private ResponseMove responseMove;
	
	public RequestMove() {
        responses.add(responseMove = new ResponseMove());
    }
	
	@Override
	public void parse() throws IOException {
		x = DataReader.readFloat(dataInput);
		y = DataReader.readFloat(dataInput);
		z = DataReader.readFloat(dataInput);
		h = DataReader.readFloat(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		
		// Create ResponseMove object
		responseMove.setPosition(this.x, this.y, this.z, this.h);
		responseMove.setUsername(this.client.getPlayer().getUsername());
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseMove);
	}
}
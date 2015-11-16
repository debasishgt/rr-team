package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseMove;

public class RequestMove extends GameRequest {
	
	float x, y, h;
	boolean isMoving;
	private ResponseMove responseMove;
	
	public RequestMove() {
        responses.add(responseMove = new ResponseMove());
    }
	
	@Override
	public void parse() throws IOException {
		x = DataReader.readFloat(dataInput);
		y = DataReader.readFloat(dataInput);
		h = DataReader.readFloat(dataInput);
		isMoving = DataReader.readBoolean(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		
		// Create ResponseMove object
		responseMove.setPosition(this.x, this.y, this.h);
		responseMove.setIsMoving(isMoving);
		responseMove.setSenderUsername(this.client.getPlayer().getUsername());
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseMove);
	}
}
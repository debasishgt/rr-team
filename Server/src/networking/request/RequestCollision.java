package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseCollision;

public class RequestCollision extends GameRequest {
	
	private ResponseCollision responseCollision;
	
	public RequestCollision() {
        responses.add(responseCollision = new ResponseCollision());
    }
	
	@Override
	public void parse() throws IOException {
		//parse the datainput here
		//x = DataReader.readFloat(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		//do the Collision business here
		
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseCollision);
	}

}

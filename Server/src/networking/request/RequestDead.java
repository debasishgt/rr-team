package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseDead;

public class RequestDead extends GameRequest {
	
	private ResponseDead responseDead;
	
	public RequestDead() {
        responses.add(responseDead = new ResponseDead());
    }
	
	@Override
	public void parse() throws IOException {
		//parse the datainput here
		//x = DataReader.readFloat(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		//do the rankings business here
		
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseDead);
	}

}

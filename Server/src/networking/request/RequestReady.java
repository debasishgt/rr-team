package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponseReady;

public class RequestReady extends GameRequest {
	
	private ResponseReady responseReady;
	
	public RequestReady() {
        responses.add(responseReady = new ResponseReady());
    }
	
	@Override
	public void parse() throws IOException {
		//parse the datainput here
		//x = DataReader.readFloat(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		//do the Ready business here
		
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responseReady);
	}

}

package networking.request;

import java.io.IOException;
import java.util.Map;
import java.util.HashMap;

import core.GameClient;
import networking.response.ResponseReady;

public class RequestReady extends GameRequest {
	
	private ResponseReady responseReady;
	
	public RequestReady() {
		responseReady = new ResponseReady();
    }
	
	@Override
	public void parse() throws IOException {
		
	}

	@Override
	public void doBusiness() throws Exception {
		if(!this.client.getPlayer().isReady()){
			this.client.getPlayer().setReady();
			int roomId = this.client.getPlayer().getRoom().getId();
			if(allReady(roomId)){
				this.client.getServer().getGameSessionByRoomId(roomId).gameStart();
			}
		}
		
		Map<String, Integer> status = new HashMap<>();
		
		for(GameClient client : this.client.getServer().getGameClientsForRoom(this.client.getPlayer().getRoom().getId()))
		{
			if(client.getPlayer().isReady())
			{
				status.put(client.getName(), 1);
			}
			else
			{
				status.put(client.getName(), 0);
			}
		}
		
		this.client.getServer().addResponseForRoom(this.client.getPlayer().getRoom().getId(), responseReady);
	}

	private boolean allReady(int room_id) {
		for(GameClient gclient : this.client.getServer().getGameClientsForRoom(room_id)){
			if(!gclient.getPlayer().isReady()){
				return false;
			}
		}
		return true;
	}

}

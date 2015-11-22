package networking.request;

import java.io.IOException;
import java.util.Map;
import java.util.HashMap;

import core.GameClient;
import networking.response.ResponseSetReady;

public class RequestReady extends GameRequest {
	
	private ResponseSetReady responseSetReady;
	
	public RequestReady() {
		responseSetReady = new ResponseReady();
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
		
		responseSetReady.setUsername(this.client.getPlayer().getUsername())
		this.client.getServer().addResponseForRoom(this.client.getPlayer().getRoom().getId(), responseSetReady);
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

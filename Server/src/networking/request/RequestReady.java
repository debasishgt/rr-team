package networking.request;

import java.io.IOException;

import core.GameClient;
import core.GameSession;
import utility.DataReader;
import networking.response.ResponseReady;

public class RequestReady extends GameRequest {
	
	private ResponseReady responseReady;
	
	public RequestReady() {
		
    }
	
	@Override
	public void parse() throws IOException {
		
	}

	@Override
	public void doBusiness() throws Exception {
		this.client.getPlayer().setReady();
		int roomId = this.client.getPlayer().getRoom().getId();
		if(allReady(roomId)){
			GameSession gsession = this.client.getServer().getGameSessionByRoomId(roomId);
			gsession.sendAllResponseReady();
			gsession.getGameroom().setTimeStarted(System.currentTimeMillis());
			gsession.setGameStarted(true);
		}
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

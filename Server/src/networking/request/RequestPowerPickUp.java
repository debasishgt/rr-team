package networking.request;

import java.io.IOException;

import utility.DataReader;
import networking.response.ResponsePowerPickUp;

public class RequestPowerPickUp extends GameRequest {
	private int powerId;
	// Data
	// Responses
	private ResponsePowerPickUp responsePowerUpPickUp;

	public RequestPowerPickUp() {
		responses.add(responsePowerUpPickUp = new ResponsePowerPickUp());
	}

	@Override
	public void parse() throws IOException {
		powerId = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		responsePowerUpPickUp.setUsername(client.getPlayer().getUsername());
		int roomId = this.client.getPlayer().getRoom().getId();
		if(this.client.getServer().getGameSessionByRoomId(roomId).getPowerups(powerId)){
			//if the powerup is available, the powerId will be sent back
			responsePowerUpPickUp.setPowerId(powerId);
		}else{
			//if the powerup is not available, 0 will be sent back
			responsePowerUpPickUp.setPowerId(0);
		}
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responsePowerUpPickUp);
	}
}
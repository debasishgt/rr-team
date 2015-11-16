package networking.request;

import java.io.IOException;

import networking.response.ResponsePowerUpPickUp;

public class RequestPowerUpPickUp extends GameRequest {

	// Data
	// Responses
	private ResponsePowerUpPickUp responsePowerUpPickUp;

	public RequestPowerUpPickUp() {
		responses.add(responsePowerUpPickUp = new ResponsePowerUpPickUp());
	}

	@Override
	public void parse() throws IOException {
		
	}

	@Override
	public void doBusiness() throws Exception {
		responsePowerUpPickUp.setUsername(client.getPlayer().getUsername());
		/*
		 * When the client picks up a power up. The servers adds the power-up to
		 * the car object it has in memory.
		 */
		client.getServer().addResponseForAllOnlinePlayers(client.getId(), responsePowerUpPickUp);
	}
}
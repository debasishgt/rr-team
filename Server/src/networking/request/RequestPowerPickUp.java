package networking.request;

import java.io.IOException;

import networking.response.ResponsePowerPickUp;

public class RequestPowerPickUp extends GameRequest {

	// Data
	// Responses
	private ResponsePowerPickUp responsePowerUpPickUp;

	public RequestPowerPickUp() {
		responses.add(responsePowerUpPickUp = new ResponsePowerPickUp());
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
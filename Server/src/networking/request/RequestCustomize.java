package networking.request;

// Java Imports
import java.io.IOException;

import driver.DatabaseDriver;
import networking.response.GameResponse;
import networking.response.ResponseCustomize;
// Custom Imports
//import core.GameServer;
import utility.DataReader;
import model.Player;
import model.PlayerVehicle;
import model.Upgrade;

public class RequestCustomize extends GameRequest {

	// Data
	private String username;
	private int statisticType;
	private int carId;
	// Responses
	private ResponseCustomize responseCustomize;
	private int player_id;

	public RequestCustomize() {
		responseCustomize = new ResponseCustomize();

	}

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		statisticType = DataReader.readInt(dataInput);
		carId = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		
//		responseAuth.setAnswer((short) 1);
		
		if (client.getServer().getThreadByPlayerUserName(username) != null) {
			Player player = client.getPlayer();
			Upgrade upgrade = DatabaseDriver.getInstance().getUpgradeById(carId);
			PlayerVehicle vehicle = DatabaseDriver.getInstance().getPlayerVehicleById(carId);
			if(player.getCurrency() >= upgrade.getPrice()) {
				player.setCurrency(player.getCurrency() - upgrade.getPrice());
				player.update();
				DatabaseDriver.getInstance().addUpgradeToVehicle(upgrade.getId(), vehicle.getId());
				responseCustomize.setMessage("");
			} else {
				
			}

//			responseCustomize.setMessage(msg);
//			client.getServer().addResponseForUser(username, (GameResponse) responseCustomize); 
//			client.getPlayer().setCar_id(carId);// sets the car for the Player
		}

	}
}
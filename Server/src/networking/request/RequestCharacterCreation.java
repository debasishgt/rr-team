package networking.request;

import java.io.IOException;

import driver.DatabaseDriver;
import model.BaseVehicle;
import model.Player;
import networking.response.ResponseCharacterCreation;
import utility.DataReader;

public class RequestCharacterCreation extends GameRequest {
	// Data
		private String vehicleName;
		private int baseId;
		// Responses
		private ResponseCharacterCreation response;

		public RequestCharacterCreation() {
			responses.add(response = new ResponseCharacterCreation());

		}

		@Override
		public void parse() throws IOException {
			vehicleName = DataReader.readString(dataInput);
			baseId = DataReader.readInt(dataInput);
		}

		@Override
		public void doBusiness() throws Exception {
			Player player = client.getPlayer();
			DatabaseDriver db = DatabaseDriver.getInstance();
			BaseVehicle bVehicle = db.getBaseVehicleById(baseId);

			if(player != null && bVehicle != null && db.createNewPlayerVehicle(bVehicle, vehicleName) > 0) {
				response.setFlag(1);
				response.setPlayerVehicles(db.getPlayerVehicles(player.getID()));
			} else {
				response.setFlag(0);
			}
		}
}

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePowerUpPickUp extends GameResponse {
	private String username;
	
    public ResponsePowerUpPickUp() {
        responseCode = Constants.SMSG_POWER_PICKUP;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
      /*Construct packet*/
        return packet.getBytes();
    }

	public void setUsername(String username) {
		this.username = username;
	}
    
}
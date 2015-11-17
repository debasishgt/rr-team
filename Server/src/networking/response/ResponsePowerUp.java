package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePowerUp extends GameResponse {
	private String username;
	
    public ResponsePowerUp() {
        responseCode = Constants.SMSG_POWER_UP;
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
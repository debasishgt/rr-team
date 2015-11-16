package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseHealth extends GameResponse {
	private String username;
    public ResponseHealth() {
        responseCode = Constants.SMSG_HEALTH;
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
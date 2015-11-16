package networking.response;

import utility.GamePacket;
import metadata.Constants;

public class ResponseCollision extends GameResponse {
	private String username;
	
	public ResponseCollision() {
        responseCode = Constants.SMSG_COLLISION;
    }
	
	@Override
	public byte[] constructResponseInBytes() {
		// TODO Auto-generated method stub
		GamePacket packet = new GamePacket(responseCode);
		packet.addString(username);
		// add the data need to pass to the client here
        return packet.getBytes();
	}

	public void setUsername(String username) {
		this.username = username;
	}

}

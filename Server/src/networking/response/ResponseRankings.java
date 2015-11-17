package networking.response;

import utility.GamePacket;
import metadata.Constants;

public class ResponseRankings extends GameResponse {
	private String username;
	
	public ResponseRankings() {
        responseCode = Constants.SMSG_RANKINGS;
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

package networking.response;

import utility.GamePacket;
import metadata.Constants;
import model.Player;

public class ResponseMove extends GameResponse {
	
	private Player player;
	
	public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }
	
	@Override
	public byte[] constructResponseInBytes() {
		// TODO Auto-generated method stub
		GamePacket packet = new GamePacket(responseCode);
		packet.addString(player.getUsername());
		//add the positionss
		return packet.getBytes();
	}

	public void setPlayer(Player player) {
		this.player = player;
	}

}

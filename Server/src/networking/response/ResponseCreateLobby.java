package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseCreateLobby extends GameResponse {
	private String gameName;
	private int valid;
	public ResponseCreateLobby() {
		responseCode = Constants.SMSG_CREATE_LOBBY;
	}

	@Override
	public byte[] constructResponseInBytes() {
		GamePacket packet = new GamePacket(responseCode);
		packet.addString(gameName);
		packet.addInt32(valid);
		return packet.getBytes();
	}
	
	public void setGameName(String gameName) {
		this.gameName = gameName;
	}

	public String getGameName() {
		return this.gameName;
	}

	public void setValid(int valid) {
		this.valid = valid;
	}

	public int getValid() {
		return this.valid;
	}
}

package networking.response;

import metadata.Constants;
import utility.GamePacket;

public class ResponseCreateLobby extends GameResponse {
	private String gameName;
	private int valid;
	private String owner;
	
	public ResponseCreateLobby() {
		responseCode = Constants.SMSG_CREATE_LOBBY;
	}

	@Override
	public byte[] constructResponseInBytes() {
		GamePacket packet = new GamePacket(responseCode);
		packet.addString(gameName);
		packet.addString(owner);
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

	public void setUsername(String username) {
		this.owner = username;
	}
}

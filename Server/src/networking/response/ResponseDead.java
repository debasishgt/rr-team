package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseDead extends GameResponse {

    private long playerId;

	public ResponseDead() {
        responseCode = Constants.SMSG_DEAD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addLong(playerId);
        return packet.getBytes();
    }
    
    public long getPlayerId() {
		return playerId;
	}

	public void setPlayerId(long playerId) {
		this.playerId = playerId;
	}
}

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePowerUpUse extends GameResponse {

    private String name;
    private int powerId;

	public ResponsePowerUpUse() {
        responseCode = Constants.SMSG_CHAT;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(name);
        packet.addInt32(powerId);
        return packet.getBytes();
    }
    
    public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getPowerId() {
		return powerId;
	}

	public void setPowerId(int powerId) {
		this.powerId = powerId;
	}
}

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePowerPickUp extends GameResponse {

    private int validate;

	public ResponsePowerPickUp() {
        responseCode = Constants.SMSG_POWER_UP_PICK_UP;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(validate);
        return packet.getBytes();
    }
    
    public int getValidate() {
		return validate;
	}

	public void setValidate(int validate) {
		this.validate = validate;
	}
}

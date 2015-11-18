package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePrizes extends GameResponse {

    private int itemId; 

    public ResponsePrizes() {
        responseCode = Constants.SMSG_PRIZES;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(itemId);
        return packet.getBytes();
    }

	public int getItemId() {
		return itemId;
	}

	public void setItemId(int itemId) {
		this.itemId = itemId;
	}
    
}

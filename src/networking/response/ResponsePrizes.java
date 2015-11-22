

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePrizes extends GameResponse {

    private int itemid;

    public int getItemid() {
        return itemid;
    }

    public void setItemid(int itemid) {
        this.itemid = itemid;
    }

    
    
    public ResponsePrizes() {
        responseCode = Constants.SMSG_PRIZES;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        
        packet.addInt32(itemid);
        return packet.getBytes();
    }

    

}

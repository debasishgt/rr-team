package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseAuth extends GameResponse {

   private int message;

    public int getMessage() {
        return message;
    }

    public void setMessage(int message) {
        this.message = message;
    }

   
    public ResponseAuth() {
        responseCode = Constants.SMSG_AUTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
   
   packet.addInt32(message);
        return packet.getBytes();
    }
    
	
}

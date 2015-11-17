package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseAuth extends GameResponse {

   private String message;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public ResponseAuth() {
        responseCode = Constants.SMSG_AUTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
   packet.addString(message);
   
        return packet.getBytes();
    }
    
	
}

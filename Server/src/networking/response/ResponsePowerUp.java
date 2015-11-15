package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePowerUp extends GameResponse {

    public ResponsePowerUp() {
        responseCode = Constants.SMSG_POWER_UP;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
      /*Construct packet*/
        return packet.getBytes();
    }
    
}
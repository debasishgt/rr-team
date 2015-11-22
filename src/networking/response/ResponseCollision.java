

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseCollision extends GameResponse {

private  int validate;

    public int getValidate() {
        return validate;
    }

    public void setValidate(int validate) {
        this.validate = validate;
    }
    
    public ResponseCollision() {
        responseCode = Constants.SMSG_COLLISION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(validate);
        return packet.getBytes();
    }

    

}
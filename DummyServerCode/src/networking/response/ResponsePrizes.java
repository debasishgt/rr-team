

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePrizes extends GameResponse {

    private String username;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    
    public ResponsePrizes() {
        responseCode = Constants.SMSG_PRIZES;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        
        packet.addString(username);
        return packet.getBytes();
    }

    

}

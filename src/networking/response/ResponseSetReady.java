
package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseSetReady extends GameResponse {

 
    private String username;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    
 
    
    public ResponseSetReady() {
        responseCode = Constants.SMSG_SET_READY;
    }

    
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
    //    packet.addInt32(playerId);
        packet.addString(username);
    
        return packet.getBytes();
    }

    

}

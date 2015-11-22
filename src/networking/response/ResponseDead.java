

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseDead extends GameResponse {

 
    private String username;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    
 
    
    public ResponseDead() {
        responseCode = Constants.SMSG_DEAD;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
    //    packet.addInt32(playerId);
        packet.addString(username);
    
        return packet.getBytes();
    }

    

}

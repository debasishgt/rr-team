


package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponsePowerUpPickUp extends GameResponse {

  private int powerId;

    public int getPowerId() {
        return powerId;
    }

    public void setPowerId(int powerId) {
        this.powerId = powerId;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    private String username;   

    
   
    public ResponsePowerUpPickUp() {
        responseCode = Constants.SMSG_POWER_PICKUP;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addInt32(powerId);
        return packet.getBytes();
    }

   
}

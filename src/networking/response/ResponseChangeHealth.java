
package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseChangeHealth extends GameResponse {

   
   private String username;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
   private int healthChange;

   
    public int getHealthChange() {
        return healthChange;
    }

    public void setHealthChange(int healthChange) {
        this.healthChange = healthChange;
    }
  

    public ResponseChangeHealth() {
        responseCode = Constants.SMSG_HEALTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
      packet.addString(username);
      packet.addInt32(healthChange);
   
        return packet.getBytes();
    }
    
	
}


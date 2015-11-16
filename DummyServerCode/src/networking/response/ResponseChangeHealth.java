
package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseChangeHealth extends GameResponse {

   private String carId;

    public String getCarId() {
        return carId;
    }

    public void setCarId(String carId) {
        this.carId = carId;
    }

    public int getHealthChange() {
        return healthChange;
    }

    public void setHealthChange(int healthChange) {
        this.healthChange = healthChange;
    }
   private int healthChange;


    public ResponseChangeHealth() {
        responseCode = Constants.SMSG_HEALTH;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
      packet.addString(carId);
     // packet.addInt32(healthChange);
   
        return packet.getBytes();
    }
    
	
}


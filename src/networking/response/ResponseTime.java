package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseTime extends GameResponse {

    private int type;

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public long getTime() {
        return time;
    }

    public void setTime(long time) {
        this.time = time;
    }
    private long time;

    
    
    
    public ResponseTime() {
        responseCode = Constants.SMSG_TIME;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        
        packet.addInt32(type);
        packet.addLong(time);
        return packet.getBytes();
    }

    

}

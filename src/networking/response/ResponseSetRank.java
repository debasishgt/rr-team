


package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseSetRank extends GameResponse {

    
    
    private int rank;

    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }
    
    public ResponseSetRank() {
        responseCode = Constants.SMSG_SET_RANK;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(rank);
        
        return packet.getBytes();
    }
    
	

	
        
        
}

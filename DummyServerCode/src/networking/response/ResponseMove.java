package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseMove extends GameResponse {

    private String position;
    private String username; 

    public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
    //    packet.addString(position);
        return packet.getBytes();
    }
    
	public String getPosition() {
		return position;
	}

	public void setPosition(float x, float y, float z,float h) {
		this.position = x + "," + y + "," + z+ "," + h;
	}

	public void setUsername(String username)
	{
		this.username = username; 
	}
	public String getUsername()
	{
		return username; 
	}

}

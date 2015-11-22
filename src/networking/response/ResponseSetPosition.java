package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseSetPosition extends GameResponse {

    
    
    private int numberOfUsers;
    private String username;

private float x ;//location vector
private float y;

    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }

    public float getH() {
        return h;
    }

    public void setH(float h) {
        this.h = h;
    }
private float z;
private float h; //facing direction
    
    
    
    public ResponseSetPosition() {
        responseCode = Constants.SMSG_SET_POSITION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(numberOfUsers);
        packet.addString(username);
        packet.addFloat(x);
        packet.addFloat(y);
        packet.addFloat(z);
        packet.addFloat(h);
        
        return packet.getBytes();
    }
    
	

	public void setUsername(String username)
	{
		this.username = username; 
	}
	public String getUsername()
	{
		return username; 
	}

        public int getNumberOfUsers() 
        {
                return numberOfUsers;
        }

        public void setNumberOfUsers(int numberOfUsers) 
        {
        this.numberOfUsers = numberOfUsers;
        }

        
        
}

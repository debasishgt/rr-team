package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseMove extends GameResponse {

    
    private String username; 
    private float y;
    private float z;
    private float h;
    private float p;
    private float r; //facing direction
    private String keys;

    
    
private float x; //location vector

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

    public float getP() {
        return p;
    }

    public void setP(float p) {
        this.p = p;
    }

    public float getR() {
        return r;
    }

    public void setR(float r) {
        this.r = r;
    }

    public String getKeys() {
        return keys;
    }

    public void setKeys(String keys) {
        this.keys = keys;
    }

    
    
    
    public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addFloat(x);
        packet.addFloat(y);
        packet.addFloat(z);
        packet.addFloat(h);
        packet.addFloat(p);
        packet.addFloat(r);
        packet.addString(keys);
        
        //    packet.addString(position);
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

}

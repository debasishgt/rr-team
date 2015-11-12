package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseMove extends GameResponse {

	private Double x;
	private Double y;
	private Double z;
	private Double h;
    private String keys;
    private String username;

	public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(username);
        packet.addDouble(x);
        packet.addDouble(y);
        packet.addDouble(z);
        packet.addDouble(h);
        packet.addString(keys);
        return packet.getBytes();
    }
    
    public Double getX() {
		return x;
	}

	public void setX(Double x) {
		this.x = x;
	}

	public Double getY() {
		return y;
	}

	public void setY(Double y) {
		this.y = y;
	}

	public Double getZ() {
		return z;
	}

	public void setZ(Double z) {
		this.z = z;
	}

	public Double getH() {
		return h;
	}

	public void setH(Double h) {
		this.h = h;
	}

	public String getKeys() {
		return keys;
	}

	public void setKeys(String keys) {
		this.keys = keys;
	}
	
	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

}

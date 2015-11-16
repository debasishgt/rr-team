package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseCollision extends GameResponse {

    private int damage;

	public ResponseCollision() {
        responseCode = Constants.SMSG_COLLISION;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(damage);
        return packet.getBytes();
    }
    
    public int getDamage() {
		return damage;
	}

	public void setDamage(int damage) {
		this.damage = damage;
	}
}

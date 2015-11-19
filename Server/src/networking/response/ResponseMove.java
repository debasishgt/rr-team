package networking.response;

import utility.GamePacket;
import metadata.Constants;

public class ResponseMove extends GameResponse {
	
	private String username;
	private float x, y, z, h;
	
	public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }
	
	public void setPosition(float x, float y, float z, float h){
		this.x=x;
		this.y=y;
		this.z=z;
		this.h=h;
	}
	
	public void setUsername(String username) {
        this.username = username;
    }
	
	@Override
	public byte[] constructResponseInBytes() {
		// TODO Auto-generated method stub
		GamePacket packet = new GamePacket(responseCode);
		packet.addString(username+" moved");
		//add the positionss
		return packet.getBytes();
	}

}

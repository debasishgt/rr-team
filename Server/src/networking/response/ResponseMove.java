package networking.response;

import utility.GamePacket;
import metadata.Constants;

public class ResponseMove extends GameResponse {
	
	private String username;
	private float x, y, h;
	private boolean isMoving;
	
	public ResponseMove() {
        responseCode = Constants.SMSG_MOVE;
    }
	
	public void setPosition(float x, float y, float h){
		this.x=x;
		this.y=y;
		this.h=h;
	}
	
	public void setIsMoving(boolean m){
		this.isMoving = m;
	}
	
	public void setSenderUsername(String username_that_moved) {
        this.username = username_that_moved;
    }
	
	@Override
	public byte[] constructResponseInBytes() {
		// TODO Auto-generated method stub
		GamePacket packet = new GamePacket(responseCode);
		//packet.addString(username);
		//add the positionss
		return packet.getBytes();
	}

}

package networking.response;

import utility.GamePacket;
import java.util.Map;
import metadata.Constants;

public class ResponseReady extends GameResponse {
	private Map<String, Integer> status;
	
	public ResponseReady() {
        responseCode = Constants.SMSG_READY;
    }
	
	@Override
	public byte[] constructResponseInBytes() {
		// TODO Auto-generated method stub
		GamePacket packet = new GamePacket(responseCode);
		packet.addInt32(status.size());
		
		for(String username : status.keySet())
		{
			packet.addString(username);
			packet.addInt32(status.get(username));
		}
		// add the data need to pass to the client here
        return packet.getBytes();
	}
	public void setStatus(Map<String, Integer> status) {
		this.status = status;
	}
}

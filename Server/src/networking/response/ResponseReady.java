package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseReady extends GameResponse {

    private int numberOfUsers;

	public ResponseReady() {
        responseCode = Constants.SMSG_READY;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        
        //calls session and returns the list of users
        
        //Loop through list and add their name and status
        
        return packet.getBytes();
    }
    
    public int getNumberOfUsers() {
		return numberOfUsers;
	}

	public void setNumberOfUsers(int numberOfUsers) {
		this.numberOfUsers = numberOfUsers;
	}
}

package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseReady extends GameResponse {

    private int  numberOfUsers;

    public int getNumberOfUsers() {
        return numberOfUsers;
    }

    public void setNumberOfUsers(int numberOfUsers) {
        this.numberOfUsers = numberOfUsers;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    private String username;
    private int status;
    
  


    public ResponseReady() {
        responseCode = Constants.SMSG_READY;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(numberOfUsers);
        packet.addString(username);
        packet.addInt32(status);
        return packet.getBytes();
    }
    

}

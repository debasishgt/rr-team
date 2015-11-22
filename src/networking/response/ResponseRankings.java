package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseRankings extends GameResponse {

    private int  number_of_players;
    
    public int getNumber_of_players() {
        return number_of_players;
    }

    public void setNumber_of_players(int number_of_players) {
        this.number_of_players = number_of_players;
    }



    public ResponseRankings() {
        responseCode = Constants.SMSG_RANKINGS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(number_of_players);
        return packet.getBytes();
    }
    

}

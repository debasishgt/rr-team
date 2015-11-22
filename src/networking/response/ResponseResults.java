package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseResults extends GameResponse {

    private int place;
    
    private int number_of_players;

    
    public int getNumber_of_players() {
        return number_of_players;
    }

    public void setNumber_of_players(int number_of_players) {
        this.number_of_players = number_of_players;
    }


    public int getPlace() {
        return place;
    }

    public void setPlace(int place) {
        this.place = place;
    }
    

    public ResponseResults() {
        responseCode = Constants.SMSG_RESULTS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(place);
        packet.addInt32(number_of_players);
        return packet.getBytes();
    }
    

}

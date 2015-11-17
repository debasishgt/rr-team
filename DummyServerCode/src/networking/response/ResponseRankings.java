package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class ResponseRankings extends GameResponse {

    private short type;

    private String msg;

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }
    
    public short getType() {
        return type;
    }

    public void setType(short type) {
        this.type = type;
    }
    
    private int number_of_players;

    
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
   //     packet.addShort16(type);
     //   packet.addInt32(number_of_players);
        packet.addString(msg);
        return packet.getBytes();
    }
    

}

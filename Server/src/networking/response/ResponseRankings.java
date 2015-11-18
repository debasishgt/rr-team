package networking.response;

import java.util.List;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;
import utility.Player;

public class ResponseRankings extends GameResponse {

	private List<Player> players;

    public ResponseRankings() {
        responseCode = Constants.SMSG_RANKINGS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(players.size());
        
        for(Player player : players)
        {
        	packet.addString(player.getUsername());
        	//packet.addInt32(session.getRank(player));
        }
        return packet.getBytes();
    }
    
    public List<Player> getPlayers() {
		return players;
	}

	public void setPlayers(List<Player> players) {
		this.players = players;
	}
}

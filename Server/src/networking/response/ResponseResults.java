package networking.response;

import java.util.List;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;
import utility.Player;

public class ResponseResults extends GameResponse {

    private List<Player> players;

    public ResponseResults() {
        responseCode = Constants.SMSG_RESULTS;
    }

    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addInt32(players.size());
        
        for(Player player : players)
        {
        	packet.addString(player.getUsername());
        	//packet.addInt32(session.getScore(player));
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

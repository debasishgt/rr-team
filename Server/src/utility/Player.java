package utility;

import model.GameRoom;

public class Player {

	private String username;
	private int player_id;
	private String character;
	private GameRoom room = null;

	public Player(String username, int player_id) {
		this.username = username;
		this.player_id = player_id;
	}
	
	public void setRoom(GameRoom room) {
		this.room = room;
	}
	
	public GameRoom getRoom() {
		return room;
	}

	public String getUsername() {
		return this.username;
	}

	public String getCharacter() {
		return this.character;
	}

	public void setCharacter(String character) {
		this.character = character;
	}
	
	public int getID()
	{
		return this.player_id;
	}
}

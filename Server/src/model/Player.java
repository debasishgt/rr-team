package model;

public class Player {
	private int player_id;
	private String username;	
	private String email;
	private GameRoom room = null;

	public Player(int player_id, String username, String email) {
		this.player_id = player_id;
		this.username = username;
		this.email = email;
		
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
	
	public String getEmail() {
		return this.email;
	}
	
	public int getID() {
		return this.player_id;
	}
}

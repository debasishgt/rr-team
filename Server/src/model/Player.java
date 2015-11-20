package model;

public class Player {
	private int player_id;
	private String username;	
	private String email;
	private GameRoom room = null;
	private Position pos;
	
	public Player(int player_id,String username) {
		this.username = username;
		this.player_id = player_id;
		this.pos = new Position();
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
	
	public Position getPosition(){
		return pos;
	}
	
	public void setPosition(float x, float y, float z, float h){
		pos.setX(x);
		pos.setY(y);
		pos.setZ(z);
		pos.setH(h);
	}
}

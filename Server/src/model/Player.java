package model;

public class Player {

	private String username;
	private int player_id;
	private String character;
	private GameRoom room = null;
	private Position pos;
	
	public Player(String username, int player_id) {
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

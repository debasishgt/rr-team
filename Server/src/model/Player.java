package model;

public class Player {
	private int player_id;
	private String username;	
	private String email;
	private GameRoom room = null;
	private Position pos;
	private boolean isReady;
	private int carId;
	
	public Player(int player_id,String username) {
		this.username = username;
		this.player_id = player_id;
		this.pos = new Position();
		this.isReady = false;
	}
	
	public void setRoom(GameRoom room) {
		this.isReady = false;
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
	
	public void setPosition(float x, float y, float z, float h, float p, float r){
		pos.setX(x);
		pos.setY(y);
		pos.setZ(z);
		pos.setH(h);
		pos.setP(p);
		pos.setZ(r);
	}

	public boolean isReady() {
		return isReady;
	}
	public void setReady() {
		this.isReady = true;
	}
	public void setNotReady(){
		this.isReady = false;
	}

	public void setCar_id(int carId) {
		this.carId = carId;
		
	}
	
	public int getCarId(int carId) {
		return this.carId;		
	}

	public int getCurrency() {
		// TODO Auto-generated method stub
		return 0;
	}

	public void setCurrency(int i) {
		// TODO Auto-generated method stub
		
	}

	public void update() {
		// TODO Auto-generated method stub
		
	}
}

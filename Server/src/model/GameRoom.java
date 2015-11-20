package model;

import driver.DatabaseDriver;

public class GameRoom {
	private int id;
	private int type;
	private long time_started;
	private String map_name;
	private String room_name;
	
	public GameRoom(int id, int type, long time_started, String map_name, String room_name) {
		this.id = id;
		this.time_started = time_started;
		this.map_name = map_name;
		this.room_name = room_name;
	}

	public int getType() {
		return type;
	}

	public void setType(int type) {
		this.type = type;
	}

	public long getTimeStarted() {
		return time_started;
	}

	public void setTimeStarted(long time_started) {
		this.time_started = time_started;
	}

	public String getMapName() {
		return map_name;
	}

	public void setMapName(String map_name) {
		this.map_name = map_name;
	}

	public int getId() {
		return id;
	}
	
	public void update() {
		DatabaseDriver dbDriver = DatabaseDriver.getInstance();
		dbDriver.updateGame(this);
	}

	public String getRoomName() {
		return room_name;
	}

	public void setRoomName(String game_name) {
		this.room_name = game_name;
	}
}

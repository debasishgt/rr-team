package model;

import driver.DatabaseDriver;

public class Game {
	private int id;
	private int type;
	private long time_started;
	private String map_name;
	
	public Game(int id, int type, long time_started, String map_name) {
		this.id = id;
		this.time_started = time_started;
		this.map_name = map_name;
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
}

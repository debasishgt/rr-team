package core;

import networking.response.ResponseReady;
import driver.DatabaseDriver;
import metadata.Constants;
import model.GameRoom;

public class GameSession extends Thread{
	private GameRoom gameroom;
	private GameServer server;
	private boolean isRunning;
	private boolean gameStarted;
	private long[] powerups;
	
	public GameSession(GameServer server){
		GameRoom gameRoom = null;
		while(gameRoom == null) {
			String roomName = "Room #" + ((int)(Math.random()*100000));
			gameRoom = DatabaseDriver.getInstance().getGameByName(roomName);
			if(gameRoom == null) {
				DatabaseDriver.getInstance().createGame(0, System.currentTimeMillis()/1000, "", roomName, 0);
				gameRoom = DatabaseDriver.getInstance().getGameByName(roomName);
			} else {
				gameRoom = null;
			}
		}
		this.gameroom = gameRoom;
		this.server = server;
	}
	
	public GameSession(GameServer server, GameRoom gameRoom){
		this.gameroom = gameRoom;
		this.server = server;
	}
	
	@Override
	public void run() {
		isRunning = true;
		gameStarted = false;
		long currentTime, gameRunTime;
		boolean eliminate = false;
		while(isRunning){
			currentTime = System.currentTimeMillis();
			if(gameStarted){
				gameRunTime = currentTime - gameroom.getTimeStarted();
				//everyone is ready and game started
			}
		}
		System.out.println("Game Over : GameId - " + getId());
		server.deleteSessionThreadOutOfActiveThreads(getId());
	}

	public GameRoom getGameroom() {
		return gameroom;
	}
	public void setGameStarted(boolean gameStarted){
		this.gameStarted = gameStarted;
	}
	
	public void setGameroom(GameRoom gameroom) {
		this.gameroom = gameroom;
	}

	public GameServer getServer() {
		return server;
	}
	
	public void sendAllResponseReady() {
		for(GameClient gclient : server.getGameClientsForRoom(gameroom.getId())){
			ResponseReady responseReady = new ResponseReady();
			responseReady.setUsername(gclient.getPlayer().getUsername());
			gclient.addResponseForUpdate(responseReady);
		}
	}

	public void gameStart() {
		//send set_position response here
		//remember to edit all gameclients.player.position
		sendAllResponseReady();
		getGameroom().setTimeStarted(System.currentTimeMillis());
		initPowerUp(getGameroom().getTimeStarted());
		setGameStarted(true);
	}

	private void initPowerUp(long l) {
		this.powerups = new long[Constants.NUMBER_OF_POWERUPS];
		for(int i=0; i<Constants.NUMBER_OF_POWERUPS; i++){
			powerups[i] = l - Constants.RESPAWN_TIME;
		}
	}

	public boolean getPowerups(int powerId) {
		long cur = System.currentTimeMillis();
		if(cur - powerups[powerId] >= Constants.RESPAWN_TIME){
			powerups[powerId] = cur;
			return true;
		}else{
			return false;
		}
	}
	
	
}


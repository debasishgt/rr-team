package core;

import networking.response.ResponseReady;
import metadata.Constants;
import model.GameRoom;

public class GameSession extends Thread{
	private GameRoom gameroom;
	private GameServer server;
	private boolean isRunning;
	private boolean gameStarted;
	private long[] powerups;
	
	public GameSession(GameServer server){
		this.gameroom = new GameRoom();
		this.server = server;
	}
	
	@Override
	public void run() {
		isRunning = true;
		gameStarted = false;
		long currentTime;
		while(isRunning){
			currentTime = System.currentTimeMillis();
			if(gameStarted){
				//everyone is ready and game started
				//gameroom.getstart_time will have the correct start_time
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


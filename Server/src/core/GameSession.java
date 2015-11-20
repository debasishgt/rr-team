package core;

import networking.response.ResponseReady;
import model.GameRoom;

public class GameSession extends Thread{
	private GameRoom gameroom;
	private GameServer server;
	private boolean isRunning;
	private boolean gameStarted;
	
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
}


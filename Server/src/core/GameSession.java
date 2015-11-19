package core;

import model.GameRoom;

public class GameSession extends Thread{
	private GameRoom gameroom;
	
	public GameSession(){
		gameroom = new GameRoom();
	}
}


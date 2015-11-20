package networking.request;

import java.io.IOException;

import core.GameSession;
import driver.DatabaseDriver;
import model.GameRoom;
import networking.response.ResponseCreateLobby;
import utility.DataReader;

public class RequestCreateLobby extends GameRequest {
	private String room_name;
	private int status;
	private ResponseCreateLobby response;
	
	public RequestCreateLobby() {
		responses.add(response = new ResponseCreateLobby());
	}
	@Override
	public void parse() throws IOException {		
		room_name = DataReader.readString(dataInput);
		int gameid = DataReader.readInt(dataInput); //Dont need
		status = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		GameRoom gameRoom = DatabaseDriver.getInstance().getGameByName(room_name);
		
		if(gameRoom == null) {
			DatabaseDriver.getInstance().createGame(0, System.currentTimeMillis()/1000, "",room_name,status);
			gameRoom = DatabaseDriver.getInstance().getGameByName(room_name);
			client.getPlayer().setRoom(gameRoom);
			response.setValid(1);
			
			GameSession session = new GameSession(client.getServer(),gameRoom);
			client.getServer().addToActiveSessions(session);
			response.setGameName(room_name);
			response.setUsername(client.getPlayer().getUsername());
			client.getServer().addResponseForAllOnlinePlayers(client.getId(), response);
		} else {
			response.setValid(0);
		}
	}
}

package networking.request;

import java.io.IOException;

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
		String username = DataReader.readString(dataInput);
		status = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		GameRoom gameRoom = DatabaseDriver.getInstance().getGameByName(room_name);
		
		if(gameRoom == null) {
//			DatabaseDriver.getInstance().createGame(0, System.currentTimeMillis()/1000, "");
//			GameRoom gameRoom = DatabaseDriver.getInstance().getGameByName(room_name);
//			client.getPlayer().setRoom(gameRoom);			
//			response.setValid(1);
//			response.setUsername(client.getPlayer().getUsername());
//			client.getServer().addResponseForRoomExcludingPlayer(gameRoom.getId(), client.getPlayer().getID(), response);
		} else {
			response.setValid(0);
		}
	}
}

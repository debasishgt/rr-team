package networking.request;

import java.io.IOException;

import driver.DatabaseDriver;
import networking.response.ResponseResults;
import utility.DataReader;

public class RequestResults extends GameRequest {

	// Data
	private int gameId;
	// Responses
	private ResponseResults responseResults;

	public RequestResults() {
		responses.add(responseResults = new ResponseResults());
	}

	@Override
	public void parse() throws IOException {
		gameId = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
		responseResults.setRankings(DatabaseDriver.getInstance().getPlayersRankingForGame(gameId));
	}
}
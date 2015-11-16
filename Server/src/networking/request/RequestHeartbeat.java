package networking.request;

import java.io.IOException;
import java.util.Queue;
import networking.response.GameResponse;

public class RequestHeartbeat extends GameRequest {
	public RequestHeartbeat() {}

	@Override
	public void parse() throws IOException {
		
	}

	@Override
	public void doBusiness() throws Exception {
		Queue<GameResponse> response_queue = this.client.getUpdates();
		
		while(!response_queue.isEmpty()){
			responses.add(response_queue.poll());
		}
	}
}

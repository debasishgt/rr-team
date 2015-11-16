package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.ResponseInt;
import networking.response.*;
import utility.DataReader;

public class RequestCharacterCreation extends GameRequest {

    


	// Data
	private String characterName;
	private int classType;
     
	// Responses
        private CharacterCreationResponse characterCreationResponse;

	public RequestCharacterCreation() {
		responses.add(characterCreationResponse = new CharacterCreationResponse());

        }

	@Override
	public void parse() throws IOException {
		characterName = DataReader.readString(dataInput);
		classType = DataReader.readInt(dataInput);
	}

	@Override
	public void doBusiness() throws Exception {
System.out.println("name=="+characterName);
System.out.println("classType=="+classType);
     characterCreationResponse.setCharacterName("create character");
        }
}

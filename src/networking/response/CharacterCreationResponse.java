
package networking.response;

// Custom Imports
import metadata.Constants;
import utility.GamePacket;

public class CharacterCreationResponse extends GameResponse {

   
    private String characterName;
    private int classType;
    private int id;

    public CharacterCreationResponse() {
        responseCode = Constants.SMSG_CREATE_CHARACTER;
    }

    
    
    @Override
    public byte[] constructResponseInBytes() {
        GamePacket packet = new GamePacket(responseCode);
        packet.addString(characterName);
        packet.addInt32(classType);
        return packet.getBytes();
    }

    
    
    
    public String getCharacterName() {
        return characterName;
    }

    public void setCharacterName(String characterName) {
        this.characterName = characterName;
    }

    public int getClassType() {
        return classType;
    }

    public void setClassType(int classType) {
        this.classType = classType;
    }

    

    
    

}


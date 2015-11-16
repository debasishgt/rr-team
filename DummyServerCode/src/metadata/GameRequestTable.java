package metadata;

// Java Imports
import java.util.HashMap;

// Custom Imports
import networking.request.GameRequest;

/**
 * The GameRequestTable class stores a mapping of unique request code numbers
 * with its corresponding request class.
 */
public class GameRequestTable {

    private static HashMap<Short, Class> requestNames; // Stores request classes by request codes

    /**
     * Initialize the hash map by populating it with request codes and classes.
     */
    public static void init() {
        requestNames = new HashMap<Short, Class>();

        // Populate the hash map using request codes and class names
      
        
       
         
        add(Constants.CMSG_AUTH, "RequestLogin"); 
        add(Constants.CMSG_MOVE, "RequestMove");
        add(Constants.CMSG_POWER_UP, "RequestPowerUpUse");
        add(Constants.CMSG_RANKINGS, "RequestRankings");
        add(Constants.CMSG_PRIZES, "RequestPrizes");
        add(Constants.CMSG_RESULTS, "RequestResults");
        add(Constants.CMSG_POWER_PICKUP, "RequestPowerUpPickUp");
        add(Constants.CMSG_CREATE_CHARACTER,"RequestCharacterCreation");
        add(Constants.CMSG_COLLISION, "RequestCollision");
        add(Constants.CMSG_DEAD, "RequestDead");
        add(Constants.CMSG_HEALTH, "RequestChangeHealth");

        
        
    /*    
        add(Constants.CMSG_DISCONNECT,"RequestDisconnect");//
        add(Constants.CMSG_REGISTER, "RequestRegister");
        add(Constants.CMSG_FORGOT_PASSWORD,"RequestForgotPassword");
        
        add(Constants.CMSG_CHAT, "RequestChat");
        
        add(Constants.CMSG_ENTER_LOBBY, "RequestEnterLobby");
        add(Constants.CMSG_ENTER_GAME_LOBBY, "RequestEnterGameLobby");
        add(Constants.CMSG_ENTER_GAME_NAME, "RequestEnterGameName");
        add(Constants.CMSG_CREATE_LOBBY, "RequestCreateLobby");
        add(Constants.CMSG_PRIVATE_CHAT, "RequestChat");
        add(Constants.CMSG_INVITE, "RequestInvite");
        add(Constants.CMSG_CAR_CHOICE, "RequestCarChoice");
        add(Constants.CMSG_CAR_PAINT, "RequestCarPaint");
        add(Constants.CMSG_CAR_TIRES, "RequestCarTires");
        add(Constants.CMSG_GARAGE_PURCHASE, "RequestGaragePurchase");
        
        add(Constants.CMSG_READY, "RequestReady");
        add(Constants.REQ_HEARTBEAT, "RequestHeartBeat");

        
        
        
        
        
        
        
    
    */
        
        add(Constants.RAND_INT, "RequestInt");
        add(Constants.RAND_SHORT, "RequestShort");
        add(Constants.RAND_STRING, "RequestString");
        add(Constants.RAND_FLOAT, "RequestFloat");
       
    
    }

    /**
     * Map the request code number with its corresponding request class,
     * derived from its class name using reflection, by inserting the pair into
     * the hash map.
     * 
     * @param code a value that uniquely identifies the request type
     * @param name a string value that holds the name of the request class
     */
    public static void add(short code, String name) {
        try {
            requestNames.put(code, Class.forName("networking.request." + name));
        } catch (ClassNotFoundException e) {
            System.err.println(e.getMessage());
        }
    }

    /**
     * Get the instance of the request class by the given request code.
     * 
     * @param requestID a value that uniquely identifies the request type
     * @return the instance of the request class
     */
    public static GameRequest get(short requestID) {
        GameRequest request = null;

        try {
            Class name = requestNames.get(requestID);

            if (name != null) {
                request = (GameRequest) name.newInstance();
                request.setID(requestID);
            } else {
                System.err.println("Invalid Request Code: " + requestID);
            }
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        return request;
    }
}

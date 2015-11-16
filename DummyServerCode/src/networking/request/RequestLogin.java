package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;

import utility.DataReader;
import networking.response.*;

public class RequestLogin extends GameRequest {

	// Data
	private String username;
	private String password;

        
        private ResponseAuth responseAuth;
	public RequestLogin() {
		responses.add(responseAuth = new ResponseAuth());
	
        }

	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		password = DataReader.readString(dataInput);
           
	}

	@Override
	public void doBusiness() throws Exception {

            	System.out.println("username=="+username);
              	System.out.println("password=="+password);
        
                
             if(username!=null && password!=null)   
            responseAuth.setMessage("auth");
           
            /*    
		Connexion db = new Connexion();

		if (db.checkAuth(username, password)) {
			System.out.println("Database Connected !");
			responseInt.setNumber(1);
		} else {
			System.out.println("Wrong credentials");
			responseInt.setNumber(0);
		}
*/
	}
}

package networking.request;

import java.io.IOException;
import driver.DatabaseDriver;
import model.Player;
import utility.DataReader;
import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import javax.activation.*;

/**
 * Client requests for their account information to be email 
 * to them. The server check the Username and Email to see 
 * if they match an account and email the user their account 
 * Information.
 *
 */
public class RequestAccountInformation extends GameRequest {
	private String username;
	private String email;
	 
	@Override
	public void parse() throws IOException {
		username = DataReader.readString(dataInput);
		email = DataReader.readString(dataInput);

	}

	@Override
	public void doBusiness() throws Exception {
		// TODO Auto-generated method stub
		Player player1 = DatabaseDriver.getInstance().getPlayerByUsername(username);
		Player player2 = DatabaseDriver.getInstance().getPlayerByEmail(email);
		
		if(!(player1 == null && player2 == null) && !(player1 != null && player2 != null && player1.getEmail() != player2.getEmail())) {
			if(player1.getEmail() == player2.getEmail() || (player1 != null && player2 == null)) {
				sendMail(player1);
			} else {
				sendMail(player2);
			}
		}
	}

	private void sendMail(Player player) {
	
	}
}

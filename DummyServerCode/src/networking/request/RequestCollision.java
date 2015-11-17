/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



package networking.request;

// Java Imports
import java.io.IOException;

// Custom Imports
//import core.GameServer;
import networking.response.*;
import utility.DataReader;

public class RequestCollision extends GameRequest {

    // Data
    private int playerId;
    private int damage;

 
    // Responses
        private ResponseCollision responseCollision;
    
    
    public RequestCollision() {
                responses.add(responseCollision = new ResponseCollision());
    
    }

    @Override
    public void parse() throws IOException {
        playerId = DataReader.readInt(dataInput);
        damage = DataReader.readInt(dataInput);
    }

    @Override
    public void doBusiness() throws Exception {
        
         System.out.println("playerId=="+playerId);
          System.out.println("damage=="+damage);
        responseCollision.setMsg("collision");
   
    }
}



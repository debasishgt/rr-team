
package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.GameResponse;
import networking.response.*;
// Custom Imports
//import core.GameServer;
import utility.DataReader;

public class RequestMove extends GameRequest {

	// Data
	private String keys,data;
	private float x, y, z, h;
	// Responses
	private ResponseMove responseMove;
        
	public RequestMove() {

	 responses.add(responseMove = new ResponseMove());

	

	}

	@Override
	public void parse() throws IOException {
           
            x=DataReader.readFloat(dataInput);
            y=DataReader.readFloat(dataInput);
            z=DataReader.readFloat(dataInput);
            h=DataReader.readFloat(dataInput);
            keys=DataReader.readString(dataInput);
            
         //   data = DataReader.readString(dataInput);
	//	String[] parts = data.split(",");
		try {
            //            x=Float.parseFloat(parts[0]);
		//	y=Float.parseFloat(parts[1]);
                  //      z=Float.parseFloat(parts[2]);
                       
                    //    h=  Float.parseFloat(parts[3]);
		
                
                } catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	public void doBusiness() throws Exception {
          System.out.println("x="+x);
          System.out.println("y="+y);
          System.out.println("z="+z);
          System.out.println("z="+h);
          System.out.println("keys="+keys);
          
         // if(keys!=null)
	  responseMove.setUsername("move");
          responseMove.setX(1);
          responseMove.setY(2);
          responseMove.setZ(3);
          responseMove.setH(4);
          responseMove.setP(5);
          responseMove.setR(6);
          responseMove.setKeys("keys");
         
       	}
}

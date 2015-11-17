package driver;

import java.sql.*;
import java.util.*;

import utility.ConfFileParser;
import utility.Player;
import configuration.GameServerConf;

//Singleton
public class DatabaseDriver {
	private static DatabaseDriver Instance = null;
	protected Connection conn;
	protected GameServerConf configuration;

	public String userName = "";
	public String password = "";
	public String serverName = "";
	public String databaseName = "";
	public int portNumber = 3306;

	public static DatabaseDriver getInstance() {
		if(Instance == null) {
			Instance = new DatabaseDriver();
		}
		
		return Instance;
	}
	protected DatabaseDriver() {
		configuration = new GameServerConf();
		ConfFileParser confFileParser = new ConfFileParser("gameServer.conf");
       	configuration.setConfRecords(confFileParser.parse());
       	
       	userName = configuration.getDatabaseUsername();
		password = configuration.getDatabasePassword();
		serverName = configuration.getDatabaseHost();
		portNumber = configuration.getDatabasePort();
		databaseName = configuration.getDatabaseName();
		
		System.out.println("username: " + userName);
		System.out.println("password: " + password);
		System.out.println("server: " + serverName);
		System.out.println("port: " + portNumber);
		
		connect();
	}

	// close the connection
	public void close() {
		try {
			conn.close();
		} catch (Exception e) {
			System.out.println("exception in close :" + e);
		}
	}
	
	protected void connect() {
		try {
			Properties connectionProps = new Properties();

			// setproperty only accept the string.
			
			connectionProps.setProperty("user", this.userName);
			connectionProps.setProperty("password", this.password);

			conn = DriverManager.getConnection("jdbc:mysql://" + this.serverName + ":" + this.portNumber + "/"+databaseName,connectionProps);

		} catch (Exception e) {
			System.out.println("Connection failure with the database :" + e);
			e.printStackTrace();
			System.exit(1);
		}
	}
	
	protected void checkConnection() {
		try {
			if(conn.isClosed()) {
				connect();
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	//Creating a new player in the database
	public int createPlayer(String username, String password) {
		try {
			checkConnection();			
			String selectSQL = "INSERT INTO players (user_name, user_password) VALUES (?, ?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, username);
			preparedStatement.setString(2, password);
			preparedStatement.executeUpdate();
			return getPlayerID(username);

		} catch (Exception e) {
			e.printStackTrace();
			return 0;
		}

	}

	// Player authentication
	public int checkPlayerAuth(String username, String password) {
		try {
			checkConnection();
			String selectSQL = "SELECT id FROM players WHERE user_name=? AND user_password =?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, username);
			preparedStatement.setString(2, password);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				return rs.getInt("id");
			}
			return -1;
		} catch(SQLException e) {
			return -1;
		}

	}

	//Get player ID from username (on creating)
	public int getPlayerID(String username) {
		try {
			checkConnection();
			String selectSQL = "SELECT id FROM players WHERE user_name = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, username);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				return rs.getInt("id");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return 0;
	}
	
	//Get friend ids for player
	public List<Integer> getFriendIdsForPlayer(int playerId) {
		try {
			checkConnection();
			ArrayList<Integer> list = new ArrayList<Integer>();			
			String selectSQL = "SELECT friend_id FROM friend_relationships WHERE player_id = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				list.add(rs.getInt("friend_id"));
			}
			return list;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return new ArrayList<Integer>();
	}
	
	//Get friends for player
	public List<Player> getFriendsForPlayer(int playerId) {
		try {
			checkConnection();
			ArrayList<Player> list = new ArrayList<Player>();
			String selectSQL = "(SELECT p.id,p.user_name FROM players p LEFT JOIN friends_relationships f ON (p.id = f.player_id) WHERE p.player_id = ?) UNION ALL (SELECT p.id,p.user_name FROM players p LEFT JOIN friends_relationships f ON (p.id = f.friend_id) WHERE p.player_id = ?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			preparedStatement.setInt(2, playerId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				list.add(new Player(rs.getString("p.user_name"),rs.getInt("p.id")));
			}
			return list;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return new ArrayList<Player>();
		
	}
	
	//Get friends for player
	public int addFriends(int playerId, int friendId) {
		try {
			checkConnection();
			String selectSQL = "INSERT INTO friend_relationship VALUES(?,?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			preparedStatement.setInt(2, friendId);
			return preparedStatement.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return 0;
	}
}
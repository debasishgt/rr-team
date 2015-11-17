package driver;

import java.sql.*;
import java.util.*;

import utility.ConfFileParser;
import utility.Player;
import configuration.GameServerConf;

//Singleton
public class DatabaseDriver {
	protected final String BASE_VEHICLE = "base_vehicles";
	protected final String DD_GAME_RANKINGS = "dd_game_rankings";
	protected final String FRIENDS_RELATIONSHIP = "friends_relationship";
	protected final String GAMES = "games";
	protected final String PLAYER_POWERUPS = "player_powerups";
	protected final String PLAYER_VEHICLES = "player_vehicles";
	protected final String PLAYERS = "players";
	protected final String POWERUPS = "powerups";
	protected final String RR_GAME_RANKINGS = "rr_game_rankings";
	protected final String UPGRADES = "upgrades";
	
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
			String selectSQL = "INSERT INTO "+PLAYERS+" (user_name, user_password) VALUES (?, ?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, username);
			preparedStatement.setString(2, password);
			preparedStatement.executeUpdate();
			preparedStatement.close();
			return getPlayerID(username);
		} catch (Exception e) {
			e.printStackTrace();
			return 0;
		}

	}

	// Player authentication
	public int checkPlayerAuth(String username, String password) {
		int ret = -1;
		try {
			checkConnection();
			
			String selectSQL = "SELECT id FROM "+PLAYERS+" WHERE user_name=? AND user_password =? LIMIT 0,1";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, username);
			preparedStatement.setString(2, password);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				ret = rs.getInt("id");
				break;
			}
			rs.close();
			preparedStatement.close();
		} catch(SQLException e) {
			e.printStackTrace();
		}
		return ret;
	}

	//Get player ID from username (on creating)
	public int getPlayerID(String username) {
		int ret = 0;
		try {
			checkConnection();
			String selectSQL = "SELECT id FROM "+PLAYERS+" WHERE user_name = ? LIMIT 0,1";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, username);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				ret = rs.getInt("id");
				break;
			}
			rs.close();
			preparedStatement.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}

	//Get friend ids for player
	public List<Integer> getFriendIdsForPlayer(int playerId) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		try {
			checkConnection();
						
			String selectSQL = "SELECT friend_id,player_id FROM "+FRIENDS_RELATIONSHIP+" WHERE player_id = ? OR friend_id = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			preparedStatement.setInt(2, playerId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				if(rs.getInt("friend_id") != playerId)
					list.add(rs.getInt("friend_id"));
				else
					list.add(rs.getInt("player_id"));
			}
			rs.close();
			preparedStatement.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return list;
	}

	//Get friends for player
	public List<Player> getFriendsForPlayer(int playerId) {
		ArrayList<Player> list = new ArrayList<Player>();
		try {
			checkConnection();
			
			String selectSQL = "SELECT p.id,p.user_name FROM "+PLAYERS+" p LEFT JOIN "+FRIENDS_RELATIONSHIP+" f1 ON (p.id = f1.player_id) LEFT JOIN "+FRIENDS_RELATIONSHIP+" f2 ON (p.id = f2.friend_id) WHERE f1.friend_id = ? OR f2.player_id = ? GROUP BY p.id";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			preparedStatement.setInt(2, playerId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				list.add(new Player(rs.getString("p.user_name"),rs.getInt("p.id")));
			}
			rs.close();
			preparedStatement.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return list;
	}

	//Get friends for player
	public int addFriends(int playerId, int friendId) {
		try {
			checkConnection();
			String selectSQL = "INSERT INTO "+FRIENDS_RELATIONSHIP+" (player_id,friend_id) VALUES(?,?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			preparedStatement.setInt(2, friendId);
			int ret = preparedStatement.executeUpdate();
			preparedStatement.close();
			return ret;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return 0;
	}

	//Create game
	public int createGame(int gameType, long timestamp, String mapName) {
		try {
			checkConnection();
			String selectSQL = "INSERT INTO "+GAMES+" (type,time_started,map_name) VALUES(?,?,?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, gameType);
			preparedStatement.setLong(2, timestamp);
			preparedStatement.setString(2, mapName);
			int ret = preparedStatement.executeUpdate();
			preparedStatement.close();
			return ret;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return 0;
	}

	//Get friends for player
	public List<Player> getPlayersForGameId(int gameId) {
		return null;
	}
}
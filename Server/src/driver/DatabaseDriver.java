package driver;

import java.sql.*;
import java.util.*;

import utility.ConfFileParser;
import utility.Player;
import configuration.GameServerConf;
import model.Game;

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
	
	public Player getPlayerByUsername(String name) {
		Player ret = null;
		try {
			checkConnection();
			String selectSQL = "SELECT * FROM " +PLAYERS+" WHERE user_name = ? LIMIT 0,1";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, name);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				ret = new Player(rs.getString("user_name"), rs.getInt("id"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public Player getPlayerById(int id) {
		Player ret = null;
		try {
			checkConnection();
			String selectSQL = "SELECT * FROM " +PLAYERS+" WHERE id = ? LIMIT 0,1";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, id);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				ret = new Player(rs.getString("user_name"), rs.getInt("id"));
			}
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
						
			String selectSQL = "(SELECT player_id as 'id' FROM "+FRIENDS_RELATIONSHIP+" WHERE friend_id = ?) UNION ALL (SELECT friend_id as 'id' FROM "+FRIENDS_RELATIONSHIP+" WHERE player_id = ?) GROUP BY id";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, playerId);
			preparedStatement.setInt(2, playerId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				list.add(rs.getInt("id"));
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
	
	public int updateGame(Game game) {
		try {
			checkConnection();
			String selectSQL = "UPDATE "+GAMES+" SET type = ?, time_started = ?, map_name = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, game.getType());
			preparedStatement.setLong(2, game.getTimeStarted());
			preparedStatement.setString(2, game.getMapName());
			int ret = preparedStatement.executeUpdate();
			preparedStatement.close();
			return ret;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return 0;
	}

	public List<Player> getPlayersForGameId(int gameId) {
		ArrayList<Player> list = new ArrayList<Player>();
		try {
			checkConnection();
			String selectSQL = "SELECT p.id, p.username FROM "+PLAYERS+" p LEFT JOIN " +DD_GAME_RANKINGS+" d ON (p.id = d.player_id) LEFT JOIN " + RR_GAME_RANKINGS + " r ON (p.id = r.player_id) WHERE d.game_id = ? OR r.game_id = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, gameId);
			preparedStatement.setInt(2, gameId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				list.add(new Player(rs.getString("user_name"),rs.getInt("id")));
			}
			rs.close();
			preparedStatement.close();
			return list;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return list;
	}
	
	public List<Integer> getPlayerIdsForGameId(int gameId) {
		ArrayList<Integer> list = new ArrayList<Integer>();
		try {
			checkConnection();
			String selectSQL = "(SELECT player_id FROM " +DD_GAME_RANKINGS+" game_id = ?) UNION ALL (SELECT player_id FROM " + RR_GAME_RANKINGS + " WHERE game_id = ?) GROUP BY player_id";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, gameId);
			preparedStatement.setInt(2, gameId);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				list.add(rs.getInt("p.id"));
			}
			rs.close();
			preparedStatement.close();
			return list;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return list;
	}
	
	public Game getGameByName(String name) {
		Game ret = null;
		try {
			checkConnection();
			String selectSQL = "SELECT * FROM " +GAMES+" WHERE map_name = ? LIMIT 0,1";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setString(1, name);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				ret = new Game(rs.getInt("id"),rs.getInt("type"), rs.getLong("time_started"), rs.getString("map_name"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public Game getGameById(int id) {
		Game ret = null;
		try {
			checkConnection();
			String selectSQL = "SELECT * FROM " +GAMES+" WHERE id = ? LIMIT 0,1";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, id);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				ret = new Game(rs.getInt("id"),rs.getInt("type"), rs.getLong("time_started"), rs.getString("map_name"));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public int updatePlayerDRank(int ranking, int gameId, int playerId) {
		int ret = 0;
		try {
			checkConnection();
			String selectSQL = "UPDATE " +DD_GAME_RANKINGS+" SET ranking = ? WHERE player_id = ? AND game_id = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, ranking);
			preparedStatement.setInt(2, playerId);
			preparedStatement.setInt(3, gameId);
			ret = preparedStatement.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public int updatePlayerRRank(int ranking, int gameId, int playerId) {
		int ret = 0;
		try {
			checkConnection();
			String selectSQL = "UPDATE " +RR_GAME_RANKINGS+" SET ranking = ? WHERE player_id = ? AND game_id = ?";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(1, ranking);
			preparedStatement.setInt(2, playerId);
			preparedStatement.setInt(3, gameId);
			ret = preparedStatement.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public int addPlayerToDGame(int gameId, int playerId) {
		int ret = 0;
		try {
			checkConnection();
			String selectSQL = "INSERT INTO " +DD_GAME_RANKINGS+" (game_id,player_id) VALUES (?,?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(3, playerId);
			preparedStatement.setInt(2, gameId);
			ret = preparedStatement.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
	
	public int addPlayerToRGame(int gameId, int playerId) {
		int ret = 0;
		try {
			checkConnection();
			String selectSQL = "INSERT INTO " +RR_GAME_RANKINGS+" (game_id,player_id) VALUES (?,?)";
			PreparedStatement preparedStatement = conn.prepareStatement(selectSQL);
			preparedStatement.setInt(3, playerId);
			preparedStatement.setInt(2, gameId);
			ret = preparedStatement.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return ret;
	}
}
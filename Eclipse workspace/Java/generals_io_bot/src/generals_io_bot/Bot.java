

package generals_io_bot;


import java.io.UnsupportedEncodingException;
import java.net.URISyntaxException;
import java.net.URLEncoder;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import io.socket.client.IO;
import io.socket.client.Socket;


public class Bot {
	Socket socket;
	int playerIndex;
	JSONArray players;
	
	public Bot(String user_id, String username, String custom_game_id) throws URISyntaxException {
		this.socket = IO.socket("http://botws.generals.io");
		
		this.socket.on(Socket.EVENT_DISCONNECT, (Object... args) -> {
			System.err.println("Disconnected from server.");
			System.exit(1);
		});

		this.socket.on(Socket.EVENT_CONNECT, (Object... args) -> {
			System.out.println("Connected to server.");
			this.socket.emit("set_username", user_id, username);
			this.socket.emit("join_private", custom_game_id, user_id);
			this.socket.emit("set_force_start", custom_game_id, true);
			try {
				System.out.println("Joined custom game at http://bot.generals.io/games/" + URLEncoder.encode(custom_game_id, "UTF-8"));
			} catch(UnsupportedEncodingException exception) {
				exception.printStackTrace();
			}
		});
		
		this.socket.on("game_start", (Object... args) -> { //[{"teams":[1,2],"replay_id":"Hl2xzA7kb","usernames":["Solly","[Bot] Solly"],"game_type":"custom","playerIndex":1,"chat_room":"game_14935864204773DGH8lses6KKsVIdAAfK"}, null]
			try {
				this.playerIndex = (int) ((JSONObject) args[0]).get("playerIndex");
				this.players = (JSONArray) (((JSONObject) args[0]).get("usernames"));
				System.out.println("Game starting! The replay will be available after the game at http://bot.generals.io/replays/" + URLEncoder.encode((String) ((JSONObject) args[0]).get("replay_id"), "UTF-8"));
			} catch(JSONException | UnsupportedEncodingException exception) {
				exception.printStackTrace();
			}
		});
		
		this.socket.on("game_update", (Object... args) -> {
			//System.out.println(args[0]);
			// Patch the city and map diffs into our local variables.
			this.cities = patch(this.cities, data.cities_diff);
			this.map = patch(map, data.map_diff);
			this.generals = data.generals;

			// The first two terms in |map| are the dimensions.
			this.width = map[0];
			this.height = map[1];
			this.size = width * height;

			// The next |size| terms are army values.
			// armies[0] is the top-left corner of the map.
			this.armies = map.slice(2, size + 2);

			// The last |size| terms are terrain values.
			// terrain[0] is the top-left corner of the map.
			this.terrain = map.slice(size + 2, size + 2 + size);
		});
		
		this.socket.on("game_won", (Object... args) -> {
			System.out.println("Yay! Win!");
			this.socket.emit("leave_game");
		});
		
		this.socket.on("game_lost", (Object... args) -> {
			try {
				System.out.println("Defeated by " + this.players.getString((int) ((JSONObject) args[0]).get("killer")) + ".");
			} catch(JSONException exception) {
				exception.printStackTrace();
			}
			this.socket.emit("leave_game");
		});
		
		this.socket.connect();
	}
	
	public static void main(String[] args) throws URISyntaxException, InterruptedException {
		Bot bot = new Bot("solly_bot", "[Bot] Solly", "solly_bot_test");
		while(bot.socket.connected()){}
	}
	
	/* Returns a new array created by patching the diff into the old array.
	 * The diff formatted with alternating matching and mismatching segments:
	 * <Number of matching elements>
	 * <Number of mismatching elements>
	 * <The mismatching elements>
	 * ... repeated until the end of diff.
	 * Example 1: patching a diff of [1, 1, 3] onto [0, 0] yields [0, 3].
	 * Example 2: patching a diff of [0, 1, 2, 1] onto [0, 0] yields [2, 0].
	 */
	public static ArrayList<Integer> patch(ArrayList<Integer> old, ArrayList<Integer> diff) {
		ArrayList<Integer> out = new ArrayList<>();
		int i = 0;
		while (i < diff.size()) {
			if (diff.get(i) != 0) {  // matching
				out.addAll(old.subList(out.size(), out.size() + diff.get(i)));
			}
			i++;
			if (i < diff.size() && diff.get(i) != 0) {  // mismatching
				out.addAll(diff.subList(i + 1, i + 1 + diff.get(i)));
				i += diff.get(i);
			}
			i++;
		}
		return out;
	}
}

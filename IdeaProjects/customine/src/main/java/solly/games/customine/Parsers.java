package solly.games.customine;

import javax.media.j3d.SceneGraphObject;
import javax.sound.sampled.Line;
import java.io.BufferedReader;
import java.io.IOException;
import java.text.ParseException;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class Parsers {
	public static class LineByLineParser implements Iterator<String> {
		private BufferedReader reader;

		LineByLineParser(BufferedReader reader) {
			this.reader = reader;
		}

		@Override public boolean hasNext() {
			try {
				return this.reader.ready();
			} catch (IOException e) {
				return false;
			}
		}

		@Override public String next() {
			try {
				String line;

				if((line = this.reader.readLine()) == null) {
					throw new NoSuchElementException();
				} else {
					return this.reader.readLine();
				}
			} catch (IOException e) {
				throw new NoSuchElementException();
			}
		}
	}

	public static SceneGraphObject parseObjectFile(BufferedReader fileReader) throws IOException, ParseException {
		LineByLineParser lineByLineParser = new LineByLineParser(fileReader);

		try {
			
		}
	}
}

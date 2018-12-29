package io.github.sollyucko.utilities;

import java.util.Iterator;
import java.util.Spliterators;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

public class Utilities {
	public static Stream<Character> readableToCharacterStream(Readable readable) {
		return null;
	}
	
	public static <T> Stream<T> iteratorStream(Iterator<T> iterator) {
		return StreamSupport.stream(Spliterators.spliteratorUnknownSize(iterator, 1024), false);
	}
}

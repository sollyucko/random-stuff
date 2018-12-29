package io.github.sollyucko.programming_languages.functional;

import io.github.sollyucko.programming_languages.InterpretPipeline;

import java.io.FileReader;
import java.io.IOException;
import java.util.*;

import static io.github.sollyucko.utilities.Utilities.readableToCharacterStream;

public class Main {
	public static void main(String[] args) throws IOException {
		List<String> argList = new ArrayList<>();
		Collections.addAll(argList, Arrays.copyOfRange(args, 1, args.length - 1));
		
		try (FileReader fileReader = new FileReader(args[0])) {
			new InterpretPipeline<>(new FunctionalLexer(),
			                        new FunctionalParser(),
			                        new FunctionalInterpreter(argList)).apply(readableToCharacterStream(fileReader));
		}
	}
}

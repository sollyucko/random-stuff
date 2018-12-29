package io.github.sollyucko.programming_languages;

import java.util.function.Function;
import java.util.stream.Stream;

public class InterpretPipeline<T extends Token, N extends Node, L extends Lexer<T>, P extends Parser<T, N>, I extends Interpreter<N>> implements Function<Stream<Character>, Integer> {
	private final I interpreter;
	private final L lexer;
	private final P parser;

	public InterpretPipeline(L lexer, P parser, I interpreter) {
		this.lexer = lexer;
		this.parser = parser;
		this.interpreter = interpreter;
	}

	public Integer apply(Stream<Character> characterStream) {
		return interpreter.apply(parser.apply(lexer.apply(characterStream)));
	}
}

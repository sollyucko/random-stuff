package io.github.sollyucko.programming_languages;

import java.util.function.Function;
import java.util.stream.Stream;

public interface Lexer<T extends Token> extends Function<Stream<Character>, Stream<T>> {

}

package io.github.sollyucko.programming_languages;

import java.util.function.Function;
import java.util.stream.Stream;

public interface Parser<T extends Token, N extends Node> extends Function<Stream<T>, N> {}

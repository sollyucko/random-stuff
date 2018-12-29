package io.github.sollyucko.programming_languages;

import java.util.function.Function;

public interface Interpreter<N extends Node> extends Function<N, Integer> {}

package io.github.sollyucko.programming_languages;

public interface TokenType<T extends Token> {
	default boolean canMatch(String source) {
		return false;
	}
	
	default boolean canStartWith(String start) {
		return start.length() == 0;
	}
	
	T getInstance(String source);
}

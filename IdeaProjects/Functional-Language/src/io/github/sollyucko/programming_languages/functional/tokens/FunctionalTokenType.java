package io.github.sollyucko.programming_languages.functional.tokens;

import io.github.sollyucko.programming_languages.TokenType;

public abstract class FunctionalTokenType<T extends FunctionalToken> implements TokenType<T> {
	public abstract T getInstance(String source);
}

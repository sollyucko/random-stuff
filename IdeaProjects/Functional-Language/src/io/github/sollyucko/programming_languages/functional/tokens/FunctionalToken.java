package io.github.sollyucko.programming_languages.functional.tokens;

import io.github.sollyucko.programming_languages.Token;

public class FunctionalToken implements Token {
	private final String source;
	
	public FunctionalToken(String source) {
		this.source = source;
	}
	
	@Override
	public String getSource() {
		return this.source;
	}
}

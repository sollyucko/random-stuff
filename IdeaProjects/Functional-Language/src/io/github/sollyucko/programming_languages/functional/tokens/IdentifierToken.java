package io.github.sollyucko.programming_languages.functional.tokens;

public class IdentifierToken extends FunctionalToken {
	private final String value;
	
	public IdentifierToken(String source) {
		super(source);
		this.value = source;
	}
	
	
	public String getValue() {
		return this.value;
	}
}

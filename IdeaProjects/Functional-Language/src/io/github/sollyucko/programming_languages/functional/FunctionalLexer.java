package io.github.sollyucko.programming_languages.functional;

import io.github.sollyucko.programming_languages.Lexer;
import io.github.sollyucko.programming_languages.functional.tokens.FunctionalToken;
import io.github.sollyucko.programming_languages.functional.tokens.FunctionalTokenType;
import io.github.sollyucko.utilities.Generator;

import java.util.*;
import java.util.stream.Stream;

import static io.github.sollyucko.utilities.Utilities.iteratorStream;

public class FunctionalLexer implements Lexer<FunctionalToken> {
	private Set<FunctionalTokenType> tokenRegistry;
	
	@Override
	public Stream<FunctionalToken> apply(Stream<Character> input) {
		return iteratorStream(new Generator<FunctionalToken>() {
			@Override
			public void generate() {
				Set<FunctionalTokenType> availableTokenTypes = new HashSet<>(FunctionalLexer.this.tokenRegistry);
				Set<FunctionalTokenType> matchableTokenTypes = new HashSet<>();
				String currentToken = "";
				
				for (Iterator<Character> it = input.iterator(); it.hasNext(); ) {
					Character character = it.next();
					String newToken = currentToken + character;
					
					for (FunctionalTokenType tokenType : availableTokenTypes) {
						if(tokenType.canMatch(currentToken)) {
							matchableTokenTypes.add(tokenType);
						}
						
						if (!tokenType.canStartWith(newToken)) {
							availableTokenTypes.remove(tokenType);
						}
					}
					
					if(availableTokenTypes.size() == 0) {
						this.yield(matchableTokenTypes.iterator().next().getInstance(currentToken));
						
						currentToken = "";
					} else {
						currentToken = newToken;
					}
				}
			}
		});
	}
}

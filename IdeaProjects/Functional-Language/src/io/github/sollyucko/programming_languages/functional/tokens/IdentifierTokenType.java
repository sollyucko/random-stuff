package io.github.sollyucko.programming_languages.functional.tokens;

public class IdentifierTokenType extends FunctionalTokenType<IdentifierToken> {
	@Override
	public IdentifierToken getInstance(String source) {
		return new IdentifierToken(source);
	}
	
	@Override
	public boolean canStartWith(String start) {
		if(super.canStartWith(start)) {
			return true;
		}
		
		return this.canMatch(start);
	}
	
	@Override
	public boolean canMatch(String source) {
		if(super.canMatch(source)) {
			return true;
		}
		
		if(source.length() == 0) {
			return false;
		}
		
		if(!Character.isLetter(source.charAt(0))) {
			return false;
		}
		
		for(Character character : source.toCharArray()) {
			if(!Character.isLetterOrDigit(character)) {
				return false;
			}
		}
		
		return true;
	}
}

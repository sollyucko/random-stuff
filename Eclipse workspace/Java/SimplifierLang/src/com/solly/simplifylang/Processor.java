

package com.solly.simplifylang;


import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;


public abstract class Processor {
	
	public static List<Token> tokenize(String code) {
		List<Token> tokens = new ArrayList<>();
		int pos = 0;
		String tmpString = "";
		
		while(pos <= code.length()) {
			pos++;
			
			Token token = getToken(tmpString);
			
			if(token != null) {
				if(getToken(tmpString + code.charAt(pos)) != null || pos == code.length()) {
					tokens.add(token);
					tmpString = String.valueOf(code.charAt(pos));
				}
			}
		}
		
		return tokens;
	}
	
	public static Token getToken(String text) {
		if(text.matches("^\\w+$")) {
			return new TokenIdentifier(text);
		} else if(text.matches("[+-]?(\\d\\.)?\\d+")) {
			return new TokenNumber(new BigDecimal(text));
		} else {
			for(TokenSymbol tokenOperator : TokenSymbol.defaultTokenOperators) {
				if(tokenOperator.text == text) {
					return tokenOperator;
				}
			}
			
			return null;
		}
	}
	
	public static Simplifiable parse(List<Token> tokens) {
		return null;
	}
}

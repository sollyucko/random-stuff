

package com.solly.simplifylang;


public class TokenSymbol implements Token {
	public String text;
	
	public TokenSymbol(String text) {
		this.text = text;
	}
	
	public String toString() {
		return this.text;
	}
	
	public static TokenSymbol[] defaultTokenOperators = new TokenSymbol[] {new TokenSymbol("+"), new TokenSymbol("-"), new TokenSymbol("*"), new TokenSymbol("/"), new TokenSymbol("("), new TokenSymbol(")")};
	// +, -, *, /, (, )
}

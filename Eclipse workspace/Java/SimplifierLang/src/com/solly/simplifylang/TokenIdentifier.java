package com.solly.simplifylang;

public class TokenIdentifier implements Token {
	
	public String text;

	public TokenIdentifier(String text) {
		this.text = text;
	}
	
	public String toString() {
		return this.text;
	}
	
}

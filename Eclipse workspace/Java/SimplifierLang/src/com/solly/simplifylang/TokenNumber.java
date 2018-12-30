

package com.solly.simplifylang;


public class TokenNumber implements Token {
	
	public Number value;

	public TokenNumber(Number value) {
		this.value = value;
	}
	
	public String toString() {
		return this.value.toString();
	}
	
}

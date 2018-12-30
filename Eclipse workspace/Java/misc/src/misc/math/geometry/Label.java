package misc.math.geometry;

import misc.math.numbers.*;

public	class	Label {
	char				name;
	@Positive int		primes;
	
	public Label(char name) {
		this.name = name;
		this.primes = 0;
	}
	public Label(char name, int primes) {
		this.name = name;
		this.primes = primes;
	}
}

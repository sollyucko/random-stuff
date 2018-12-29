package io.github.sollyucko.symj;

import lombok.Data;
import org.jetbrains.annotations.NotNull;

import java.math.BigInteger;

@Data
public class Rational {
	@NotNull private final BigInteger denominator;
	@NotNull private final BigInteger numerator;
	
	public Rational(@NotNull BigInteger integer) {
		this(integer, BigInteger.ONE);
	}
	
	public Rational(@NotNull BigInteger numerator, @NotNull BigInteger denominator) {
		BigInteger gcd = numerator.gcd(denominator);
		
		this.numerator = numerator.divide(gcd);
		this.denominator = denominator.divide(gcd);
	}
	
	public Rational negate() {
		return new Rational(this.getNumerator().negate(), this.getDenominator());
	}
	
	public @NotNull Rational add(@NotNull Rational other) {
		return new Rational(this.getNumerator()
		                        .multiply(other.getDenominator())
		                        .add(other.getNumerator().multiply(this.getDenominator())),
		                    this.getDenominator().multiply(other.getDenominator()));
	}
	
	public @NotNull Rational subtract(@NotNull Rational other) {
		return new Rational(this.getNumerator()
		                        .multiply(other.getDenominator())
		                        .subtract(other.getNumerator().multiply(this.getDenominator())),
		                    this.getDenominator().multiply(other.getDenominator()));
	}
	
	public @NotNull Rational multiply(@NotNull Rational other) {
		return new Rational(this.getNumerator().multiply(other.getNumerator()),
		                    this.getDenominator().multiply(other.getDenominator()));
	}
	
	public @NotNull Rational divide(@NotNull Rational other) {
		return new Rational(this.getNumerator().multiply(other.getDenominator()),
		                    this.getDenominator().multiply(other.getNumerator()));
	}
}

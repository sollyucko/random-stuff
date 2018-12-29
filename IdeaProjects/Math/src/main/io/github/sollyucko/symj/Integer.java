package io.github.sollyucko.symj;

import lombok.*;
import org.jetbrains.annotations.NotNull;

import java.math.BigInteger;

@Data
@EqualsAndHashCode(callSuper=true)
public class Integer extends Rational {
	@NotNull private final BigInteger value;
	
	public Integer() {
		this(BigInteger.ZERO);
	}
	
	public Integer(@NotNull BigInteger value) {
		super(value);
		this.value = value;
	}
	
	public Integer negate() {
		return new Integer(this.getValue().negate());
	}
	
	public Integer add(Integer other) {
		return new Integer(this.getValue().add(other.getValue()));
	}
	
	public Integer subtract(Integer other) {
		return new Integer(this.getValue().subtract(other.getValue()));
	}
	
	public Integer multiply(Integer other) {
		return new Integer(this.getValue().multiply(other.getValue()));
	}
	
	public Rational divide(Integer other) {
		return new Rational(this.getValue(), other.getValue());
	}
}

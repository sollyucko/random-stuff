package io.github.sollyucko.symj;

import org.jetbrains.annotations.NotNull;

import java.math.BigInteger;

public class NonNegativeInteger extends Integer {
	public NonNegativeInteger() {
		this(BigInteger.ZERO);
	}
	
	public NonNegativeInteger(@NotNull BigInteger value) {
		super(value);
		assert value.compareTo(BigInteger.ZERO) >= 0;
	}
	
	@NotNull
	public NonNegativeInteger add(@NotNull NonNegativeInteger value) {
		return new NonNegativeInteger(this.getValue().add(value.getValue()));
	}
	
	@NotNull
	public NonNegativeInteger multiply(@NotNull NonNegativeInteger value) {
		return new NonNegativeInteger(this.getValue().multiply(value.getValue()));
	}
	
	@NotNull
	public NonNegativeInteger mod(@NotNull NonNegativeInteger other) {
		return new NonNegativeInteger(this.getValue().mod(other.getValue()));
	}
	
	@NotNull
	public NonNegativeInteger pow(@NotNull NonNegativeInteger other) {
		return new NonNegativeInteger(this.getValue().pow())
	}
}

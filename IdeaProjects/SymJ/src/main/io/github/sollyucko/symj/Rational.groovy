package io.github.sollyucko.symj

import org.jetbrains.annotations.NotNull

class Rational {
    @NotNull final BigInteger numerator
    @NotNull final BigInteger denominator

    Rational() {
        this.numerator = 1
        this.denominator = 1
    }

    Rational(@NotNull BigInteger value) {
        this.numerator = value
        this.denominator = 1
    }

    Rational(@NotNull BigInteger numerator, @NotNull BigInteger denominator) {
        def gcd = numerator.gcd(denominator)

        this.numerator = numerator / gcd as BigInteger
        this.denominator = denominator / gcd as BigInteger
    }

    @NotNull Rational negate() {
        return new Rational(-this.numerator, this.denominator)
    }

    @NotNull Rational add(@NotNull Rational other) {
        return new Rational(this.numerator * other.denominator + other.numerator * this.denominator, this.denominator * other.denominator)
    }

    @NotNull Rational subtract(@NotNull Rational other) {
        return this + -other
    }

    @NotNull Rational multiply(@NotNull Rational other) {
        return new Rational(this.numerator * other.numerator, this.denominator * other.denominator)
    }

    @NotNull Rational pow(@NotNull Integer other) {
        if(other == 0) {
            return new Rational()
        } else if(other > 0) {
            return new Rational(this.numerator ** other, this.denominator ** other)
        }
    }
}
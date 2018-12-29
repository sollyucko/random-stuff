package io.github.sollyucko.collections.test.instruction;

import io.github.sollyucko.collections.Deque;
import org.junit.jupiter.api.Assertions;

public class PopLeft extends Instruction {
	public PopLeft(Deque<Integer> deque, Integer value) {
		super(deque, value);
	}
	
	@Override
	public void execute() {
		Assertions.assertEquals(this.value, this.deque.popLeft());
	}
}

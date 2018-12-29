package io.github.sollyucko.collections.test.instruction;

import io.github.sollyucko.collections.Deque;

public class PushRight extends Instruction {
	public PushRight(Deque<Integer> deque, Integer value) {
		super(deque, value);
	}
	
	@Override
	public void execute() {
		this.deque.pushRight(this.value);
	}
}

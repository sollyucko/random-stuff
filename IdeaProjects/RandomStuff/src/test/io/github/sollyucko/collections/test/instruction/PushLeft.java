package io.github.sollyucko.collections.test.instruction;

import io.github.sollyucko.collections.Deque;

public class PushLeft extends Instruction {
	public PushLeft(Deque<Integer> deque, Integer value) {
		super(deque, value);
	}
	
	@Override
	public void execute() {
		this.deque.pushLeft(this.value);
	}
}

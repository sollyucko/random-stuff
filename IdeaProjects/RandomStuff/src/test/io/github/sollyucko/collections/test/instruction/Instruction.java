package io.github.sollyucko.collections.test.instruction;

import io.github.sollyucko.collections.Deque;

@SuppressWarnings("unused")
public abstract class Instruction {
	public final Deque<Integer> deque;
	public final Integer value;
	
	public Instruction(Deque<Integer> deque, Integer value) {
		this.deque = deque;
		this.value = value;
	}
	
	public abstract void execute();
	
}

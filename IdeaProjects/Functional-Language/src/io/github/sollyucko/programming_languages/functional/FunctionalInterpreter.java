package io.github.sollyucko.programming_languages.functional;

import io.github.sollyucko.programming_languages.Interpreter;

import java.util.List;

public class FunctionalInterpreter implements Interpreter<FunctionalNode> {
	private final List<String> args;

	public FunctionalInterpreter(List<String> args) {
		this.args = args;
	}

	@Override
	public Integer apply(FunctionalNode functionalNode) {
		return null;
	}
}

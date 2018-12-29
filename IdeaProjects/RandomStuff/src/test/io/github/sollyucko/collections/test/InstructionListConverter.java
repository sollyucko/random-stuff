package io.github.sollyucko.collections.test;

import io.github.sollyucko.collections.Deque;
import io.github.sollyucko.collections.test.instruction.*;
import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.NotNull;
import org.junit.jupiter.api.extension.ParameterContext;
import org.junit.jupiter.params.converter.ArgumentConversionException;
import org.junit.jupiter.params.converter.ArgumentConverter;

import java.lang.reflect.InvocationTargetException;
import java.util.*;

import static java.text.MessageFormat.format;

public class InstructionListConverter implements ArgumentConverter {
	static Map<String, Class<? extends Instruction>> instructionClasses = new HashMap<>();
	
	static {
		instructionClasses.put("AS", AssertSize.class);
		instructionClasses.put("oL", PopLeft.class);
		instructionClasses.put("oR", PopRight.class);
		instructionClasses.put("uL", PushLeft.class);
		instructionClasses.put("uR", PushRight.class);
	}
	
	private Deque<Integer> deque;
	
	public InstructionListConverter() {}
	
	@Override
	@Contract(pure = true)
	public Object convert(Object source, ParameterContext context) throws ArgumentConversionException {
		if (!Instruction[].class.isAssignableFrom(context.getParameter().getType())) {
			throw this.throwException(source, context);
		}
		
		if (source instanceof Instruction[]) {
			return source;
		} else if (source instanceof String) {
			if (source.equals("")) {
				return new Instruction[0];
			}
			
			String[] parts = ((String) source).split(",");
			this.deque = this.getDeque(context);
			return Arrays.stream(parts).map(this::parseInstruction).toArray(Instruction[]::new);
		} else {
			throw this.throwException(source, context);
		}
	}
	
	private Deque<Integer> getDeque(@NotNull ParameterContext context) {
		return ((DequeTest) context.getTarget().orElseThrow(RuntimeException::new)).deque;
	}
	
	@SuppressWarnings("unchecked")
	private Class<? extends Instruction> getInstructionClass(String instructionType) {
		return instructionClasses.get(instructionType);
	}
	
	@NotNull
	@Contract(pure = true)
	private Instruction parseInstruction(@NotNull String stringInstruction) {
		String instructionType = stringInstruction.substring(0, 2);
		Integer value = Integer.valueOf(stringInstruction.substring(2));
		
		try {
			return this.getInstructionClass(instructionType).getDeclaredConstructor(Deque.class, Integer.class).newInstance(this.deque, value);
		} catch (InstantiationException | IllegalAccessException | NoSuchMethodException | InvocationTargetException e) {
			throw new RuntimeException(e);
		}
	}
	
	@NotNull
	@Contract(pure = true)
	private ArgumentConversionException throwException(@NotNull Object source, @NotNull ParameterContext context) throws ArgumentConversionException {
		return new ArgumentConversionException(format("Cannot convert {0} to {1}", source.getClass().getCanonicalName(), context.getParameter().getType().getCanonicalName()));
	}
}

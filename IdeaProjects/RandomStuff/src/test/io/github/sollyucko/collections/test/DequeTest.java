package io.github.sollyucko.collections.test;

import io.github.sollyucko.collections.Deque;
import io.github.sollyucko.collections.test.instruction.Instruction;
import org.jetbrains.annotations.NotNull;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.converter.ConvertWith;
import org.junit.jupiter.params.provider.CsvFileSource;

import java.time.Duration;
import java.util.Iterator;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

public class DequeTest {
	Deque<Integer> deque;
	
	@Test
	void testDefaultSizeHintDoesNothing() {
		final Deque<Integer> deque2 = new Deque<Integer>() {
			@Override
			public boolean isEmpty() {
				throw new RuntimeException();
			}
			
			@NotNull
			@Override
			public Iterator<Integer> iterator() {
				throw new RuntimeException();
			}
			
			@Override
			public Integer popLeft() {
				throw new RuntimeException();
			}
			
			@Override
			public Integer popRight() {
				throw new RuntimeException();
			}
			
			@Override
			public void pushLeft(Integer item) {
				throw new RuntimeException();
			}
			
			@Override
			public void pushRight(Integer item) {
				throw new RuntimeException();
			}
			
			@Override
			public int size() {
				throw new RuntimeException();
			}
		};
		
		assertTimeout(Duration.ZERO, () -> deque2.sizeHint(0));
	}
	
	@Test
	void testIterator() {
		final Iterator<Integer> iterator = this.deque.iterator();
		assertFalse(iterator.hasNext());
		assertThrows(NoSuchElementException.class, iterator::next);
	}
	
	@Test
	void testIterator2() {
		this.deque.pushLeft(1);
		final Iterator<Integer> iterator = this.deque.iterator();
		assertTrue(iterator.hasNext());
		assertEquals(1, (int) iterator.next());
		assertFalse(iterator.hasNext());
		assertThrows(NoSuchElementException.class, iterator::next);
	}
	
	@Test
	void testIterator3() {
		final Iterator<Integer> iterator = this.deque.iterator();
		assertThrows(UnsupportedOperationException.class, iterator::remove);
	}
	
	@Test
	void testPopLeftEmptyThrows() {
		assertThrows(NoSuchElementException.class, () -> this.deque.popLeft());
	}
	
	@Test
	void testPopRightEmptyThrows() {
		assertThrows(NoSuchElementException.class, () -> this.deque.popRight());
	}
	
	@Test
	void testPushLeftIsNotEmpty() {
		this.deque.pushLeft(1);
		assertFalse(this.deque.isEmpty());
	}
	
	@Test
	void testPushLeftNullThrows() {
		assertThrows(RuntimeException.class, () -> this.deque.pushLeft(null));
	}
	
	@ParameterizedTest
	@CsvFileSource(resources = "/push_pop_test.csv")
	void testPushPop(@ConvertWith(InstructionListConverter.class) Instruction[] instructions) {
		for (Instruction instruction : instructions) {
			instruction.execute();
		}
	}
	
	@Test
	void testPushRightIsNotEmpty() {
		this.deque.pushRight(1);
		assertFalse(this.deque.isEmpty());
	}
	
	@Test
	void testPushRightNullThrows() {
		assertThrows(RuntimeException.class, () -> this.deque.pushRight(null));
	}
	
	@Test
	void testStartIsEmpty() {
		assertTrue(this.deque.isEmpty());
	}
	
	@Test
	void testStartSizeZero() {
		assertEquals(this.deque.size(), 0);
	}
}

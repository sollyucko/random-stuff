package io.github.sollyucko.collections;

import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.NotNull;

import java.util.*;

import static java.lang.Math.floorDiv;
import static java.lang.Math.max;
import static java.text.MessageFormat.format;

public class ArrayDeque<T> implements Deque<T> {
	private int head;
	private int itemCount;
	private Object[] items;
	private int tail;
	
	public ArrayDeque() {
		this.items = new Object[0];
		this.itemCount = 0;
		this.head = 0;
		this.tail = 0;
	}
	
	@Contract(pure = true)
	@SuppressWarnings("unchecked")
	private T getItem(int index) {
		return (T) this.items[index];
	}
	
	@Contract(pure = true)
	@Override
	public boolean isEmpty() {
		return this.itemCount == 0;
	}
	
	@Contract(pure = true)
	@Override
	@NotNull
	public Iterator<T> iterator() {
		return new DequeIterator();
	}
	
	@Override
	@NotNull
	public T popLeft() {
		if (this.isEmpty()) {
			throw new NoSuchElementException("Deque is empty");
		}
		
		T item = this.getItem(this.head);
		this.items[this.head] = null;
		this.head++;
		this.itemCount--;
		return item;
	}
	
	@Override
	@NotNull
	public T popRight() {
		if (this.isEmpty()) {
			throw new NoSuchElementException("Deque is empty");
		}
		
		final T item = this.getItem(this.tail);
		this.items[this.tail] = null;
		this.tail--;
		this.itemCount--;
		return item;
	}
	
//	private void printDebugInfo() {
//		System.out.println(format("Items: {0}\nHead: {1}\nTail: {2}\nItem count: {3}", Arrays.toString(this.items), this.head, this.tail, this.itemCount));
//	}
	
	@Override
	public void pushLeft(@NotNull T item) {
		if (this.head <= 0) {
			this.sizeHint(this.items.length + 1);
		}
		
		this.head--;
		this.items[this.head] = item;
		this.itemCount++;
	}
	
	@Override
	public void pushRight(@NotNull T item) {
		if (this.tail >= (this.items.length - 1)) {
			this.sizeHint(this.items.length + 1);
		}
		
		this.tail++;
		this.items[this.tail] = item;
		this.itemCount++;
	}
	
	@Contract(pure = true)
	@Override
	public int size() {
		return this.itemCount;
	}
	
	public void sizeHint(int size) {
		final int realSize = (max(size, this.size()) + 1) * 2;
		final Object[] newArray = new Object[realSize];
		final int newHead = floorDiv(realSize - this.size(), 2);
		
		System.arraycopy(this.items, this.head, newArray, newHead, this.itemCount);
		
		this.head = newHead;
		this.tail = this.head + this.itemCount - 1;
		this.items = newArray;
	}
	
	private class DequeIterator implements Iterator<T> {
		private int size;
		private int startpos;
		
		DequeIterator() {
			this.startpos = ArrayDeque.this.head;
			this.size = ArrayDeque.this.itemCount;
		}
		
		@Contract(pure = true)
		@Override
		public boolean hasNext() {
			return this.size != 0;
		}
		
		@Override
		public T next() {
			if (this.hasNext()) {
				this.size--;
				return ArrayDeque.this.getItem(this.startpos++);
			} else {
				throw new NoSuchElementException();
			}
		}
		
		@Override
		public void remove() {
			throw new UnsupportedOperationException();
		}
	}
}
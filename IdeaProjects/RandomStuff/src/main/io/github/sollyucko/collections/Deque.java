package io.github.sollyucko.collections;

public interface Deque<T> extends Iterable<T> {
	boolean isEmpty();
	T popLeft();
	T popRight();
	void pushLeft(T item);
	void pushRight(T item);
	int size();
	default void sizeHint(int size) {}
}

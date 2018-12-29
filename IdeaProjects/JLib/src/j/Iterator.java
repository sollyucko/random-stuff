package j;

public interface Iterator<T> {
	T next() throws IteratorExhaustedError;
}

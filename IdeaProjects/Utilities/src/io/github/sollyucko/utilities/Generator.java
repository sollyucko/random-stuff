package io.github.sollyucko.utilities;

import java.util.Iterator;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public abstract class Generator<T> implements Iterator<T> {
	private final BlockingQueue<T> queue = new LinkedBlockingQueue<>();
	private Thread thread;
	
	public Generator() {
		this.thread = new Thread(this::generate);
		this.thread.run();
	}
	
	public void yield(T object) {
		this.queue.add(object);
	}
	
	public abstract void generate();
	
	@Override
	public boolean hasNext() {
		while(true) {
			if (!this.thread.isAlive()) {
				return !this.queue.isEmpty();
			}
			
			if(!this.queue.isEmpty()) {
				return true;
			}
		}
	}
	
	@Override
	public T next() {
		try {
			return this.queue.take();
		} catch (InterruptedException e) {
			throw new RuntimeException(e);
		}
	}
}

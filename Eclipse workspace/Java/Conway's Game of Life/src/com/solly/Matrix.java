package com.solly;

import java.util.Collection;

public interface Matrix<T> {
	T getItem(int row, int column);
	int getHeight();
	int getWidth();
	Collection<T> getRow(int index);
	Collection<? extends Collection<T>> getRows();
	Collection<? extends Collection<T>> getRows(int start, int end);
	Collection<T> getColumn(int index);
	Collection<? extends Collection<T>> getColumns();
}

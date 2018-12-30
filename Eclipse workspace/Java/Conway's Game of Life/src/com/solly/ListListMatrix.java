

package com.solly;


import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.function.Consumer;


public class ListListMatrix<T> implements Cloneable, Iterable<T>/*, Matrix<T>*/ {
	public boolean equals(Object object) {
		if(object instanceof ListListMatrix) {
			return this.rows.equals(((ListListMatrix<?>) object).rows);
		}
		return false;
	}
	
	public class ListListMatrixIterator<U> implements Iterator<U> {
		private ListListMatrix<U> matrix;
		private int x = -1;
		private int y = 0;
		
		public ListListMatrixIterator(ListListMatrix<U> matrix) {
			this.matrix = matrix;
		}
		
		public boolean hasNext() {
			return this.x + 1 < this.matrix.getWidth() || this.y + 1 < this.matrix.getHeight();
		}
		
		public U next() {
			if(this.x + 1 == this.matrix.getWidth()) {
				this.x = 0;
				this.y++;
			} else {
				this.x++;
			}
			return this.matrix.getItem(this.y, this.x);
		}
	}
	
	private List<List<T>> rows;
	
	public ListListMatrix() {
		this.rows = new ArrayList<>();
	}
	
	public void addColumn() {
		for(List<T> row : this.rows) {
			row.add(null);
		}
	}
	
	public void addColumn(int index) {
		for(List<T> row : this.rows) {
			row.add(index, null);
		}
	}
	
	public void addColumn(int index, List<T> column) {
		for(int i = 0; i < this.getWidth(); i++) {
			if(i < column.size()) {
				this.rows.get(i).add(index, column.get(i));
			} else {
				this.rows.get(i).add(index, null);
			}
		}
	}
	
	public void addColumn(List<T> column) {
		for(int i = 0; i < this.getWidth(); i++) {
			if(i < column.size()) {
				this.rows.get(i).add(column.get(i));
			} else {
				this.rows.get(i).add(null);
			}
		}
	}
	
	public void addColumns(int index, List<List<T>> columns) {
		for(int i = 0; i < columns.size(); i++) {
			this.addColumn(index + i, columns.get(i));
		}
	}
	
	public void addColumns(List<List<T>> columns) {
		for(List<T> column : columns) {
			this.addColumn(column);
		}
	}
	
	public void addRow() {
		this.rows.add(new ArrayList<>(Collections.nCopies(this.getWidth(), null)));
	}
	
	public void addRow(int index) {
		this.rows.add(index, new ArrayList<>(Collections.nCopies(this.getWidth(), null)));
	}
	
	public void addRow(int index, List<T> row) {
		if(row.size() < this.getWidth()) {
			row.addAll(Collections.nCopies(this.getWidth() - row.size(), null));
		} else if(row.size() > this.getWidth()) {
			for(List<T> oldRow : this.rows) {
				oldRow.addAll(Collections.nCopies(row.size() - this.getWidth(), null));
			}
		}
		this.rows.add(index, row);
	}
	
	public void addRow(List<T> row) {
		if(row.size() < this.getWidth()) {
			row.addAll(Collections.nCopies(this.getWidth() - row.size(), null));
		} else if(row.size() > this.getWidth()) {
			for(List<T> oldRow : this.rows) {
				oldRow.addAll(Collections.nCopies(row.size() - this.getWidth(), null));
			}
		}
		this.rows.add(row);
	}
	
	public void addRows(int index, List<List<T>> rows) {
		for(int i = 0; i < rows.size(); i++) {
			this.addRow(i + index, rows.get(i));
		}
	}
	
	public void addRows(List<List<T>> rows) {
		for(List<T> row : rows) {
			this.addRow(row);
		}
	}
	
	@SuppressWarnings("unchecked") public ListListMatrix<T> clone() {
		try {
			ListListMatrix<T> cloned = (ListListMatrix<T>) super.clone();
			cloned.rows = new ArrayList<>(cloned.rows);
			for(int i = 0; i < cloned.rows.size(); i++) {
				cloned.rows.set(i, new ArrayList<>(cloned.rows.get(i)));
			}
			return cloned;
		} catch(CloneNotSupportedException exception) {
			throw new RuntimeException(exception);
		}
	}
	
	public void forEach(Consumer<? super T> action) {
		for(List<T> row : this.rows) {
			for(T item : row) {
				action.accept(item);
			}
		}
	}
	
	public List<T> getColumn(int index) {
		List<T> values = new ArrayList<>();
		for(List<T> row : this.rows) {
			values.add(row.get(index));
		}
		return values;
	}
	
	public List<List<T>> getColumns() {
		return this.getColumns(0, this.rows.get(0).size() - 1);
	}
	
	public List<List<T>> getColumns(int start, int end) {
		List<List<T>> columns = new ArrayList<>();
		for(int index = start; index <= end; index++) {
			columns.add(this.getColumn(index));
		}
		return columns;
	}
	
	public int getHeight() {
		return this.rows.size();
	}
	
	public T getItem(int row, int column) {
		return this.rows.get(row).get(column);
	}
	
	public List<T> getRow(int index) {
		return this.rows.get(index);
	}
	
	public List<List<T>> getRows() {
		return this.rows;
	}
	
	public List<List<T>> getRows(int start, int end) {
		return this.rows.subList(start, end);
	}
	
	public int getWidth() {
		if(this.rows.size() > 0) {
			return this.rows.get(0).size();
		}
		return 0;
	}
	
	public ListListMatrixIterator<T> iterator() {
		return new ListListMatrixIterator<>(this);
	}
	
	public void removeColumn(int index) {
		for(List<T> row : this.rows) {
			row.remove(index);
		}
	}
	
	public void removeColumns(int start, int end) {
		for(int i = start; i <= end; i++) {
			this.removeColumn(i);
		}
	}
	
	public void removeRow(int index) {
		this.rows.remove(index);
	}
	
	public void removeRows(int start, int end) {
		for(int i = start; i <= end; i++) {
			this.removeRow(i);
		}
	}
	
	public void setColumn(int index, List<T> column) {
		for(int i = 0; i < column.size(); i++) {
			this.rows.get(i).set(index, column.get(i));
		}
	}
	
	public void setHeight(int height) {
		if(this.getHeight() < height) {
			for(int i = this.getHeight(); i < height; i++) {
				this.addRow();
			}
		} else if(this.getHeight() > height) {
			for(int i = this.getHeight(); i < height; i++) {
				this.removeRow(this.getHeight());
			}
		}
	}
	
	public void setItem(int row, int column, T item) {
		this.rows.get(row).set(column, item);
	}
	
	public void setRow(int index, List<T> row) {
		this.rows.set(index, row);
	}
	
	public void setWidth(int width) {
		if(this.getWidth() < width) {
			for(int i = this.getWidth(); i < width; i++) {
				this.addColumn();
			}
		} else if(this.getWidth() > width) {
			for(int i = this.getWidth(); i < width; i++) {
				this.removeColumn(this.getWidth() - 1);
			}
		}
	}
	
	public String toString() {
		return this.rows.toString();
	}
	
	public int hashCode() {
		return this.rows.hashCode();
	}
}

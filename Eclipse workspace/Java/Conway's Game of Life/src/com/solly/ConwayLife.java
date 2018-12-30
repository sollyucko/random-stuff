

package com.solly;


import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;


public class ConwayLife {
	public static class PeriodIterationsAndGrid {
		public int period;
		public int iterations;
		public ListListMatrix<Boolean> grid;

		PeriodIterationsAndGrid(int period, int iterations, ListListMatrix<Boolean> grid) {
			this.period = period;
			this.iterations = iterations;
			this.grid = grid;
		}
	}
	
	public static PeriodIterationsAndGrid getPeriod(ListListMatrix<Boolean> grid) {
		List<ListListMatrix<Boolean>> grids = new ArrayList<>();
		int iterations = 0;
		while(!grids.contains(grid)) {
			if(!grids.contains(grid)) {
				grids.add(grid);
				grid = process(grid);
			}
			iterations++;
		}
		return new PeriodIterationsAndGrid(iterations - grids.indexOf(grid), grids.indexOf(grid) + 1, grid);
	}
	
	public static <T> boolean contains(T[] array, T value) { // contains(array, value)
		for(T item : array) { // for each item in the array
			if(item.equals(value)) { // if the item is equal to the value
				return true; // return true
			}
		}
		return false; // return false
	}
	
	public static int countCells(ListListMatrix<Boolean> grid) {
		int cells = 0;
		for(Boolean cell : grid) {
			if(cell != null) {
				cells++;
			}
		}
		return cells;
	}
	
	public static void main(String[] args) {
		try(Scanner scanner = new Scanner(System.in)) {
			ListListMatrix<Boolean> grid = new ListListMatrix<>();
			Random randomizer = new Random();
			int height = scanner.nextInt();
			int width = scanner.nextInt();
			for(int x = 0; x < height; x++) {
				List<Boolean> row = new ArrayList<>();
				for(int y = 0; y < width; y++) {
					row.add(randomizer.nextBoolean() ? true : null);
				}
				grid.addRow(row);
			}
			System.out.println("Start:\n" + stringifyGrid(grid));
			System.out.println(countCells(grid) + " cells\n\n");
			ListListMatrix<Boolean> processed = ConwayLife.process(grid);
			System.out.println("End:\n" + stringifyGrid(processed));
			System.out.println(countCells(processed) + " cells\n\n");
			//PeriodIterationsAndGrid periodetc = getPeriod(processed);
			//System.out.println("Period " + periodetc.period + " after " + periodetc.iterations + " iterations with grid:\n" + stringifyGrid(periodetc.grid));
		}
	}
	
	public static ListListMatrix<Boolean> process(ListListMatrix<Boolean> startingGrid) { // process(startingGrid)
		return ConwayLife.process(startingGrid, new Integer[] {2, 3}, new Integer[] {3}); // 2, 3 survive; 3 born
	}
	
	public static ListListMatrix<Boolean> process(ListListMatrix<Boolean> startingGrid, int iterations) { // process(startingGrid, iterations)
		return ConwayLife.process(startingGrid, iterations, new Integer[] {2, 3}, new Integer[] {3}); // 2, 3 survive; 3 born
	}
	
	public static ListListMatrix<Boolean> process(ListListMatrix<Boolean> startingGrid, int iterations, Integer[] survive, Integer[] born) {
		for(int i = 0; i < iterations; i++) { // repeat # of iterations
			startingGrid = ConwayLife.process(startingGrid, survive, born); // process the starting grid
		}
		return startingGrid; // return the starting grid
	}
	
	public static ListListMatrix<Boolean> process(ListListMatrix<Boolean> startingGrid, Integer[] survive, Integer[] born) { // process(startingGrid, survive, born)
		startingGrid = startingGrid.clone();
		startingGrid.addRow(0); // add a row to the beginning of the starting grid
		startingGrid.addRow(0); // add a row to the beginning of the starting grid
		startingGrid.addRow(); // add a row to the end of the starting grid
		startingGrid.addRow(); // add a row to the end of the starting grid
		startingGrid.addColumn(0); // add a column to the beginning of the starting grid
		startingGrid.addColumn(0); // add a column to the beginning of the starting grid
		startingGrid.addColumn(); // add a column to the end of the starting grid
		startingGrid.addColumn(); // add a column to the end of the starting grid
		
		ListListMatrix<Boolean> newGrid = new ListListMatrix<>();
		for(int row = 1; row < startingGrid.getHeight() - 1; row++) { // for each row from second to second-to-last
			newGrid.addRow(); // add an row to the new grid
			newGrid.setWidth(startingGrid.getWidth() - 2); // set the new grid's width to the starting grid's width minus 2
			for(int column = 1; column < startingGrid.getWidth() - 1; column++) { // for each column from second to second-to-last
				if(startingGrid.getItem(row, column) != null) { // if the current cell is on
					if( // if the number of surrounding squares on is in the list of survival numbers
					/*@formatter:off*/
					ConwayLife.contains(survive,
						(startingGrid.getItem(row - 1, column - 1) != null ? 1 : 0) +
						(startingGrid.getItem(row - 1, column    ) != null ? 1 : 0) +
						(startingGrid.getItem(row - 1, column + 1) != null ? 1 : 0) +
						(startingGrid.getItem(row,     column - 1) != null ? 1 : 0) +
						(startingGrid.getItem(row,     column + 1) != null ? 1 : 0) +
						(startingGrid.getItem(row + 1, column - 1) != null ? 1 : 0) +
						(startingGrid.getItem(row + 1, column    ) != null ? 1 : 0) +
						(startingGrid.getItem(row + 1, column + 1) != null ? 1 : 0)
					)
					/*@formatter:on*/
					) {
						newGrid.getRow(row - 1).set(column - 1, true); // add a true to the last row of the new grid
					} else {
						newGrid.getRow(row - 1).set(column - 1, null); // add a null to the last row of the new grid
					}
				} else { // otherwise (if the current cell is off)
					if( // if the number of surrounding squares on is in the list of birth numbers
					/*@formatter:off*/
					ConwayLife.contains(born,
						(startingGrid.getItem(row - 1, column - 1) != null ? 1 : 0) +
						(startingGrid.getItem(row - 1, column    ) != null ? 1 : 0) +
						(startingGrid.getItem(row - 1, column + 1) != null ? 1 : 0) +
						(startingGrid.getItem(row,     column - 1) != null ? 1 : 0) +
						(startingGrid.getItem(row,     column + 1) != null ? 1 : 0) +
						(startingGrid.getItem(row + 1, column - 1) != null ? 1 : 0) +
						(startingGrid.getItem(row + 1, column    ) != null ? 1 : 0) +
						(startingGrid.getItem(row + 1, column + 1) != null ? 1 : 0)
					)
					/*@formatter:on*/
					) {
						newGrid.getRow(row - 1).set(column - 1, true); // add a true to the new grid
					} else {
						newGrid.getRow(row - 1).set(column - 1, null); // add a null to the new grid
					}
				}
			}
		}
		try {
			while(true) { // forever
				if(newGrid.getRow(0).contains(true)) { // if the first row has any cells on
					break; // stop looping
				}
				newGrid.removeRow(0); // remove the first row
			}
			while(true) { // forever
				if(newGrid.getRow(newGrid.getHeight() - 1).contains(true)) { // if the last row has any cells on
					break; // stop looping
				}
				newGrid.removeRow(newGrid.getHeight() - 1); // remove the last row
			}
			while(true) { // forever
				if(newGrid.getColumn(0).contains(true)) { // if the first column has any cells on
					break; // stop looping
				}
				newGrid.removeColumn(0); // remove the first column
			}
			while(true) { // forever
				if(newGrid.getColumn(newGrid.getWidth() - 1).contains(true)) { // if the last column has any cells on
					break; // stop looping
				}
				newGrid.removeColumn(newGrid.getWidth() - 1); // remove the last column
			}
		} catch(IndexOutOfBoundsException e) {}
		return newGrid; // return the starting grid
	}
	
	public static String stringifyGrid(ListListMatrix<Boolean> grid) {
		String string = "";
		for(List<Boolean> row : grid.getRows()) {
			for(Boolean item : row) {
				string += item != null ? "#" : " ";
			}
			string += "\n";
		}
		return string;
	}
}



package com.solly;


import java.awt.EventQueue;

import javax.swing.DefaultCellEditor;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JTable;
import javax.swing.table.TableColumn;


public class ConwayLifeGUI {
	private JFrame	frame;
	private JTable	table;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			@SuppressWarnings("synthetic-access") public void run() {
				ConwayLifeGUI window = new ConwayLifeGUI();
				window.frame.setVisible(true);
			}
		});
	}
	
	/**
	 * Create the application.
	 */
	public ConwayLifeGUI() {
		initialize();
	}
	
	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		this.frame = new JFrame();
		this.table = new JTable();
		this.frame.getContentPane().add(this.table);
		this.table.setCellEditor(new DefaultCellEditor(new JCheckBox()));
		this.table.getColumnModel().addColumn(new TableColumn());
	}
}

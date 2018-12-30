package com.solly.codeedit;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.KeyStroke;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

import java.awt.event.KeyEvent;
import java.awt.event.InputEvent;
import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import javax.swing.JSeparator;

public class MainWindow {
	
	public JFrame frame;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainWindow window = new MainWindow();
					window.frame.setVisible(true);
				} catch(Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	/**
	 * Create the application.
	 * @throws UnsupportedLookAndFeelException 
	 * @throws IllegalAccessException 
	 * @throws InstantiationException 
	 * @throws ClassNotFoundException 
	 */
	public MainWindow() throws ClassNotFoundException, InstantiationException, IllegalAccessException, UnsupportedLookAndFeelException {
		initialize();
	}
	
	/**
	 * Initialize the contents of the frame.
	 * @throws UnsupportedLookAndFeelException 
	 * @throws IllegalAccessException 
	 * @throws InstantiationException 
	 * @throws ClassNotFoundException 
	 */
	private void initialize() throws ClassNotFoundException, InstantiationException, IllegalAccessException, UnsupportedLookAndFeelException {
		this.frame = new JFrame();
		this.frame.addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent arg0) {
				// TODO Show confirmation dialog if not saved.
			}
		});
		this.frame.setExtendedState(Frame.MAXIMIZED_BOTH);
		this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		
		JMenuBar menuBar = new JMenuBar();
		this.frame.setJMenuBar(menuBar);
		
		JMenu file = new JMenu("File");
		file.setMnemonic('F');
		file.setMnemonic(KeyEvent.VK_F);
		menuBar.add(file);
		
		JMenu file_new = new JMenu("New");
		file_new.setMnemonic('N');
		file_new.setMnemonic(KeyEvent.VK_N);
		file.add(file_new);
		
		JMenuItem file_open = new JMenuItem("Open");
		file_open.setMnemonic('O');
		file_open.setMnemonic(KeyEvent.VK_O);
		file_open.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, InputEvent.CTRL_MASK));
		file.add(file_open);
		
		JSeparator separator = new JSeparator();
		file.add(separator);
		
		JMenuItem mntmClose = new JMenuItem("Close");
		mntmClose.setMnemonic('C');
		mntmClose.setMnemonic(KeyEvent.VK_C);
		file.add(mntmClose);
		
		JMenuItem mntmCloseAll = new JMenuItem("Close all");
		file.add(mntmCloseAll);
		
		JSeparator separator_1 = new JSeparator();
		file.add(separator_1);
		
		JMenuItem file_save = new JMenuItem("Save");
		file_save.setMnemonic('S');
		file_save.setMnemonic(KeyEvent.VK_S);
		file_save.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, InputEvent.CTRL_MASK));
		file.add(file_save);
		
		JMenuItem mntmSaveAs = new JMenuItem("Save as...");
		file.add(mntmSaveAs);
		
		JMenuItem mntmSaveAll = new JMenuItem("Save all");
		file.add(mntmSaveAll);
	}
}

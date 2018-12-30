/*
 * Creates a new javax.swing.JFrame and provides various methods for interacting with it.
 */


package apis.graphics;


import java.awt.EventQueue;

import javax.swing.JFrame;


public class Window {
	public class Main extends Window {
		
		public Main() {
			super();
		}
		
		public Main(String title) {
			super(title);
		}
		
		void initialize() {
			this.frame = new JFrame();
			this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		}
		
		void initialize(String title) {
			this.frame = new JFrame();
			this.frame.setTitle(title);
			this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		}
		
	}
	
	public JFrame frame;
	
	public Window() {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				initialize();
			}
		});
	}
	
	public Window(String title) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				initialize(title);
			}
		});
	}
	
	void initialize() {
		this.frame = new JFrame();
	}
	
	void initialize(String title) {
		this.frame = new JFrame();
		this.frame.setTitle(title);
	}
}

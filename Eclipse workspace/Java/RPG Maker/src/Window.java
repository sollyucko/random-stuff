import java.awt.BorderLayout;
import java.awt.Component;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;

import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JLayeredPane;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTabbedPane;
import javax.swing.KeyStroke;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

import org.eclipse.jdt.annotation.NonNullByDefault;


public @NonNullByDefault({}) class Window {
	
	public JFrame frame;
	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		} catch(@SuppressWarnings("unused") ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException e) {}
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Window window = new Window();
					window.frame.setVisible(true);
				} catch(Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	/**
	 * Create the application.
	 */
	public Window() {
		initialize();
	}
	
	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		this.frame = new JFrame();
		this.frame.setTitle("RPG Maker");
		this.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.frame.setExtendedState(this.frame.getExtendedState() | JFrame.MAXIMIZED_BOTH);
		
		JMenuBar menuBar = new JMenuBar();
		this.frame.setJMenuBar(menuBar);
		
		JMenu file = new JMenu("File");
		file.setMnemonic('f');
		menuBar.add(file);
		
		JMenuItem new_ = new JMenuItem("New");
		new_.setMnemonic('n');
		new_.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, InputEvent.CTRL_MASK));
		file.add(new_);
		
		JMenuItem open = new JMenuItem("Open");
		open.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, InputEvent.CTRL_MASK));
		open.setMnemonic('o');
		file.add(open);
		
		JMenuItem save = new JMenuItem("Save");
		save.setMnemonic('s');
		save.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, InputEvent.CTRL_MASK));
		file.add(save);
		
		JMenuItem export = new JMenuItem("Export");
		export.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				switch(JOptionPane.showOptionDialog(export, "", "Export", JOptionPane.OK_CANCEL_OPTION, JOptionPane.QUESTION_MESSAGE, null, new String[] {".exe", ".app"}, null)) {
					case 0: // .exe
						System.out.println(".exe");
						break;
					case 1: // .app
						System.out.println(".app");
						break;
					default:
						throw new RuntimeException("Invalid option");
				}
			}
		});
		export.setMnemonic('e');
		export.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, InputEvent.CTRL_MASK | InputEvent.SHIFT_MASK));
		file.add(export);
		
		JMenu edit = new JMenu("Edit");
		edit.setMnemonic('e');
		menuBar.add(edit);
		
		JMenuItem undo = new JMenuItem("Undo");
		undo.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Z, InputEvent.CTRL_MASK));
		undo.setMnemonic('u');
		edit.add(undo);
		
		JMenuItem redo = new JMenuItem("Redo");
		redo.setMnemonic('r');
		redo.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Y, InputEvent.CTRL_MASK));
		edit.add(redo);
		
		edit.addSeparator();
		
		JMenuItem cut = new JMenuItem("Cut");
		cut.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_X, InputEvent.CTRL_MASK));
		cut.setMnemonic('t');
		edit.add(cut);
		
		JMenuItem copy = new JMenuItem("Copy");
		copy.setMnemonic('c');
		copy.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_C, InputEvent.CTRL_MASK));
		edit.add(copy);
		
		JTabbedPane views = new JTabbedPane(JTabbedPane.LEFT);
		this.frame.getContentPane().add(views, BorderLayout.CENTER);
		
		JLayeredPane mapPane = new JLayeredPane();
		views.addTab("Map", null, mapPane, null);
		
		JPanel panel = new JPanel();
		mapPane.add(panel);
		panel.setLayout(new GridLayout(1, 0, 0, 0));
		
		JInternalFrame layerFrame = new JInternalFrame("Layers");
		layerFrame.setLocation(mapPane.getX() + mapPane.getWidth(), mapPane.getY() + mapPane.getHeight());
		layerFrame.setAlignmentY(Component.BOTTOM_ALIGNMENT);
		layerFrame.setAlignmentX(Component.RIGHT_ALIGNMENT);
		layerFrame.setResizable(true);
		layerFrame.setVisible(true);
		mapPane.add(layerFrame);
		
		JScrollPane layers = new JScrollPane();
		
		layerFrame.getContentPane().add(layers, BorderLayout.SOUTH);
		layerFrame.pack();
		
		JLayeredPane eventTab = new JLayeredPane();
		views.addTab("Events", null, eventTab, null);
		
		Layer layer = new Layer("Layer");
		this.frame.getContentPane().add(layer, BorderLayout.NORTH);
		layer.setBounds(new Rectangle(10, 10, 10, 10));
		layer.setLayout(new FlowLayout(FlowLayout.CENTER, 5, 5));
	}
	
	@SuppressWarnings("serial") public static class Layer extends JPanel {
		String name;
		
		public Layer() {
			this.name = JOptionPane.showInputDialog(this, "Layer name", "Layer name", JOptionPane.QUESTION_MESSAGE);
			System.out.println(this);
			this.setLayout(new BorderLayout());
		}
		
		public Layer(String name) {
			this.name = name;
			System.out.println(this);
			this.setLayout(new BorderLayout());
		}
		
		public Dimension getPreferredSize() {
			System.out.println(super.getPreferredSize());
			return super.getPreferredSize();
		}
		
		public void paintComponent(Graphics graphic) {
			super.paintComponent(graphic);
			System.out.println(this);
			graphic.drawString(this.name, 10, 20);
			System.out.println(graphic);
		}
		
		protected String paramString() {
			return this.name;
		}
		
		public String toString() {
			return this.name;
		}
	}
}

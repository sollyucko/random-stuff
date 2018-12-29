package io.github.sollyucko.ide;

import javax.swing.*;
import java.util.HashSet;
import java.util.Set;

import static javax.swing.SwingUtilities.invokeLater;

public class IDE {
	private Set<ComponentType> componentTypes = new HashSet<>();
	private Set<FileType> fileTypes = new HashSet<>();
	
	private IDE(String[] args) {
		for (Plugin plugin : PluginLoader.load_plugins()) {
			fileTypes.addAll(plugin.getFileTypes());
			componentTypes.addAll(plugin.getComponentTypes());
		}
	}
	
	public static void main(String[] args) {
		invokeLater(new IDE(args)::createAndShowFrame);
	}
	
	private JMenu createJMenu(String text, JMenuItem... menuItems) {
		JMenu menu = new JMenu(text);
		
		for (JMenuItem menuItem : menuItems) {
			menu.add(menuItem);
		}
		
		return menu;
	}
	
	private JMenuBar createJMenuBar(JMenu... menus) {
		JMenuBar menuBar = new JMenuBar();
		
		for (JMenu menuItem : menus) {
			menuBar.add(menuItem);
		}
		
		return menuBar;
	}
	
	private void createAndShowFrame() {
		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		} catch (ClassNotFoundException | InstantiationException | UnsupportedLookAndFeelException | IllegalAccessException e) {
			throw new RuntimeException(e);
		}
		JFrame frame = new JFrame();
		frame.add(
			createJMenuBar(
				createJMenu("File",
					createJMenu("New",
			            this.getNewFileMenuItems()
		            ),
				    createJMenuItem("Test")
				)
			)
		);
		frame.setSize(500, 500);
		frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
	
	private JMenuItem[] getNewFileMenuItems() {
		Set<JMenuItem> items = new HashSet<>();
		
		for(FileType fileType : fileTypes) {
			items.add(createJMenuItem(fileType.getFileExtension(), new CreateFileAction(fileType)));
		}
		return items.toArray(new JMenuItem[]{});
	}
	
	private JMenuItem createJMenuItem() {return createJMenuItem(null, null, null);}
	private JMenuItem createJMenuItem(String text) {return createJMenuItem(text, null, null);}
	private JMenuItem createJMenuItem(Action action) {return createJMenuItem(null, action, null);}
	private JMenuItem createJMenuItem(String text, Action action) {return createJMenuItem(text, action, null);}
	private JMenuItem createJMenuItem(Icon icon) {return createJMenuItem(null, null, icon);}
	private JMenuItem createJMenuItem(String text, Icon icon) {return createJMenuItem(text, null, icon);}
	private JMenuItem createJMenuItem(Action action, Icon icon) {return createJMenuItem(null, action, icon);}
	
	private JMenuItem createJMenuItem(String text, Action action, Icon icon) {
		JMenuItem item = new JMenuItem();
		
		if(text != null) item.setText(text);
		if(action != null) item.setAction(action);
		if(icon != null) item.setIcon(icon);
		return item;
	}
}
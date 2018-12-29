package io.github.sollyucko.utils.swing;

import lombok.SneakyThrows;
import lombok.experimental.UtilityClass;

import javax.swing.*;
import java.awt.*;

@UtilityClass
public class SwingUtils {
	@SneakyThrows
	public Frame createFrameWithDefaults(Component... components) {
		UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		
		JFrame frame = new JFrame();
		
		for (Component component : components) {
			frame.add(component);
		}
		
		frame.pack();
		frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		frame.setVisible(true);
		return frame;
	}
	
	public JMenu createJMenu(String text, JMenuItem... menuItems) {
		JMenu menu = new JMenu(text);
		
		for (JMenuItem menuItem : menuItems) {
			menu.add(menuItem);
		}
		
		return menu;
	}
	
	public JMenuBar createJMenuBar(JMenu... menus) {
		JMenuBar menuBar = new JMenuBar();
		
		for (JMenu menuItem : menus) {
			menuBar.add(menuItem);
		}
		
		return menuBar;
	}
	
	public JMenuItem createJMenuItem(String text, Action action, Icon icon) {
		JMenuItem item = new JMenuItem();
		
		if (text != null) { item.setText(text); }
		if (action != null) { item.setAction(action); }
		if (icon != null) { item.setIcon(icon); }
		return item;
	}
}

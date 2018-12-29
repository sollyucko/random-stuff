package io.github.sollyucko.ide;

import javax.swing.*;
import java.awt.*;

public interface ToolWindow {
	Component getComponent();
	Icon getIcon();
	String getName();
}

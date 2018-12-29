package io.github.sollyucko.ide;

import javax.swing.*;
import java.awt.*;
import java.io.File;

public interface FileType {
	Icon getIcon();
	String getName();
	Component openFile(File file);
}

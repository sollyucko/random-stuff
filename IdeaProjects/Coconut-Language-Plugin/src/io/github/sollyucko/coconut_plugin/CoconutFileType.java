package io.github.sollyucko.coconut_plugin;

import com.intellij.openapi.vfs.VirtualFile;
import com.jetbrains.python.PythonFileType;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import javax.swing.*;

import static io.github.sollyucko.coconut_plugin.icons.CoconutIcons.FILE;

public class CoconutFileType extends PythonFileType {
	public static final CoconutFileType INSTANCE = new CoconutFileType();
	
	private CoconutFileType() {
		super(CoconutLanguage.INSTANCE);
	}
	
	@Override
	public @NotNull String getDefaultExtension() {
		return "coco";
	}
	
	@Override
	public @NotNull String getDescription() {
		return "Coconut file";
	}
	
	@Override
	public @NotNull Icon getIcon() {
		return FILE;
	}
	
	@Override
	public @NotNull String getName() {
		return "Coconut file";
	}
}

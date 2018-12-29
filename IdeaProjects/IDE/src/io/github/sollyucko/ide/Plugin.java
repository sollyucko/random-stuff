package io.github.sollyucko.ide;

import java.util.*;

public interface Plugin {
	default Set<FileType> getFileTypes() {
		return Collections.emptySet();
	}
	
	default Set<ToolWindow> getToolWindows() {
		return Collections.emptySet();
	}
}

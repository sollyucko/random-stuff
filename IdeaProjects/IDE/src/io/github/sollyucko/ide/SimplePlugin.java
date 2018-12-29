package io.github.sollyucko.ide;

import java.util.Set;

public class SimplePlugin implements Plugin {
	private final Set<FileType> fileTypes;
	private final Set<ToolWindow> toolWindows;
	
	public <T> SimplePlugin(Set<FileType> fileTypes, Set<ToolWindow> toolWindows) {
		this.fileTypes = fileTypes;
		this.toolWindows = toolWindows;
	}
	
	
	@Override
	public Set<FileType> getFileTypes() {
		return this.fileTypes;
	}
	
	@Override
	public Set<ToolWindow> getToolWindows() {
		return this.toolWindows;
	}
}

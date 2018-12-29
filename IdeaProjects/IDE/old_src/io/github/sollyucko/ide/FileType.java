package io.github.sollyucko.ide;

import java.io.File;

public interface FileType {
	String getFileExtension();
	FileHandler getFileHandler();
	File createFile();
}

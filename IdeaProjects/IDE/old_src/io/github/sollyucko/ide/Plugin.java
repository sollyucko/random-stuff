package io.github.sollyucko.ide;

import java.util.Set;

public interface Plugin {
	Set<FileType> getFileTypes();
	Set<ComponentType> getComponentTypes();
}

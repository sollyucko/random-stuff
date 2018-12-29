package io.github.sollyucko.coconut_plugin;

import com.intellij.openapi.fileTypes.FileTypeConsumer;
import com.intellij.openapi.fileTypes.FileTypeFactory;
import org.jetbrains.annotations.NotNull;

public class CoconutFileTypeFactory extends FileTypeFactory {
	
	@Override
	public void createFileTypes(@NotNull FileTypeConsumer consumer) {
		consumer.consume(CoconutFileType.INSTANCE);
	}
}

package io.github.sollyucko.coconut_plugin.psi;

import com.intellij.psi.tree.IElementType;
import io.github.sollyucko.coconut_plugin.CoconutLanguage;
import org.jetbrains.annotations.NonNls;
import org.jetbrains.annotations.NotNull;

public class CoconutElementType extends IElementType {
	public CoconutElementType(@NotNull @NonNls String debugName) {
		super(debugName, CoconutLanguage.INSTANCE);
	}
}

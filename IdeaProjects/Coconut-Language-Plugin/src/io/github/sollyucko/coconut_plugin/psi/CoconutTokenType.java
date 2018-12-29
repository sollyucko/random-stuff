package io.github.sollyucko.coconut_plugin.psi;

import com.intellij.psi.tree.IElementType;
import io.github.sollyucko.coconut_plugin.CoconutLanguage;
import org.jetbrains.annotations.NonNls;
import org.jetbrains.annotations.NotNull;

public class CoconutTokenType extends IElementType {
	public CoconutTokenType(@NotNull @NonNls String debugName) {
		super(debugName, CoconutLanguage.INSTANCE);
	}
	
	@Override
	public String toString() {
		return "CoconutTokenType." + super.toString();
	}
}

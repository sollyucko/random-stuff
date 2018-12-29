package io.github.sollyucko.coconut_plugin;

import com.intellij.lang.Language;

public class CoconutLanguage extends Language {
	public static final Language INSTANCE = new CoconutLanguage();
	
	private CoconutLanguage() {
		super("Coconut");
	}
}

package io.github.sollyucko.ide;

import com.google.common.reflect.ClassPath;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.Set;
import java.util.stream.Collectors;

//import static io.github.sollyucko.utils.swing.SwingUtils.*;
//import static javax.swing.SwingUtilities.invokeLater;

public class IDE {
	private static Set<Class<? extends Plugin>> loadPlugins(File pluginDirectory) throws IOException {
		//noinspection unchecked
		System.out.println(ClassPath.from(new URLClassLoader(new URL[]{pluginDirectory.toURI().toURL()}))
		                            .getAllClasses()
		                            .parallelStream()
		                            .filter(x -> !x.getPackageName().startsWith("java."))
		                            .map((ClassPath.ClassInfo classInfo) -> {System.out.println(classInfo); return classInfo.load();})
		                            .filter(Plugin.class::isAssignableFrom)
		                            .map(x -> (Class<? extends Plugin>) x)
		                            .collect(Collectors.toSet()));

		return null;
	}
	
	public static void main(String[] args) throws IOException {
		System.out.println(loadPlugins(new File("not_plugins/")));
		//		//@formatter:off
		//		invokeLater(() -> createFrameWithDefaults(
		//				createJMenuBar(
		//						createJMenu(
		//								"File"
		//						)
		//				)
		//		));
		//		//@formatter:on
	}
}

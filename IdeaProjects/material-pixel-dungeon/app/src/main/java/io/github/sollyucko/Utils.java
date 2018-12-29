package io.github.sollyucko;

import org.jetbrains.annotations.NotNull;

@SuppressWarnings("WeakerAccess")
public final class Utils {
	@NotNull
	public static RuntimeException wrapException(@NotNull Exception e) {
		if (e instanceof RuntimeException) {
			return (RuntimeException) e;
		} else {
			return new RuntimeException(e);
		}
	}
	
	@NotNull
	private static Class<?>[] getClasses(@NotNull Object[] args) {
		Class<?>[] argTypes = new Class[args.length];
		
		for (int i = 0; i < args.length; i++) {
			argTypes[i] = args[i].getClass();
		}
		
		return argTypes;
	}
	
	@NotNull
	public static Object callSuperMethod(@NotNull Object object, @NotNull String name, @NotNull Object... args) {
		return callMethod(object, object.getClass().getSuperclass(), name, args, getClasses(args));
		
	}
	
	@NotNull
	public static Object callMethod(@NotNull Object object, @NotNull String name, @NotNull Object... args) {
		return callMethod(object, object.getClass(), name, args, getClasses(args));
	}
	
	@NotNull
	public static Object callMethod(@NotNull Object object, Class<?> objectClass, @NotNull String name, Object[] args, Class<?>[] argClasses) {
		try {
			return objectClass.getMethod(name, argClasses).invoke(object, args);
		} catch (Exception e) {
			throw wrapException(e);
		}
	}
}

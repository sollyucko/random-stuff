def bootstrap(runtime):
	runtime.builtins.Object = Object = runtime.Object()
	runtime.builtins.Class = Class = runtime.Object()
	
	Object.set_internal_attribute('class', Class)
	Class.set_internal_attribute('class', Class)
	
	Object.set_internal_attribute('name', 'Object')
	Class.set_internal_attribute('name', 'Class')
	
	Object.set_internal_attribute('mro', [Object])
	Class.set_internal_attribute('mro', [Class, Object])

def bootstrap(runtime):
	@runtime.set_builtin('Class')
	class Class:
		parents = []
	
	Class.class_ = Class
	
	@runtime.set_builtin('Object')
	class Object:
		class_ = Class
		parents = []
		
		@staticmethod
		def new(cls):
			return cls()
	
	Class.parents.append(Object)
	
	@runtime.set_builtin('Integer')
	class Integer:
		class_ = Class
		parents = []
		
		@staticmethod
		def new(cls=None):
			if cls == None:
				cls = Integer
			
			obj = Object.new(cls)
			obj.class_ = cls
			obj.value = 0
			return obj
	
	@runtime.set_builtin('Float')
	class Float:
		class_ = Class
		parents = []
		
		@staticmethod
		def new(cls=None):
			if cls == None:
				cls = Float
			
			obj = Object.new(cls)
			obj.class_ = cls
			obj.value = 0
			return obj

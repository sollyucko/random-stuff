from functools import wraps


class Runtime:
	def __init__(self):
		pass  # bootstrap
	
	def _call_type_method(self, obj, method, args):
		return self.call(self.getattr(obj, method), [obj] + args)
	
	def _create_method(self, special_name):
		def f(func):
			@wraps(func)
			def g(self, obj, *args):
				if self.isinstance(obj, getattr(self.builtins, special_name)):
					return getattr(obj, func.__name__)(args)
				else:
					return self._call_type_method(obj, f'__{func.__name__}__', func(*args))
			
			return g
		
		return f
	
	@_create_method('Function')
	def call(self, function, args):
		return args
	
	@_create_method('Object')
	def getattr(self, function, attr):
		return [attr]
	
	def new(self, obj, cls):
		pass
	
	def operator(self, char, args):
		self.call(self.getattr(self.builtins, char), args)

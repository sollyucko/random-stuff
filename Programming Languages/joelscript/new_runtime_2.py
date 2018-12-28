from types import SimpleNamespace
from typing import List

from .bootstrapper_2 import bootstrap
from .stdlib import init_stdlib

operator_magic = {
	'+': '__add__',
	'-': '__sub__',
	'*': '__mul__',
	'/': '__truediv__',
	'**': '__pow__'
}


class Runtime:
	def __init__(self):
		self.builtins = SimpleNamespace()
		bootstrap(self)
		init_stdlib(self)
		self.scopes = [{}]
	
	def builtin(self, cls_or_f):
		setattr(self.builtins, cls_or_f.__name__, cls_or_f)
		return cls_or_f
	
	def builtin_method(self, obj):
		def decorator(f):
			obj.setattr(f.__name__, f)
			return f
		
		return decorator
	
	def builtin_magic_method(self, obj):
		def decorator(f):
			setattr(obj, f.__name__, f)
			return f
		
		return decorator
	
	def enter_scope(self, scope):
		self.scopes.append(scope)
	
	def exit_scope(self):
		return self.scopes.pop()
	
	def get_local(self, name: str):
		for scope in reversed(self.scopes):
			if name in scope:
				return scope[name]
		else:
			self.throw(self.builtins.NameError.new(name))
	
	def get_global(self, name: str):
		if name in self.scopes[-1]:
			return self.scopes[-1][name]
		else:
			self.throw(self.builtins.NameError.new(name))
	
	def set_local(self, name: str, value):
		for scope in reversed(self.scopes):
			if name in scope:
				scope[name] = value
				break
		else:
			self.scopes[-1][name] = value
	
	def set_global(self, name: str, value: 'Object'):
		self.scopes[0][name] = value
	
	def from_native(self, native):
		if isinstance(native, int):
			class_name = 'Integer'
		elif isinstance(native, float):
			class_name = 'Float'
		elif isinstance(native, str):
			class_name = 'String'
		
		obj = getattr(self.builtins, class_name).new()
		obj.value = native
		return obj
	
	def operator(self, char: str, args: List['Object']):
		return getattr(args[0], operator_magic[char])(*args[1:])


class Object:
	def __init__(self):
		self.attributes = {}
	
	def getattr(self, name: str):
		return self.attributes[name]
	
	def setattr(self, name: str, value: 'Object'):
		self.attributes[name] = value


class Class(Object):
	def init(self, name: str):
		self.setattr('name', name)
		# self.setattr('parents', b.List.init())
		# self.setattr('metaclass', b.None)
		self.parents = []
		self.metaclass = None
		
		def init(self, args: List['Object']):
			pass
		
		def call(self, args: List['Object']):
			obj = self.type.new(args)
			obj.init(args)
			return obj


class Function(Object):
	def init(self, action, name: str = None):
		if name is None:
			name = action.__name__
		
		self.action = action
		self.name = name
	
	def call(self, args):
		return self.action(*args)

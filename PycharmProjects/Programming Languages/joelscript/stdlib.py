import random
import time


def init_stdlib(runtime):
	runtime.builtins.Integer = Integer = runtime.Type('Integer')
	
	@runtime.builtin_magic_method(Integer)
	@runtime.Function
	def init(args):
		if len(args) == 1:
			this, = args
			this.value = 0
		elif len(args) == 2:
			this, value = args
			this.value = value
	
	# b = runtime.builtins
	
	'''
	@runtime.builtin
	class Integer(b.Object, metaclass=b.Class):
		def __init__(self, args):
			if len(args) > 0:
				self.value = args[0]
			else:
				self.value = 0
		
		def __add__(self, other):
			if isinstance(other, Integer):
				return self.value + other.value
			else:
				return NotImplemented
		
		def __str__(self):
			return self.value
		
		def __repr__(self):
			return f'{type(self).__name__}({self.value})'
	'''


class OldStuff:  # just for now
	class Timer:
		def __init__(self):
			self.running = False
			self.startTime = None
			self.add = 0
		
		def start(self):
			self.running = True
			self.startTime = time.time() * 1000 - self.add
			self.add = 0
		
		def stop(self):
			if self.running:
				self.running = False
				self.add = time.time() * 1000 - self.startTime
				self.startTime = None
		
		def reset(self):
			self.running = False
			self.startTime = None
			self.add = 0
		
		def get(self):
			if self.startTime == None:
				return self.add
			else:
				return time.time() * 1000 - self.startTime + self.add
	
	class Error:
		def __init__(self, errorType, errorText):
			self.errorType = errorType
			self.errorText = errorText
		
		def get_print_text(self):
			return self.errorType + ": " + self.errorText
	
	class JoelscriptFunctions:
		# Class function calling Syntax: ...classObject.function_name(parameters)...;
		def __init__(self):
			self.variables = dict()
			self.functions = dict()
		
		def get_var(self, name):  # Syntax: ...name...;
			if name in self.variables:
				return self.variables[name]
			else:
				return Error("NameError", "name " + name + " is not defined")
		
		def set_var(self, name, value):  # Syntax: var name = "value"; (use var even if already defined, var is ALWAYS used when setting vars)
			self.variables[name] = value
			return value
		
		def calculation(self, statement):
			return eval(statement)
		
		def _print(self, *text, **kwargs):  # Syntax: print("text","more","and","more",end="something");
			print(" ".join(text))
			return
		
		def _input(self, message, varType):  # Syntax: ...input("Hello World", str)...;
			if varType == "obj":
				return input(message + " ")
			else:
				return eval(varType + "(input(message))")
		
		def _random(self, lower, upper, interval):  # Syntax: ...random(1.2,9.6,0.2)...;
			self.i = 1
			while int(self.i * interval) != self.i * interval:
				self.i += 1
			self.val = random.randint(lower * self.i, upper * self.i)
			return self.val / self.i
		
		def _millis(self):  # Syntax: ...millis()...;
			return time.time() * 1000
		
		def _Timer(self):  # Class, Line 16; Syntax: ...Timer()...;
			return Timer()

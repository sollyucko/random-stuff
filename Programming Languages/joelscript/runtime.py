# Solly made new version, don't edit it

import random
import time

'''
class function:
    def __init__(self,code,*params):
        self.parameters = dict()
        for i in params:
            self.parameters[i] = None
        self.code = code
    def call(variables,*params):
        self.iteration = 0
        for i in parameters:
            self.iteration += 1
            self.variables[i] = params[self.iteration-1]
'''


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


class Runtime:
	def __init__(self):
		pass
	
	def operator(self, char, args):
		if char == '+':
			if len(args) == 1:
				return args[0]
			elif len(args) == 2:
				return args[0] + args[1]
	
	# etc.

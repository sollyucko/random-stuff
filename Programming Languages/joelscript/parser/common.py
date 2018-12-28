class Base:
	def __init__(self, src):
		self.src = src
	
	def __str__(self):
		return self.src
	
	def __repr__(self):
		return f'{type(self).__name__}({self.src})'


class String(Base): pass


class Integer(Base): pass


class Float(Base): pass


class Operator(Base):
	def __init__(self, char, arg_count):
		super().__init__(char)
		self.arg_count = arg_count
	
	def __repr__(self):
		return f'{type(self).__name__}({self.src!r}, {self.arg_count!r})'


class Paren(Base): pass


class StartParen(Paren): pass


class EndParen(Paren): pass


class JSSyntaxError(SyntaxError):
	pass

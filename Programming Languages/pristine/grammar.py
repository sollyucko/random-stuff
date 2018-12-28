from pyparsing import javaStyleComment, pythonStyleComment

comment = javaStyleComment ^ pythonStyleComment
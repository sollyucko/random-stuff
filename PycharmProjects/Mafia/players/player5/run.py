from os.path import basename, dirname

from players.player0 import run

if __name__ == '__main__':
	print(__file__)
	
	run.main(basename(dirname(__file__)))

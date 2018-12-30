from contextlib import redirect_stdout
from enum import Enum, auto
from pickle import dump, load
from sys import stdout
from typing import Dict, Set

from parse import parse


class Role(Enum):
	VILLAGER = auto()
	MAFIA = auto()
	COP = auto()
	DOCTOR = auto()


roles = {
	'a member of the mafia': Role.MAFIA,
	'the cop': Role.COP,
	'the doctor': Role.DOCTOR
}


def delimited_list(delimiter):
	def f(string):
		return string.split(delimiter)
	
	return f


class State:
	name: str
	role: Role
	players: Dict[str, Set[Role]]
	day: int
	
	def __init__(self, name: str, player_string: str):
		self.name = name
		self.role = Role.VILLAGER
		self.players = {player: set(Role) for player in player_string.split('\n')}
		self.players[self.name] = {self.role}
		self.day = 0
	
	def logic(self, inp: str):
		stdout.write(inp)
		
		if inp.startswith('Rise and shine!'):
			# Day 0
			if 'allies' in inp:
				parsed = parse('Rise and shine! Today is day 0.\nNo voting will occur today.\nBe warned: Tonight the mafia will strike.\nYou are {role}.\nYour allies are:\n{allies:list}', inp, {'list': delimited_list('\n')})
				
				for ally in parsed['allies']:
					self.players[ally] = {roles[parsed['role']]}
				
				self.players[self.name] = {roles[parsed['role']]}
			
			if 'You are ' in inp:
				parsed = parse('Rise and shine! Today is day 0.\nNo voting will occur today.\nBe warned: Tonight the mafia will strike.\nYou are {role}.', inp)
				
				self.role = roles[parsed['role']]
				self.players[self.name] = {self.role}
		
		elif self.role == Role.COP:
			parsed = parse('Dawn of day {day:d}.\nLast night, {dead_bot} was killed.\nInvestigations showed that {investigated_bot} is {alignment}-aligned.\nThese players are still alive: {remaining_players:list}', inp, {'list': delimited_list(', ')})
			
			self.day = parsed['day']
			self.players.pop(parsed['dead_bot'])
			self.players[parsed['investigated_bot']] = parsed['alignment']
		else:
			parsed = parse('Dawn of day {day:d}.\nLast night, {dead_bot} was killed.\nThese players are still alive: {remaining_players:list}', inp, {'list': delimited_list(', ')})
			
			self.day = parsed['day']
			self.players.pop(parsed['dead_bot'])


def main(name: str):
	print('Hi!')
	
	try:
		with open(f'../{name}/state.pickle', 'rb') as f:
			state = load(f)
	except FileNotFoundError:
		with open(f'../{name}/players', 'r') as f:
			state = State(name, f.read())
	
	with open(f'../{name}/from_server', 'r') as f:
		inp = f.read()
	
	with open(f'../{name}/to_server', 'w') as out_f:
		with redirect_stdout(out_f):
			state.logic(inp)
	
	with open(f'../{name}/state.pickle', 'wb') as f:
		dump(state, f)


if __name__ == '__main__':
	main('player0')

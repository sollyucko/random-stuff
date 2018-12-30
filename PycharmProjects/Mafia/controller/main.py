#!/bin/python3

from os import chdir, listdir, path, system
from os.path import isdir
from random import shuffle
from sys import exit, platform

from messages import messages


class Player(object):
	"""Player object for each bot."""
	vote = None
	role = 0
	
	# Messages to the player are stored in the player object themself until they
	# are sent, allowing more than one message to be sent with relative ease.
	messages = ''
	
	def __init__(self, name):
		self.name = name
	
	def add_message(self, s):
		self.messages += f'{s}\n'
	
	def get_role(self):
		if self.role == 1:
			return 'a mafioso'
		if self.role == 2:
			return 'the cop'
		if self.role == 3:
			return 'the doctor'
		return 'a villager'


def m_read(p):
	"""Return contents of player p's 'to_server' file, stripped of special
	characters, and clear the file.
	"""
	with open(f'{p.name}/to_server', 'r+') as f:
		s = ''.join(c for c in f.read() if c.isalnum() or c == ' ')
		f.truncate(0)
	
	return s


def m_write(players):
	"""Write messages to each player to that player's 'from_server' file"""
	# Convert Player object to a 1-element list to allow calling for a single
	# player
	if isinstance(players, Player):
		players = [players]
	
	for p in players:
		with open(f'{p.name}/from_server', 'w') as f:
			f.write(p.messages)
		p.messages = ''


def execute(p):
	"""Executes the bot associated with player p"""
	chdir(p.name)
	
	if platform.startswith('win'):
		system('run')
	else:
		system(path.join('.', 'run'))
	
	chdir('..')


def log(message):
	"""Append message + newline to the log file. This happens a lot, so this
	function exists as shorthand.
	"""
	with open('../tmp/log', 'a') as f:
		f.write(f'{message}\n')


def assign_roles(players):
	"""Make 1/3 of the players mafia, 1 player a cop and one player a doctor.
	Return the list of players, a list of mafia, the Player object of the cop and
	the Player object of the doctor.
	"""
	# Shuffling the whole list ensures you aren't assigning multiple roles to one
	# player, which we would have to account for with random.choice()
	shuffle(players)
	
	# Assign mafia
	for _ in range(len(players) // 3):
		players[0].role = 1
		players.append(players.pop(0))
	
	# Assign cop
	players[0].role = 2
	players.append(players.pop(0))
	
	# Assign doctor
	players[0].role = 3
	
	# Return list of players, list of mafia, cop and doctor
	return players, [player for player in players if player.role == 1], players[-1], players[0]


def get_players(players):
	"""Return a list of player objects for each player name in the input. Also
	return the doc, cop and a list of the mafia seperately.
	"""
	# At least six players are required.
	if len(players) < 6:
		exit('Not enough players.')
	
	# Convert to Player object, assign roles, and return
	return assign_roles(list(map(Player, players)))


def kill(p, players, mafia, cop, doctor):
	"""Return every role the player p might be filling, with them removed."""
	
	players.remove(p)
	
	if p in mafia:
		mafia.remove(p)
	if cop is p:
		cop = None
	if doctor is p:
		doctor = None
	
	return players, mafia, cop, doctor


def main():
	# Clear the log file, so it's fresh for the new game
	with open('../tmp/log', 'w') as f:
		f.truncate(0)
	
	# Get player objects for all players, the doc, the cop, and a list of mafia
	chdir('../players')
	
	players = [player for player in listdir('.') if isdir(player)]
	
	players, mafia, cop, doctor = get_players(players)
	
	# Give everyone a list of players
	for p in players:
		with open(f'{p.name}/players', 'w') as f:
			# Sort it so that it isn't ordered by role
			f.write('\n'.join(sorted([l.name for l in players])))
	
	# Create a dictionary allowing you to look up player objects by their name
	name_to_player = dict(map(lambda p: (p.name, p), players))
	
	day = 0
	
	# Day 0 doesn't have a suspect or victim, every subsequent day does
	suspect, victim = None, None
	
	# Game loop, exits when mafia is dead or mafia outnumbers village
	while mafia and (len(players) - len(mafia)) > len(mafia):
		log(f'Day {day} begins.')
		
		# Randomize turn order every day. Bots /shouldn't/ be able to figure
		# this out, but who knows what you crazy kids will come up with. :P
		shuffle(players)
		
		# Print a message at the beginning of each day. On the first day, power
		# roles need to be old their role and mafia members need to know their
		# allies. On every other day, the cop needs to know the result of their
		# investigation and all players need to know who died.
		if day == 0:
			log(f'Cop: {cop.name}\nDoctor: {doctor.name}\nMafia: {", ".join(m.name for m in mafia)}')
			
			for p in players:
				p.add_message('Rise and shine! Today is day 0.\nNo voting will occur today.\nBe warned: Tonight the mafia will strike.')
			
			for m in mafia:
				m.add_message('\nYou are a member of the mafia.\nYour allies are:')
				m.add_message('\n'.join(p.name for p in mafia if p is not m))
			
			cop.add_message('You are the cop.')
			doctor.add_message('You are the doctor.')
		else:
			for p in players:
				p.add_message(f'Dawn of day {day}.')
				if victim is not None:
					p.add_message(f'Last night, {victim.name} was killed. They were {victim.get_role()}.')
			
			if victim is not None:
				players, mafia, cop, doctor = kill(victim, players, mafia, cop, doctor)
				log(f'{victim.name}, {victim.get_role()}, was killed.')
				if (not mafia) or len(mafia) >= (len(players) - len(mafia)):
					break
			
			if suspect is not None and cop is not None:
				cop.add_message(f'Investigations showed that {suspect.name} is {"mafia" if suspect.role == 1 else "village"}-aligned.')
			
			log(f'These players are still alive: {", ".join(p.name for p in players)}')
		
		m_write(players)
		
		# During a day, players may perform up to 50 actions (Action= vote or talk)
		for r in range(50):
			for p in players:
				try:
					execute(p)
					command = m_read(p).split()
					if command[0] == 'vote':
						# Set the player's vote
						if day != 0:
							if command[1] == 'no':
								if command[2] == 'one':
									p.vote = None
									log(f'{p.name} has voted to lynch no one.')
									for l in players:
										l.add_message(f'{p.name} has voted to lynch no one.')
							else:
								p.vote = name_to_player[command[1]]
								if p.vote in players:
									log(f'{p.name} has voted to lynch {command[1]}.')
									
									for l in players:
										l.add_message(f'{p.name} has voted to lynch {command[1]}.')
								else:
									p.vote = None
					elif command[0] == 'say':
						# Send a message to all players
						message = f'{p.name} says "'
						# Messages with an id higher than 4 have the name of a bot attached
						# This screws with parsing a bit so we handle them separately
						if int(command[1]) > 4:
							if len(command) == 4:
								# Convert from a name to a player object and back to ensure
								# that it's a correct name
								message += f'{name_to_player[command[3]].name}, '
							
							message += messages[int(command[1])]
							message += f'{name_to_player[command[2]].name}"'
						
						else:
							if len(command) == 3:
								message += f'{name_to_player[command[2]].name}, '
							
							message += f'{messages[int(command[1])]}"'
						
						log(message)
						for l in players:
							l.add_message(message)
				except (KeyError, IndexError):
					# Do nothing on invalid input
					pass
			
			m_write(players)
		
		# Tally up the votes for each player
		votes = [p.vote for p in players]
		
		# Shuffle to eliminate max() bias
		shuffle(votes)
		
		# The most voted player is lynched, with ties broken randomly
		lynched = max(votes, key=votes.count)
		if lynched is not None:
			log(f'The town has killed {lynched.name}!')
			log(f'They were {lynched.get_role()}.')
			for p in players:
				p.add_message(f"\nThe town has killed {lynched.name}!\nThey were {lynched.get_role}.")
			players, mafia, cop, doctor = kill(lynched, players, mafia, cop, doctor)
		else:
			log('The town opted to lynch no one today.')
			for p in players:
				p.add_message('The town opted to lynch no one today.')
		
		m_write(players)
		for p in players:
			execute(p)
			p.vote = None
		
		# Don't go to night if a win condition's been met.
		if not mafia or (len(players) - len(mafia)) <= len(mafia):
			break
		
		# Day ends, night begins
		
		# MAFIA NIGHT ACTION
		# Each mafioso votes for a victim. The most voted player is then killed,
		# unless saved that night by the doctor.
		for m in mafia:
			m.add_message('It is night. Vote for a victim.')
		m_write(mafia)
		
		victim_votes = []
		for m in mafia:
			try:
				execute(m)
				v = name_to_player[m_read(m)]
				
				if v in players:
					victim_votes.append(v)
					log(f'{m.name} votes to kill {victim_votes[-1].name}.')
				else:
					victim_votes.append(None)
					log(f'{m.name} votes to kill no one.')
			except (KeyError, IndexError):
				# Vote to kill no one on invalid input
				victim_votes.append(None)
				log(f'{m.name} votes to kill no one.')
		
		# Shuffle to eliminate max() bias
		shuffle(victim_votes)
		
		# The victim is the player most voted for by the mafia, with ties broken
		# randomly.
		victim = max(victim_votes, key=victim_votes.count)
		log(f'The mafia collectively decides to kill {victim.name if victim is not None else "no one"}.')
		
		# COP NIGHT ACTION
		# The cop chooses a player to investigate. At the dawn of the next day,
		# they are told whether that player is village- or mafia-aligned.
		if cop is not None:
			cop.add_message('It is night. Who would you like to investigate?')
			m_write(cop)
			try:
				execute(cop)
				suspect = name_to_player[m_read(cop)]
				log(f'{cop.name} spends the night investigating {suspect.name}.')
			except (KeyError, IndexError):
				# Investigate no one on invalid input
				suspect = None
				log(f'{cop.name} chooses not to investigate anyone.')
		
		# DOCTOR NIGHT ACTION
		# The doctor chooses a player they expect the mafia to try to kill. If they
		# are right, the mafia gets no kills that night.
		if doctor is not None:
			doctor.add_message('It is night. Who would you like to save?')
			m_write(doctor)
			try:
				execute(doctor)
				patient = name_to_player[m_read(doctor)]
				if patient == victim:
					victim = None
					log(f'{doctor.name} was able to save {patient.name} from near-certain death.')
				else:
					log(f'{doctor.name} tried to save {patient.name}, but they were not the target.')
			except (KeyError, IndexError):
				# Save no one on invalid input
				log(f'{doctor.name} took tonight off.')
		
		log('')
		day += 1
	
	if mafia:
		print('MAFIA VICTORY')
		log('MAFIA VICTORY')
	else:
		print('VILLAGE VICTORY')
		log('VILLAGE VICTORY')


if __name__ == '__main__':
	main()

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Generator
from dataclasses import dataclass, field

from input import input_value


@dataclass
class Game:
    initial_minimum: int
    initial_maximum: int
    current_minimum: int = field(init=False)
    current_maximum: int = field(init=False)
    
    def __post_init__(self):
        self.current_minimum = self.initial_minimum
        self.current_maximum = self.initial_maximum
    
    def run_game(self, guesser: Guesser, hinter: Hinter) -> int:
        guess_count = 0
        
        guesses = guesser.get_guesses()
        guess = next(guesses)
        
        hints = guesser.get_guesses()
        next(hints)
        
        while True:
            guess_count += 1
            hint = hints.send(guess)
            
            if hint > 0:
                self.current_minimum = max(self.current_minimum, guess + 1)
            elif hint < 0:
                self.current_maximum = min(self.current_maximum, guess - 1)
            else:
                guesses.send(hint)
                return guess_count
            
            if self.current_maximum < self.current_minimum:
                raise ValueError('Invalid set of hints.')
            
            guess = guesses.send(hint)


@dataclass
class Player:
    game: Game


class Guesser(Player, ABC):
    @abstractmethod
    def get_guesses(self) -> Generator[int, int, None]:
        pass


class Hinter(Player, ABC):
    @abstractmethod
    def get_hints(self) -> Generator[int, int, None]:
        pass


class ComputerGuesser(Guesser):
    def get_guesses(self) -> Generator[int, int, None]:
        while True:
            yield (self.game.current_minimum + self.game.current_maximum) // 2


class HumanGuesser(Guesser):
    def get_guesses(self) -> Generator[int, int, None]:
        while True:
            hint = yield input_value(int, prompt='Guess: ',
                                     error_message=f'Please enter an integer in the range '
                                                   f'[{self.game.initial_minimum}, {self.game.initial_maximum}]\n',
                                     constraints=frozenset(
                                         lambda x: self.game.initial_minimum <= x <= self.game.initial_maximum))
            
            if hint < 0:
                print('Try a smaller number.')
            elif hint > 0:
                print('Try a bigger number.')
            else:
                print('Correct!')

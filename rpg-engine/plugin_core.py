from typing import Tuple

import pygame

pygame.init()

__all__ = ['Window']


class Window:
    def __init__(self, *, size: Tuple[int, int] = (0, 0), flags: int = 0, **kwargs):
        self.flags = flags
        self.screen = pygame.display.set_mode(size, flags)

    def main_loop(self):
        """
        Override to add functionality.
        """

    def on_event(self, event: pygame.event.EventType):
        """
        Override to add event handlers. Make sure to call super(event).
        """

    def run(self):
        while True:
            for event in iter(pygame.event.poll, pygame.event.Event(pygame.NOEVENT)):
                self.on_event(event)

            self.main_loop()

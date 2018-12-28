import pygame

from plugin_core import Window

__all__ = ['QuitableWindow']


class QuitableWindow(Window):
    def on_event(self, event: pygame.event.EventType):
        super().on_event(event)

        if event.type == pygame.QUIT:
            exit()

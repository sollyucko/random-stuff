from typing import Tuple

import pygame

from plugin_core import Window

__all__ = ['ResizableWindow']


class ResizableWindow(Window):
    def __init__(self, *, flags: int = 0, size: Tuple[int, int] = (0, 0), **kwargs):
        super().__init__(size=size, flags=(flags | pygame.RESIZABLE), **kwargs)
        self.size = size

    def on_event(self, event: pygame.event.EventType):
        super().on_event(event)

        if event.type == pygame.VIDEORESIZE:
            self.screen = pygame.display.set_mode(event.size, self.flags)

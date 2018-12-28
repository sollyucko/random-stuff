from typing import Set

import pygame

from plugin_core import Window

__all__ = ['Object', 'ObjectWindow']


class Object:
    def draw(self, screen: pygame.Surface):
        pass


class SurfaceObject:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.rect = surface.get_rect()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)

    def move(self, x: int, y: int):
        self.rect = self.rect.move(x, y)


class ObjectWindow(Window):
    def __init__(self, *, background=(0, 0, 0), objects: Set[Object] = set(), **kwargs):
        super().__init__(background=background, objects=objects, **kwargs)

        self.background = background
        self.objects = objects

    def add_object(self, obj: Object):
        self.objects.add(obj)

    def on_event(self, event: pygame.event.EventType):
        super().on_event(event)

    def main_loop(self):
        super().main_loop()

        self.screen.fill(self.background)

        for obj in self.objects:
            obj.draw(self.screen)

        pygame.display.flip()

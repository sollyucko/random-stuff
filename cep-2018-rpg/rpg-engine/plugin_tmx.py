from typing import Tuple

import pygame

import tmx
from plugin_objects import ObjectWindow


class TMXWindow(ObjectWindow):
    def __init__(self, *, size: Tuple[int, int] = (0, 0), start_map_path: str, focus: Tuple[int, int] = (0, 0),
                 tickrate: int, **kwargs):
        super().__init__(size=size, **kwargs)

        self.clock = pygame.time.Clock()
        self.tilemap: tmx.TileMap = None
        self.set_tilemap(map_path=start_map_path, focus=focus)
        self.tickrate = tickrate

    def set_tilemap(self, *, map_path: str, focus: Tuple[int, int] = (0, 0)):
        try:
            self.objects.remove(self.tilemap)
        except KeyError:
            pass

        rect = self.screen.get_rect()

        self.tilemap = tmx.load(map_path, (rect.height, rect.width))
        self.tilemap.set_focus(*focus)
        self.objects.add(self.tilemap)

    def main_loop(self):
        super().main_loop()

        self.tilemap.update(self.clock.tick(self.tickrate))

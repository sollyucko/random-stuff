from os import chdir
from pathlib import Path

import pygame

from plugin_rpg import Direction, Foot, RPGWindow

START_SIZE = 640, 480
TICK_RATE = 10
TILE_SIZE = 32
FONT_COLOR = (238, 58, 140)

BASE_DIR = Path(__file__).parent
RESOURCES_DIR = BASE_DIR / 'testrpg_resources'

BALL_PATH = RESOURCES_DIR / 'intro_ball.gif'
MAP_PATH = RESOURCES_DIR / 'outside.tmx'
PLAYER_ICON_DIR = RESOURCES_DIR / 'player_icons'
ENEMY_ICON_PATH = RESOURCES_DIR / 'enemy.png'

PLAYER_HP = 100
ENEMY_HP = 10


def main():
    chdir(RESOURCES_DIR)
    player_icons = {
        (direction, foot): pygame.transform.smoothscale(
            pygame.image.load(str(
                PLAYER_ICON_DIR / 'player-{direction}-{foot}_foot.png'.format(direction=direction.name.lower(),
                                                                              foot=foot.name.lower()))),
            (TILE_SIZE, TILE_SIZE))
        for direction in Direction
        for foot in Foot
    }
    
    enemy_icon = pygame.transform.smoothscale(pygame.image.load(str(ENEMY_ICON_PATH)), (TILE_SIZE, TILE_SIZE))
    RPGWindow(size=START_SIZE, start_map_path=MAP_PATH, tickrate=TICK_RATE, enemy_icon=enemy_icon, tile_size=TILE_SIZE,
              enemy_hp=ENEMY_HP, player_hp=PLAYER_HP, font_color=FONT_COLOR, player_icons=player_icons).run()


if __name__ == '__main__':
    main()

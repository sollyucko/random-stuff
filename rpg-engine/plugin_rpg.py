from enum import Enum, auto
from operator import itemgetter
from random import choice, random
from typing import Dict, Optional, Tuple, Union

import pygame

import tmx
from plugin_quitable import QuitableWindow
from plugin_resizable import ResizableWindow
from plugin_tmx import TMXWindow

__all__ = ['RPGWindow', 'Direction', 'Foot']


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Foot(Enum):
    LEFT = auto()
    RIGHT = auto()


class RPGWindow(QuitableWindow, ResizableWindow, TMXWindow):
    def __init__(self, *, enemy_icon: pygame.Surface, tile_size: int = 1, enemy_hp: float, player_hp: float,
                 font_color: Tuple[int, int, int], player_icons: Dict[Tuple[Direction, Foot], pygame.Surface],
                 **kwargs):
        self.font_color = font_color
        self.enemy_hp = enemy_hp
        self.enemy_icon = enemy_icon
        self.tile_size = tile_size

        self.map_path = ''
        self.sprite_layer_stack = {}
        self.sprites = tmx.SpriteLayer()
        self.start_cell = (0, 0)
        super().__init__(enemy_icon=enemy_icon, tile_size=tile_size, enemy_hp=enemy_hp, player_hp=player_hp,
                         font_color=font_color, player_icons=player_icons, **kwargs)
        self.player = Player(self.sprites, images={key: icon.convert_alpha() for key, icon in player_icons.items()},
                             window=self, location=self.start_cell, hp=player_hp)

        self.init_talk_characters()
    
    def set_tilemap(self, *, map_path: str, start_cell: Optional[Tuple[int, int]] = None, **kwargs):
        self.sprite_layer_stack[self.map_path] = self.sprites

        self.map_path = map_path

        try:
            self.sprites = self.sprite_layer_stack[map_path]
        except KeyError:
            self.sprites = tmx.SpriteLayer()

        try:
            player = self.player
        except AttributeError:
            pass
        else:
            self.sprites.add(player)
        
        super().set_tilemap(map_path=map_path)

        self.init_talk_characters()
        
        self.tilemap.layers.append(self.sprites)

        if start_cell is None:
            start_cell = choice(self.tilemap.layers['triggers'].match(isStart='true'))
            start_cell = start_cell.px, start_cell.py

        self.tilemap.set_focus(*start_cell, force=True)

        try:
            player = self.player
        except AttributeError:
            self.start_cell = start_cell
        else:
            player.rect.x, player.rect.y = start_cell

    def spawn(self, enemy: 'Enemy'):
        self.sprites.add(enemy)

    def display_text(self, text: str, position: Tuple[int, int] = (0, 0)):
        size = min(get_text_size(text, self.screen.get_rect().width), self.screen.get_rect().height)
        self.screen.blit(render_text(text, size, self.font_color), position)
        # self.screen.blit(render_text_old(text, self.screen.get_rect().width, self.screen.get_rect().height, self.font_color), position)

    def show_big_text(self, text: str, position: Tuple[int, int] = (0, 0)):
        self.screen.fill(self.background)

        for obj in self.objects:
            obj.draw(self.screen)

        self.display_text(text, position)
        pygame.display.flip()

        while not pygame.key.get_pressed()[pygame.K_RETURN]:
            for event in iter(pygame.event.poll, pygame.event.Event(pygame.NOEVENT)):
                self.on_event(event)

        # prevent multiple messages accidentally being closed simultaneously
        while pygame.key.get_pressed()[pygame.K_RETURN]:
            for event in iter(pygame.event.poll, pygame.event.Event(pygame.NOEVENT)):
                self.on_event(event)

    @staticmethod
    def collide_rects(rect1, rect2):
        # Don't use pygame.Rect.collide_rect because of the *edge* case handling

        if rect1.right <= rect2.left:
            return False

        if rect2.right <= rect1.left:
            return False

        if rect1.bottom <= rect2.top:
            return False

        if rect2.bottom <= rect1.top:
            return False

        return True

    def collide_border(self, location):
        window_rect = pygame.Rect(self.tilemap.view_x, self.tilemap.view_y, self.tilemap.px_width,
                                  self.tilemap.px_height)

        if window_rect.right < location.right:
            return True
        if window_rect.left > location.left:
            return True
        if window_rect.bottom < location.bottom:
            return True
        if window_rect.top > location.top:
            return True

        return False

    def collide_sprite(self, location: pygame.Rect):
        collisions = set()

        for sprite2 in self.sprites:
            if sprite2.rect is not location:
                if self.collide_rects(location, sprite2.rect):
                    collisions.add(sprite2)
        
        return collisions

    def collide_objects(self, location: pygame.Rect):
        for obj in self.tilemap.layers['triggers'].collide(location, 'isSolid'):
            if self.collide_rects(location, obj):
                return True

        return False
    
    def can_move(self, location: pygame.Rect):
        return not self.collide_objects(location) and not self.collide_border(location)

    def init_talk_characters(self):
        for talk_character in self.tilemap.layers['people'].find('icon'):
            image = pygame.image.load(talk_character['icon'])
            image = image.convert_alpha()
            image = pygame.transform.smoothscale(image, (self.tile_size, self.tile_size))
            self.sprites.add(TalkCharacter(window=self, image=image, location=(talk_character.top, talk_character.left),
                                           text=talk_character['text']))


class Entity(pygame.sprite.Sprite):
    def __init__(self, *groups, location: Tuple[int, int], window: RPGWindow, hp: float):
        super().__init__(*groups)
        self.image = self.get_image()
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.window = window
        self.hp = hp
        self.show_hp()
    
    def show_hp(self):
        self.image = self.get_image()
        self.image.blit(
            render_text(
                str(self.hp),
                min(
                    get_text_size(
                        str(self.hp),
                        self.rect.width
                    ),
                    self.rect.height
                ),
                self.window.font_color
            ),
            (0, 0)
        )
        # self.image.blit(self.window.render_text_old(str(self.hp), self.rect.width, self.rect.height), (0, 0))
    
    def get_image(self):
        """Override this and return the image to display."""


class Player(Entity):
    def __init__(self, *groups, images: Dict[Tuple[Direction, Foot], pygame.Surface], location: Tuple[int, int],
                 window: RPGWindow, hp: float):
        self.direction = Direction.UP
        self.foot = Foot.LEFT
        self.images = images

        super().__init__(*groups, location=location, window=window, hp=hp)
    
    def get_image(self):
        return self.images[self.direction, self.foot].copy()

    def update(self, dt):
        old = self.rect.copy()
        new = self.rect.copy()
        
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            self.direction = Direction.UP
            self.animate_walk()
            new.y -= self.rect.height
        if key[pygame.K_DOWN]:
            self.direction = Direction.DOWN
            self.animate_walk()
            new.y += self.rect.height
        if key[pygame.K_LEFT]:
            self.direction = Direction.LEFT
            self.animate_walk()
            new.x -= self.rect.width
        if key[pygame.K_RIGHT]:
            self.direction = Direction.RIGHT
            self.animate_walk()
            new.x += self.rect.width

        if not self.window.collide_objects(new) and not self.window.collide_border(new):
            self.rect = new

        if old != new:
            for enemy in self.window.collide_sprite(self.rect):
                self.rect = old
                enemy.attack(1)

            for enemy in self.window.sprites:
                if enemy is not self:
                    enemy.tick()

        for area in self.window.tilemap.layers['triggers'].collide(self.rect, 'probEnemy'):
            if old != self.rect and random() < float(area['probEnemy']):
                enemy_rect = self.rect
                self.rect = old
                self.window.spawn(Enemy(image=self.window.enemy_icon, location=enemy_rect.topleft, window=self.window,
                                        hp=self.window.enemy_hp))

        entries = self.window.tilemap.layers['triggers'].collide(self.rect, 'destinationMap')

        if entries:
            entry = choice(entries)
            self.window.set_tilemap(map_path=entry['destinationMap'],
                                    start_cell=(entry['destinationX'], entry['destinationY']))

        self.window.tilemap.set_focus(self.rect.x, self.rect.y)

    def attack(self, damage: float):
        self.hp -= damage

        if self.hp <= 0:
            self.show_hp()
            self.window.tilemap.draw(self.window.screen)
            self.window.show_big_text('You lose :(')
            pygame.display.quit()
            pygame.quit()
            exit()
        else:
            self.show_hp()

    def animate_walk(self):
        self.foot = Foot.LEFT if self.foot == Foot.RIGHT else Foot.RIGHT
        self.show_hp()


class Enemy(Entity):
    def __init__(self, *groups, image: pygame.Surface, location: Tuple[int, int], window: RPGWindow, hp: float):
        self.original_image = image

        super().__init__(*groups, location=location, window=window, hp=hp)

    def get_image(self):
        return self.original_image.copy()

    def attack(self, damage: float):
        self.hp -= damage

        if self.hp <= 0:
            self.show_hp()
            self.window.tilemap.draw(self.window.screen)
            self.window.show_big_text('You killed an enemy!')
            self.kill()
        else:
            self.show_hp()

    def move(self, direction: Direction, distance: int = 1):
        rect = self.rect.copy()

        if direction == Direction.UP:
            rect.y -= self.rect.height * distance
        elif direction == Direction.DOWN:
            rect.y += self.rect.height * distance
        elif direction == Direction.LEFT:
            rect.x -= self.rect.width * distance
        elif direction == Direction.RIGHT:
            rect.x += self.rect.width * distance

        return rect

    def tick(self):
        if is_adjacent(self.window, self.rect):
            self.window.player.attack(1)
        else:
            try:
                self.rect = self.move(
                    max(
                        (
                            (direction, distance)
                            for direction, distance
                            in get_distances(self.window.player.rect, self.rect).items()
                            if not self.window.collide_objects(self.move(direction)) and not self.window.collide_border(
                            self.move(direction)) and not self.window.collide_sprite(self.move(direction))
                        ),
                        key=itemgetter(1)
                    )[0]
                )
            except ValueError:
                pass  # If it's impossible to move, don't move.


class TalkCharacter(pygame.sprite.Sprite):
    def __init__(self, *groups, location: Tuple[int, int], window: RPGWindow, image: pygame.Surface, text: str):
        super().__init__(*groups)
        self.image = image
        self.rect = pygame.rect.Rect(location, self.image.get_size())
        self.window = window
        self.text = text
    
    def attack(self, damage: float):
        for line in self.text.split('\n'):
            self.window.show_big_text(line)
    
    def tick(self):
        pass


def get_player_distances(window, rect):
    return get_distances(window.player.rect, rect)


def get_distances(rect_1, rect_2):
    return {
        Direction.LEFT:  (rect_2.left - rect_1.right) // rect_2.width,
        Direction.RIGHT: (rect_1.left - rect_2.right) // rect_2.width,
        Direction.UP:    (rect_2.top - rect_1.bottom) // rect_2.height,
        Direction.DOWN:  (rect_1.top - rect_2.bottom) // rect_2.height
    }


def is_adjacent(window, rect):
    return all(distance <= 0 for distance in get_distances(window.player.rect, rect).values())


def render_text_old(text: str, width: int, height: int,
                    color: Union[Tuple[int, int, int], pygame.Color]) -> pygame.Surface:
    size = min(get_text_size(text, width), height)
    return render_text(text, size, color)


def render_text(text: str, size: int, color: Union[Tuple[int, int, int], pygame.Color]) -> pygame.Surface:
    return pygame.font.Font(None, int(size)).render(text, True, color)


def get_text_size(text: str, width: int, test_factor: int = 100000) -> int:
    # if test_factor is too large, overflow may occur; if too small, precision will be lost
    return int(width * test_factor / pygame.font.Font(None, test_factor).size(text)[0])

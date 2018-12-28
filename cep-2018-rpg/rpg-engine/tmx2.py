from enum import Enum, auto
from typing import List, Union

import pygame
from lxml import etree


class Orientation(Enum):
    ORTHOGONAL = auto()
    ISOMETRIC = auto()
    STAGGERED = auto()
    HEXAGONAL = auto()


class RenderOrder(Enum):
    RIGHT_DOWN = auto()
    RIGHT_UP = auto()
    LEFT_DOWN = auto()
    LEFT_UP = auto()


class SizeInTiles(int):
    pass


class SizeInPixels(int):
    pass


class LayerID(int):
    pass


class ObjectID(int):
    pass


class Axis(Enum):
    X = auto()
    Y = auto()


class Parity(Enum):
    EVEN = auto()
    ODD = auto()


Color = Union[str, pygame.Color]


class Tileset:
    @classmethod
    def from_xml(cls, xml: etree.Element):
        pass


class Map:
    def __init__(self, *, version: str, tiledversion: str, orientation: Orientation,
                 renderorder: RenderOrder = RenderOrder.RIGHT_DOWN, width: SizeInTiles, height: SizeInTiles,
                 tilewidth: SizeInPixels, tileheight: SizeInPixels, hexsidelength: SizeInPixels = None,
                 staggeraxis: Axis = None, staggerindex: Parity = None, backgroundcolor: Color = None,
                 nextlayerid: LayerID, nextobjectid: ObjectID, tilesets: List[Tileset] = (), **kwargs):
        self.__dict__.update(kwargs)
        self.version = version
        self.tiledversion = tiledversion
        self.orientation = orientation
        self.renderorder = renderorder
        self.width = width
        self.height = height
        self.tilewidth = tilewidth
        self.tileheight = tileheight
        
        if orientation in {Orientation.HEXAGONAL}:
            self.hexsidelength = hexsidelength
        
        if orientation in {Orientation.STAGGERED, Orientation.HEXAGONAL}:
            self.staggeraxis = staggeraxis
            self.staggerindex = staggerindex
        
        self.backgroundcolor = backgroundcolor
        self.nextlayerid = nextlayerid
        self.nextobjectid = nextobjectid
    
    @classmethod
    def from_xml(cls, xml: etree.Element):
        cls(**xml)

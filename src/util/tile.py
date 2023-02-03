from dataclasses import dataclass
from pygame import Rect
from .constants import TILE_SIZE
@dataclass
class Tile:
    x : int
    y : int
    piece : object = None
    rect = None
    def __post_init__(self):
        self.rect = Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)